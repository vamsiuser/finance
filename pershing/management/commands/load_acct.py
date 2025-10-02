from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction
from dataclasses import dataclass
from typing import Dict, List, Tuple
import itertools, datetime, os

from pershing.constants import EXTRA_LAYOUT, LEAD_LAYOUT, RECORD_TABLE_MAP

HEADER_SENTINEL  = "BOF"
TRAILER_SENTINEL = "EOF PERSHING"

# ---- table name map (edit to match your MySQL table names) ----
# If your tables are named without schema prefixes in MySQL, keep just the bare names.
HEADER_TABLE  = "ACCT_ACCF_Header"
TRAILER_TABLE = "ACCT_ACCF_Trailer"

# ---- fixed-width helpers ----
def seg(s: str, start1: int, end1: int) -> str:
    """1-based inclusive -> python slice, rstrip spaces"""
    return s[start1-1:end1].rstrip()

# Shared leading fields present on most detail records per layout:


def pos(start, end_inclusive):
    """Convert spec positions (1-based, inclusive) into Python slice tuple."""
    return (start - 1, end_inclusive)

# Add per-record extras here as you map more fields from the spec

AUDIT_COLUMN = "LastUpdateDate"   # many of your tables require this NOT NULL

@dataclass
class TableMeta:
    name: str
    columns: List[str]
    pk_cols: List[str]
    not_null: List[str]
    
def upsert_mysql(table: str, rows: List[Dict[str, object]], meta: TableMeta):
    if not rows:
        return
    # unify set of columns across rows
    colset = set()
    for r in rows:
        colset.update(r.keys())
    cols = sorted(colset)

    placeholders = "(" + ",".join(["%s"] * len(cols)) + ")"
    insert_sql = f"INSERT INTO `{table}` ({', '.join('`'+c+'`' for c in cols)}) VALUES {', '.join([placeholders]*len(rows))}"

    # ON DUPLICATE KEY UPDATE all columns to VALUES(col) (except PKs if you prefer to skip)
    update_assign = ", ".join([f"`{c}`=VALUES(`{c}`)" for c in cols if c not in meta.pk_cols])
    if not update_assign:
        update_assign = f"`{cols[0]}`=VALUES(`{cols[0]}`)"  # fallback

    sql = insert_sql + f" ON DUPLICATE KEY UPDATE {update_assign}"

    params: List[object] = []
    for r in rows:
        params.extend([r.get(c) for c in cols])

    with connection.cursor() as cur:
        cur.execute(sql, params)

def get_table_meta(table: str) -> TableMeta:
    with connection.cursor() as cur:
        # columns + nullability
        cur.execute("""
            SELECT COLUMN_NAME, IS_NULLABLE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = %s
            ORDER BY ORDINAL_POSITION
        """, [table])
        cols, not_null = [], []
        for c, isnull in cur.fetchall():
            cols.append(c)
            if isnull == "NO":
                not_null.append(c)
        # primary key columns (in order)
        cur.execute("""
            SELECT kcu.COLUMN_NAME
            FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
            JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
              ON tc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
             AND tc.TABLE_SCHEMA = kcu.TABLE_SCHEMA
             AND tc.TABLE_NAME = kcu.TABLE_NAME
            WHERE tc.TABLE_SCHEMA = DATABASE()
              AND tc.TABLE_NAME = %s
              AND tc.CONSTRAINT_TYPE='PRIMARY KEY'
            ORDER BY kcu.ORDINAL_POSITION
        """, [table])
        pk_cols = [r[0] for r in cur.fetchall()]
    return TableMeta(table, cols, pk_cols, not_null)

def build_row(line: str, rec_type: str, meta: TableMeta) -> Dict[str, object]:
    if rec_type == "Header":
        layout = EXTRA_LAYOUT.get("HEADER", {})
    elif rec_type == "Trailer":
        layout = EXTRA_LAYOUT.get("TRAILER", {})
    else:
        layout = {**LEAD_LAYOUT, **EXTRA_LAYOUT.get(rec_type, {})}
    row = {}
    for col, (a,b) in layout.items():
        if col in meta.columns:
            row[col] = seg(line, a, b)
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
        if r in['BirthDate', 'DateTaxIDAppliedFor','FromDate2','FromDate3','MostRecentMailReturnDate','SecondMostRecentMailReturnDate','ThirdMostRecentMailReturnDate','AgreementExecDate'] and row[r] == "00000000":
            row[r] = None
        if row[r] == "00000000":
            row[r] = None
        if r in ['ToDate1','ToDate2','ToDate3']:
            row[r] = None
            
    return row

