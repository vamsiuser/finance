from dataclasses import dataclass
from typing import Dict, List, Tuple
from django.db import connection, transaction

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