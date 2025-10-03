from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List
from django.core.exceptions import ValidationError
import itertools, datetime
from pershing.sqlprocess.acct_sql import upsert_mysql, get_table_meta
from pershing.constants import ACCT_5_DATEFIELDS, ACCT_A_DATEFIELDS, ACCT_B_DATEFIELDS, ACCT_C_DATEFIELDS, EXTRA_LAYOUT
from pershing.indexmapping.acct.other_mapping import LEAD_LAYOUT, RECORD_TABLE_MAP, HEADER_SENTINEL, TRAILER_SENTINEL, HEADER_TABLE, TRAILER_TABLE, AUDIT_COLUMN


@dataclass
class TableMeta:
    name: str
    columns: List[str]
    pk_cols: List[str]
    not_null: List[str]

class loadAcctFilesManager(object):
    def __init__(self):
        self.meta_cache: Dict[str, TableMeta] = {}
        
    def is_header(self, line: str) -> bool:
        s = line.lstrip("\ufeff ")
        return s.startswith("BOF")

    def is_trailer(self, line: str) -> bool:
        s = line.lstrip("\ufeff ")
        return s.startswith("EOF")
    def seg(self, s: str, start1: int, end1: int) -> str:
        """1-based inclusive -> python slice, rstrip spaces"""
        return s[start1-1:end1].rstrip()
    
    
    def meta_for(self, table: str) -> TableMeta:
        if table not in self.meta_cache:
            self.meta_cache[table] = get_table_meta(table)
        return self.meta_cache[table]
    def chunks(self, it, n=1000):
        it = iter(it)
        while True:
            block = list(itertools.islice(it, n))
            if not block:
                return
            yield block

    def build_row(self, line: str, rec_type: str, meta: TableMeta) -> Dict[str, object]:
        if rec_type == "Header":
            layout = EXTRA_LAYOUT.get("HEADER", {})
        elif rec_type == "Trailer":
            layout = EXTRA_LAYOUT.get("TRAILER", {})
        else:
            layout = {**LEAD_LAYOUT, **EXTRA_LAYOUT.get(rec_type, {})}
        row = {}
        for col, (a,b) in layout.items():
            if col in meta.columns:
                row[col] = self.seg(line, a, b)
        # stamp audit if present
        if AUDIT_COLUMN in meta.columns:
            row[AUDIT_COLUMN] = datetime.datetime.utcnow()
        if rec_type in["Header","Trailer"]:
            row['IBDNumber'] = "AAA"
        
        if "DateOfData" in row and row["DateOfData"]:
            try:
                row["DateOfData"] = datetime.datetime.strptime(row["DateOfData"], "%m/%d/%Y").date()
            except ValueError:
                raise ValueError(f"{meta.name}: invalid DateOfData '{row['DateOfData']}'")
            
        # basic integrity: all PKs present and non-empty
        missing = [c for c in meta.pk_cols if (c not in row) or (str(row[c]).strip() == "")]
        if missing:
            raise ValueError(f"{meta.name}: missing PK fields {missing}. Add their positions in EXTRA_LAYOUT.")
        for r in row:
            if row[r] == "":
                row[r] = None
            if row[r] in["00000000","000000"]:
                row[r] = None
            if 'RecordIndicatorValue' in row and row['RecordIndicatorValue'] == "A":
                if r in ACCT_A_DATEFIELDS:
                    try:
                        row[r] = datetime.datetime.strptime(row[r], "%Y%m%d").date() if row[r] else None
                    except:
                        row[r] = None
                    
                if 'CommissionPercentDiscount' in r:
                    if row[r]:
                        whole = row[r][:-9] or "0"
                        frac  = row[r][-9:]
                        row[r] = Decimal(f"{int(whole)}.{frac}")
                        
            if 'RecordIndicatorValue' in row and row['RecordIndicatorValue'] == "B":
                if r in ACCT_B_DATEFIELDS:
                    try:
                        row[r] = datetime.datetime.strptime(row[r], "%Y%m%d").date() if row[r] else None
                    except:
                        row[r] = None
            if 'RecordIndicatorValue' in row and row['RecordIndicatorValue'] == "C":
                if r in ACCT_C_DATEFIELDS:
                    try:
                        row[r] = datetime.datetime.strptime(row[r], "%Y%m%d").date() if row[r] else None
                    except:
                        row[r] = None
            if 'RecordIndicatorValue' in row and row['RecordIndicatorValue'] == "5":
                if r in ACCT_5_DATEFIELDS:
                    print(r,"-----------")
                    try:
                        row[r] = datetime.datetime.strptime(row[r], "%Y%m%d").date() if row[r] else None
                    except:
                        row[r] = None
            
            if 'RecordIndicatorValue' in row and row['RecordIndicatorValue'] == "T":
                if 'PercentAllocation' in r:
                    if row[r]:
                        whole = row[r][:-9] or "0"
                        frac  = row[r][-9:]
                        row[r] = Decimal(f"{int(whole)}.{frac}")
        return row
    
    def process_block(self, lines):
        header_rows, trailer_rows = [], []
        detail_rows: Dict[str, List[Dict[str, object]]] = {t: [] for t in RECORD_TABLE_MAP.values()}
        for line, raw in lines:
            line = raw.rstrip("\r\n")
            if not line:
                continue
            if self.is_header(line):
                m = self.meta_for(HEADER_TABLE)
                row = self.build_row(line, "Header", m)
                header_rows.append(row)
                continue

            if self.is_trailer(line):
                m = self.meta_for(TRAILER_TABLE)
                row = self.build_row(line, "Trailer", m)
                trailer_rows.append(row)
                continue

            if len(line) < 3:
                raise (f"Line {line}: too short")
            
            rec = line[2]  # column 3 in spec
            if rec not in RECORD_TABLE_MAP:
                raise ValidationError(f"Line {line}: unknown record indicator '{rec}'")
            
            tname = RECORD_TABLE_MAP[rec]
            m = self.meta_for(tname)
            row = self.build_row(line, rec, m)
            detail_rows[tname].append(row)
        # batch UPSERTs
        try:
            if header_rows:
                upsert_mysql(HEADER_TABLE, header_rows, self.meta_for(HEADER_TABLE))
            for tname, rows in detail_rows.items():
                for block in self.chunks(rows, 100):
                    upsert_mysql(tname, block, self.meta_for(tname))
            if trailer_rows:
                upsert_mysql(TRAILER_TABLE, trailer_rows, self.meta_for(TRAILER_TABLE))
        except Exception as e:
            print(row)
            raise ValidationError(str(e))