ACCT_D = {
        "TransactionCode":               (1, 2),
        "RecordIndicatorValue":          (3, 3),     # 'D'
        "RecordIDSequenceNumber":        (4, 11),
        "AccountNumber":                 (12, 20),
        "IBDNumber":                     (21, 23),
        "Literal01":                     (24, 24),
        "InvestmentProfessionalNumber":  (25, 28),
        "AccountShortName":              (29, 38),
        "Literal03":                     (39, 40),

        # ACCOUNT ADDRESS 3
        "AddressTransactionCode3":       (41, 41),
        "SpecialHandlingIndicator3":     (42, 42),
        "DeliveryIdentifier3":           (43, 43),
        "AttentionLinePrefix3":          (44, 47),
        "AttentionLineDetail3":          (48, 75),
        "Address3Line1":                 (76, 107),
        "Address3Line2":                 (108, 139),
        "Address3Line3":                 (140, 171),
        "Address3Line4":                 (172, 203),
        "City3":                         (204, 218),
        "State3":                        (219, 220),
        "Zip3":                          (221, 235),
        "NonUSOrCanadaCity3":            (204, 235),
        "CountryCode3":                  (236, 237),
        "MailingAddressIndicator3":      (238, 238),
        #NON-US/CANADA ZIP/POSTAL CODE (3); (239, 253), # not in database
        "Literal04":                     (254, 337),

        # ACCOUNT ADDRESS 4
        "AddressTransactionCode4":       (338, 338),
        "SpecialHandlingIndicator4":     (339, 339),
        "DeliveryIdentifier4":           (340, 340),
        "AttentionLinePrefix4":          (341, 344),
        "AttentionLineDetail4":          (345, 372),
        "Address4Line1":                 (373, 404),
        "Address4Line2":                 (405, 436),
        "Address4Line3":                 (437, 468),
        "Address4Line4":                 (469, 500),
        "City4":                         (501, 515),
        "State4":                        (516, 517),
        "Zip4":                          (518, 532),
        "NonUSOrCanadaCity4":            (501, 532),
        "CountryCode4":                  (533, 534),
        "MailingAddressIndicator4":      (535, 535),
        # NON-US/CANADA ZIP/POSTAL CODE (4); (536, 550), # not in database
        "Literal05":                     (551, 749),
        "Literal06":                     (750, 750), #X
    }