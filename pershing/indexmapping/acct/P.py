ACCT_P = {
    "TransactionCode":                  (1, 2),
    "RecordIndicatorValue":             (3, 3),
    "RecordIDSequenceNumber":           (4, 11),
    "AccountNumber":                    (12, 20),
    "IBDNumber":                        (21, 23),
    "Literal01":                        (24, 24),
    "InvestmentProfessionalNumber":     (25, 28),
    "AccountShortName":                 (29, 38),
    "Literal03":                        (39, 40),

    # GENERAL INFORMATION
    "ParentID":                         (41, 46),
    "InstitutionID":                    (47, 54),
    "InstitutionAccountNumber":         (55, 70),
    "AlertAcronym":                     (71, 78),
    "AlertAccessCode":                  (79, 90),
    "ConfirmationOption":               (91, 91),
    "BirthDate":                        (92, 99),
    "Literal04":                        (100, 103),
    "CountryOfCitizenship":             (104, 105),

    # DTC INSTRUCTIONS
    "DTCTransactionCode":               (106, 106),
    "LocationProductCode":              (107, 110),
    "InstitutionNumber":                (111, 118),
    "InstitutionName":                  (119, 158),
    "AgentNumber":                      (159, 166),
    "AgentName":                        (167, 206),
    "AgentInternalNumber":              (207, 222),
    "AgentInternalName":                (223, 272),
    "ClearingAgentNumber":              (273, 280),
    "ClearingAgentName":                (281, 315),

    "FirstDTCIpNumber":                 (316, 323),
    "FirstIPAccountNumber":             (324, 346),
    "SecondDTCIpNumber":                (347, 354),
    "SecondIPAccountNumber":            (355, 377),

    # FED/UST/GNMA/ALL OTHER INSTRUCTIONS
    "FedTransactionCode":               (378, 378),
    "FedLocationProductCode":           (379, 382),
    "ABANumber":                        (383, 391),
    "InternalAccountNumber":            (392, 431),
    "FederalWireBankName":              (432, 481),

    # EUROCLEAR INSTRUCTIONS
    "EUROTransactionCode":              (482, 482),
    "EUROLocationProductCode":          (483, 486),
    "EUROClearNumber":                  (487, 494),
    "EUROClearAccountNumber":           (495, 509),

    # CEDEL INSTRUCTIONS
    "CEDTransactionCode":               (510, 510),
    "CEDLocationProductCode":           (511, 514),
    "CEDELNumber":                      (515, 522),
    "CEDELAccountNumber":               (523, 537),

    # PHYSICAL INSTRUCTIONS
    "PhysicalTransactionCode":          (538, 538),
    "PhysicalLocationProductCode":      (539, 542),
    "AccountNumberForPhysicalDelivery": (543, 557),

    # OTHER INSTRUCTIONS
    "OtherInstructions1":               (558, 589),
    "OtherInstructions2":               (590, 621),
    "OtherInstructions3":               (622, 653),
    "OtherInstructions4":               (654, 685),
    "OtherInstructions5":               (686, 717),
    "OtherInstructions6":               (718, 749),

    "Literal05":                        (750, 750),
}