LEAD_LAYOUT = {
    "TransactionCode":        (1, 2),   # e.g., “CI”
    "RecordIndicatorValue":   (3, 3),   # e.g., “A”
    "RecordIDSequenceNumber": (4, 11),  # “00000001…”
    "AccountNumber":          (12, 20), # office(3)+base(6)
    "IBDNumber":              (21, 23),
}

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

def pos(start, end_inclusive):
    """Convert spec positions (1-based, inclusive) into Python slice tuple."""
    return (start - 1, end_inclusive)

EXTRA_LAYOUT = {
    # -------------------------
    # FILE HEADER / TRAILER
    # -------------------------
    "HEADER": {
        "literal_bof": pos(1, 18),                 # "BOF PERSHING "
        "literal_customer_acct_info": pos(19, 36), # "CUSTOMER ACCT INFO"
        "literal_data_of": pos(37, 46),            # " DATA OF "
        "date_of_data": pos(47, 56),               # "MM/DD/CCYY"
        "literal_to_remote": pos(57, 67),          # " TO REMOTE "
        "remote_id": pos(68, 71),
        "literal_begins_here": pos(72, 85),        # " BEGINS HERE "
        "run_date": pos(86, 95),                   # "MM/DD/CCYY"
        "run_time": pos(97, 104),                  # "HH:MM:SS"
        "refresh_or_update": pos(119, 127),        # "REFRESHED"/"UPDATED "
        "end_marker": pos(750, 750),               # "A"
    },  # :contentReference[oaicite:0]{index=0}

    "TRAILER": {
        "literal_eof": pos(1, 18),                 # "EOF PERSHING "
        "literal_customer_acct_info": pos(19, 36), # "CUSTOMER ACCT INFO"
        "literal_data_of": pos(37, 46),            # " DATA OF "
        "date_of_data": pos(47, 56),               # "MM/DD/CCYY"
        "literal_to_remote": pos(57, 67),          # " TO REMOTE "
        "remote_id": pos(68, 71),
        "literal_ends_here": pos(72, 83),          # " ENDS HERE. "
        "literal_total_detail": pos(84, 105),      # "TOTAL DETAIL RECORDS: "
        "detail_record_count": pos(106, 115),      # 10 digits
        "refresh_or_update": pos(119, 127),        # "REFRESHED"/"UPDATED "
        "end_marker": pos(750, 750),               # "Z"
    },  # :contentReference[oaicite:1]{index=1}

    # -------------------------
    # MANDATORY / COMMON RECORDS
    # -------------------------
    "A": {  # Record A: Main Account Information
        "transaction_code": pos(1, 2),            # "CI"
        "record_indicator": pos(3, 3),            # "A"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        # USA PATRIOT Act / KYC highlights
        "pep_indicator": pos(671, 671),
        "private_banking_indicator": pos(672, 672),
        "foreign_bank_indicator": pos(673, 673),
        "initial_source_of_funds": pos(674, 677),
        "patriot_exempt_reason": pos(678, 681),
        "primary_country_citizenship": pos(682, 683),
        "country_of_residence": pos(684, 685),
        "birth_date_ccyymmdd": pos(686, 693),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:2]{index=2}

    "B": {  # Record B: Main Account Information (Tax/KYC)
        "transaction_code": pos(1, 2),            # "CI"
        "record_indicator": pos(3, 3),            # "B"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        # Tax ID & W-8/W-9
        "tax_id_type": pos(41, 41),
        "tax_id_number": pos(42, 50),
        "tax_id_applied_date": pos(51, 58),       # CCYYMMDD
        "w8w9_indicator": pos(59, 60),            # "W8"/"W9"/" "
        "w8w9_date_signed": pos(61, 68),          # CCYYMMDD
        "w8w9_effective_date": pos(69, 76),       # CCYYMMDD
        "w8w9_document_type": pos(77, 80),        # Appendix Q
        "tax_status": pos(81, 81),
        # (Plenty more in B; add as needed)
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:3]{index=3}

    "C": {  # Record C: Address 1 & 2
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "C"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        # Address (1)
        "addr1_txn_code": pos(41, 41),
        "addr1_special_handling": pos(42, 42),
        "addr1_delivery_id": pos(43, 43),
        "addr1_attention_prefix": pos(44, 47),
        "addr1_attention_detail": pos(48, 75),
        "addr1_line1": pos(76, 107),
        "addr1_line2": pos(108, 139),
        "addr1_line3": pos(140, 171),
        "addr1_line4": pos(172, 203),
        "addr1_city": pos(204, 218),
        "addr1_state": pos(219, 220),
        "addr1_zip": pos(221, 235),
        "addr1_non_us_city": pos(204, 235),       # alternate mapping
        "addr1_country_code": pos(236, 237),
        # Address (2)
        "addr2_txn_code": pos(338, 338),
        "addr2_special_handling": pos(339, 339),
        "addr2_delivery_id": pos(340, 340),
        "addr2_attention_prefix": pos(341, 344),
        "addr2_attention_detail": pos(345, 372),
        "addr2_line1": pos(373, 404),
        "addr2_line2": pos(405, 436),
        "addr2_line3": pos(437, 468),
        "addr2_line4": pos(469, 500),
        "addr2_city": pos(501, 515),
        "addr2_state": pos(516, 517),
        "addr2_zip": pos(518, 532),
        "addr2_non_us_city": pos(501, 532),
        "addr2_country_code": pos(533, 534),
        "addr2_set_as_mailing": pos(535, 535),
        "addr2_non_us_postal": pos(536, 550),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:4]{index=4}

    "D": {  # Record D: Address 3 & 4
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "D"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        # Address (3)
        "addr3_txn_code": pos(41, 41),
        "addr3_special_handling": pos(42, 42),
        "addr3_delivery_id": pos(43, 43),
        "addr3_attention_prefix": pos(44, 47),
        "addr3_attention_detail": pos(48, 75),
        "addr3_line1": pos(76, 107),
        "addr3_line2": pos(108, 139),
        "addr3_line3": pos(140, 171),
        "addr3_line4": pos(172, 203),
        "addr3_city": pos(204, 218),
        "addr3_state": pos(219, 220),
        "addr3_zip": pos(221, 235),
        "addr3_non_us_city": pos(204, 235),
        "addr3_country_code": pos(236, 237),
        "addr3_set_as_mailing": pos(238, 238),
        "addr3_non_us_postal": pos(239, 253),
        # Address (4)
        "addr4_txn_code": pos(338, 338),
        "addr4_special_handling": pos(339, 339),
        "addr4_delivery_id": pos(340, 340),
        "addr4_attention_prefix": pos(341, 344),
        "addr4_attention_detail": pos(345, 372),
        "addr4_line1": pos(373, 404),
        "addr4_line2": pos(405, 436),
        "addr4_line3": pos(437, 468),
        "addr4_line4": pos(469, 500),
        "addr4_city": pos(501, 515),
        "addr4_state": pos(516, 517),
        "addr4_zip": pos(518, 532),
        "addr4_non_us_city": pos(501, 532),
        "addr4_country_code": pos(533, 534),
        "addr4_set_as_mailing": pos(535, 535),
        "addr4_non_us_postal": pos(536, 550),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:5]{index=5}

    "E": {  # Record E: Address 5 & 6
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "E"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        # Address (5)
        "addr5_txn_code": pos(41, 41),
        "addr5_special_handling": pos(42, 42),
        "addr5_delivery_id": pos(43, 43),
        "addr5_attention_prefix": pos(44, 47),
        "addr5_attention_detail": pos(48, 75),
        "addr5_line1": pos(76, 107),
        "addr5_line2": pos(108, 139),
        "addr5_line3": pos(140, 171),
        "addr5_line4": pos(172, 203),
        "addr5_city": pos(204, 218),
        "addr5_state": pos(219, 220),
        "addr5_zip": pos(221, 235),
        "addr5_non_us_city": pos(204, 235),
        "addr5_country_code": pos(236, 237),
        "addr5_set_as_mailing": pos(238, 238),
        "addr5_non_us_postal": pos(239, 253),
        # Address (6)
        "addr6_txn_code": pos(338, 338),
        "addr6_special_handling": pos(339, 339),
        "addr6_delivery_id": pos(340, 340),
        "addr6_attention_prefix": pos(341, 344),
        "addr6_attention_detail": pos(345, 372),
        "addr6_line1": pos(373, 404),
        "addr6_line2": pos(405, 436),
        "addr6_line3": pos(437, 468),
        "addr6_line4": pos(469, 500),
        "addr6_city": pos(501, 515),
        "addr6_state": pos(516, 517),
        "addr6_zip": pos(518, 532),
        "addr6_non_us_city": pos(501, 532),
        "addr6_country_code": pos(533, 534),
        "addr6_set_as_mailing": pos(535, 535),
        "addr6_non_us_postal": pos(536, 550),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:6]{index=6}

    "F": {  # Record F: Address 7 (+Tax production fields)
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "F"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        # Address (7)
        "addr7_txn_code": pos(41, 41),
        "addr7_special_handling": pos(42, 42),
        "addr7_delivery_id": pos(43, 43),
        "addr7_attention_prefix": pos(44, 47),
        "addr7_attention_detail": pos(48, 75),
        "addr7_line1": pos(76, 107),
        "addr7_line2": pos(108, 139),
        "addr7_line3": pos(140, 171),
        "addr7_line4": pos(172, 203),
        "addr7_city": pos(204, 218),
        "addr7_state": pos(219, 220),
        "addr7_zip": pos(221, 235),
        "addr7_non_us_city": pos(204, 235),
        "addr7_country_code": pos(236, 237),
        "addr7_set_as_mailing": pos(238, 238),
        "addr7_non_us_postal": pos(239, 253),
        # Tax servicer / group
        "tax_servicer": pos(338, 341),
        "tax_group_id": pos(342, 353),
        "tax_group_id_status": pos(354, 354),
        "tax_group_description": pos(355, 394),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:7]{index=7}

    "W": {  # Record W: Additional account-level info (KYC phones, email, flags)
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "W"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        "record_txn_code": pos(41, 41),
        # A few key highlights (there are many more telephone slices)
        "non_usd_trading": pos(42, 42),
        "base_currency": pos(43, 45),
        "email": pos(646, 695),
        "external_positions_ind": pos(696, 696),
        "purge_eligible_ind": pos(697, 697),
        "advisory_acct_ind": pos(698, 698),
        "product_profile_code": pos(699, 702),
        "cents_per_share_discount": pos(703, 704),
        "country_of_tax_residency": pos(746, 749),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:8]{index=8}

    "4": {  # Record 4: Account-level KYC/AML
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "4"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        "record_txn_code": pos(41, 41),
        # Tail end AML/limits
        "exempt_4210": pos(728, 728),
        "msfta_received": pos(729, 729),
        "covered_securities_limit": pos(730, 739),
        "account_high_risk": pos(740, 740),
        "mtm_limit": pos(741, 747),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:9]{index=9}

    "5": {  # Record 5: Customer Due Diligence (optional)
        "transaction_code": pos(1, 2),
        "record_indicator": pos(3, 3),            # "5"
        "record_id_seq": pos(4, 11),
        "account_number": pos(12, 20),
        "ibd_number": pos(21, 23),
        "ip_number": pos(25, 28),
        "account_short_name": pos(29, 38),
        "record_txn_code": pos(41, 41),
        "certification_date": pos(42, 49),        # CCYYMMDD
        "certified_by": pos(50, 81),
        "end_marker": pos(750, 750),
    },  # :contentReference[oaicite:10]{index=10}
}