def chunks(it, n=1000):
    it = iter(it)
    while True:
        block = list(itertools.islice(it, n))
        if not block:
            return
        yield block

def z(table: str, rows: List[Dict[str, object]], meta: TableMeta):
    if not rows:
        return
    # unify set of columns across rows
    colset = set()
    for r in rows:
        colset.update(r.keys())
    cols = sorted(colset)

    placeholders = "(" + ",".join(["%s"] * len(cols)) + ")"
    insert_sql = f"INSERT INTO `{table}` ({', '.join('`'+c+'`' for c in cols)}) VALUES {', '.join([placeholders]*len(rows))}"

    # ON DUPLICATE KEY UPDATE all columns to VALUES(col) (except PKs if you prefer to skip)
    update_assign = ", ".join([f"`{c}`=VALUES(`{c}`)" for c in cols if c not in meta.pk_cols])
    if not update_assign:
        update_assign = f"`{cols[0]}`=VALUES(`{cols[0]}`)"  # fallback

    sql = insert_sql + f" ON DUPLICATE KEY UPDATE {update_assign}"

    params: List[object] = []
    for r in rows:
        params.extend([r.get(c) for c in cols])

    with connection.cursor() as cur:
        cur.execute(sql, params)
        
def is_header(line: str) -> bool:
    s = line.lstrip("\ufeff ")   # strip BOM + leading spaces
    return s.startswith("BOF")

def is_trailer(line: str) -> bool:
    s = line.lstrip("\ufeff ")
    return s.startswith("EOF")

class Command(BaseCommand):
    help = "Load ACCT/ACCF file into MySQL via Django"

    def add_arguments(self, parser):
        parser.add_argument("path", help="Path to ACCT/ACCF flat file")

    @transaction.atomic
    def handle(self, *args, **opts):
        path = opts["path"]
        if not os.path.exists(path):
            raise CommandError(f"File not found: {path}")

        meta_cache: Dict[str, TableMeta] = {}
        def meta_for(table: str) -> TableMeta:
            if table not in meta_cache:
                meta_cache[table] = get_table_meta(table)
            return meta_cache[table]

        header_rows, trailer_rows = [], []
        detail_rows: Dict[str, List[Dict[str, object]]] = {t: [] for t in RECORD_TABLE_MAP.values()}
        
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            for ln, raw in enumerate(fh, 1):
                line = raw.rstrip("\r\n")
                
                if not line:
                    continue
                
                if is_header(line):
                    m = meta_for(HEADER_TABLE)
                    row = build_row(line, "Header", m)
                    header_rows.append(row)
                    continue

                if is_trailer(line):
                    m = meta_for(TRAILER_TABLE)
                    row = build_row(line, "Trailer", m)
                    trailer_rows.append(row)
                    continue

                if len(line) < 3:
                    raise CommandError(f"Line {ln}: too short")
                
                rec = line[2]  # column 3 in spec
                if rec not in RECORD_TABLE_MAP:
                    raise CommandError(f"Line {ln}: unknown record indicator '{rec}'")
                
                tname = RECORD_TABLE_MAP[rec]
                m = meta_for(tname)
                row = build_row(line, rec, m)
                detail_rows[tname].append(row)
        print(detail_rows,"detail_rowsdetail_rowsdetail_rowsdetail_rows")

        # batch UPSERTs
        try:
            if header_rows:
                upsert_mysql(HEADER_TABLE, header_rows, meta_for(HEADER_TABLE))
            for tname, rows in detail_rows.items():
                print(tname,rows,"++++++++++++++++++++++++++++")
                for block in chunks(rows, 1000):
                    upsert_mysql(tname, block, meta_for(tname))
            if trailer_rows:
                upsert_mysql(TRAILER_TABLE, trailer_rows, meta_for(TRAILER_TABLE))
        except Exception as e:
            print(e,"eeeeeeeeeeeeeeeeee")
            raise CommandError(str(e))

        self.stdout.write(self.style.SUCCESS("Load complete."))
