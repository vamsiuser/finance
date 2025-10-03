HEADER_SENTINEL  = "BOF"
TRAILER_SENTINEL = "EOF PERSHING"

HEADER_TABLE  = "ACCT_ACCF_Header"
TRAILER_TABLE = "ACCT_ACCF_Trailer"

AUDIT_COLUMN = "LastUpdateDate"

RECORD_TABLE_MAP = {
    "A": "ACCT_ACCF_A",
    "B": "ACCT_ACCF_B",
    "C": "ACCT_ACCF_C",
    "D": "ACCT_ACCF_D",
    "E": "ACCT_ACCF_E",
    "F": "ACCT_ACCF_F",
    "G": "ACCT_ACCF_G",
    "H": "ACCT_ACCF_H",
    "I": "ACCT_ACCF_I",
    "J": "ACCT_ACCF_J",
    "K": "ACCT_ACCF_K",
    "L": "ACCT_ACCF_L",
    "M": "ACCT_ACCF_M",
    "N": "ACCT_ACCF_N",
    "P": "ACCT_ACCF_P",
    "R": "ACCT_ACCF_R",
    "S": "ACCT_ACCF_S",
    "T": "ACCT_ACCF_T",
    "U": "ACCT_ACCF_U",
    "W": "ACCT_ACCF_W",
    "X": "ACCT_ACCF_X",
    "4": "ACCT_ACCF_4",
    "5": "ACCT_ACCF_5",
    "7": "ACCT_ACCF_7",
}

LEAD_LAYOUT = {
    "TransactionCode":        (1, 2),   # e.g., “CI”
    "RecordIndicatorValue":   (3, 3),   # e.g., “A”
    "RecordIDSequenceNumber": (4, 11),  # “00000001…”
    "AccountNumber":          (12, 20), # office(3)+base(6)
    "IBDNumber":              (21, 23),
}