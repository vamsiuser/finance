ACCT_E = {
        "TransactionCode":               (1, 2),
        "RecordIndicatorValue":          (3, 3),     # 'E'
        "RecordIDSequenceNumber":        (4, 11),
        "AccountNumber":                 (12, 20),
        "IBDNumber":                     (21, 23),
        "Literal01":                     (24, 24),
        "InvestmentProfessionalNumber":  (25, 28),
        "AccountShortName":              (29, 38),
        "Literal03":                     (39, 40),

        # ACCOUNT ADDRESS 5
        "AddressTransactionCode5":       (41, 41),
        "SpecialHandlingIndicator5":     (42, 42),
        "DeliveryIdentifier5":           (43, 43),
        "AttentionLinePrefix5":          (44, 47),
        "AttentionLineDetail5":          (48, 75),
        "Address5Line1":                 (76, 107),
        "Address5Line2":                 (108, 139),
        "Address5Line3":                 (140, 171),
        "Address5Line4":                 (172, 203),
        "City5":                         (204, 218),
        "State5":                        (219, 220),
        "Zip5":                          (221, 235),
        "NonUSOrCanadaCity5":            (204, 235),
        "CountryCode5":                  (236, 237),
        "MailingAddressIndicator5":      (238, 238),
        # NON-US/CANADA ZIP/POSTAL CODE (5); (239, 253), # not in database
        "Literal04":                     (254, 337),

        # ACCOUNT ADDRESS 6
        "AddressTransactionCode6":       (338, 338),
        "SpecialHandlingIndicator6":     (339, 339),
        "DeliveryIdentifier6":           (340, 340),
        "AttentionLinePrefix6":          (341, 344),
        "AttentionLineDetail6":          (345, 372),
        "Address6Line1":                 (373, 404),
        "Address6Line2":                 (405, 436),
        "Address6Line3":                 (437, 468),
        "Address6Line4":                 (469, 500),
        "City6":                         (501, 515),
        "State6":                        (516, 517),
        "Zip6":                          (518, 532),
        "NonUSOrCanadaCity6":            (501, 532),
        "CountryCode6":                  (533, 534),
        "MailingAddressIndicator6":      (535, 535),
        # NON-US/CANADA ZIP/POSTAL CODE (6); (536, 550), # not in database
        "Literal05":                     (551, 749),
        "Literal06":                     (750, 750), #X
    }