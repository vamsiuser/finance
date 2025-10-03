ACCT_C = {
        "TransactionCode":               (1, 2),
        "RecordIndicatorValue":          (3, 3),
        "RecordIDSequenceNumber":        (4, 11),
        "AccountNumber":                 (12, 20),
        "IBDNumber":                     (21, 23),
        "Literal01":                     (24, 24),
        "InvestmentProfessionalNumber":  (25, 28),
        "AccountShortName":              (29, 38),
        "Literal03":                     (39, 40),

        # ACCOUNT ADDRESS 1
        "AddressTransactionCode1":       (41, 41),
        "SpecialHandlingIndicator1":     (42, 42),
        "DeliveryIdentifier1":           (43, 43),
        "AttentionLinePrefix1":          (44, 47),
        "AttentionLineDetail1":          (48, 75),
        "Address1Line1":                 (76, 107),
        "Address1Line2":                 (108, 139),
        "Address1Line3":                 (140, 171),
        "Address1Line4":                 (172, 203),
        "City1":                         (204, 218),
        "State1":                        (219, 220),
        "Zip1":                          (221, 235),
        "NonUSOrCanadaCity1":            (204, 235),
        "CountryCode1":                  (236, 237),
        "Literal04":                     (238, 238),
        "MostRecentMailReturnDate":      (239, 246), # CCYYMMDD
        "MostRecentReturnComment":       (247, 267),
        "MostRecentReturnMailType":      (268, 271),
        "SecondMostRecentMailReturnDate":(272, 279),
        "SecondMostRecentReturnComment": (280, 300),
        "SecondMostRecentReturnMailType":(301, 304),
        "ThirdMostRecentMailReturnDate": (305, 312),
        "ThirdMostRecentReturnComment":  (313, 333),
        "ThirdMostRecentReturnMailType": (334, 337),

        # ACCOUNT ADDRESS 2
        "AddressTransactionCode2":       (338, 338),
        "SpecialHandlingIndicator2":     (339, 339),
        "DeliveryIdentifier2":           (340, 340),
        "AttentionLinePrefix2":          (341, 344),
        "AttentionLineDetail2":          (345, 372),
        "Address2Line1":                 (373, 404),
        "Address2Line2":                 (405, 436),
        "Address2Line3":                 (437, 468),
        "Address2Line4":                 (469, 500),
        "City2":                         (501, 515),
        "State2":                        (516, 517),
        "Zip2":                          (518, 532),
        "NonUSOrCanadaCity2":            (501, 532),
        "CountryCode2":                  (533, 534),
        "AccountDescription":            (535, 566),
        "MailingAddressIndicator":       (567, 567),
        # "NON-US/CANADA ZIP/POSTAL CODE (2)" : (568, 582), # not in database
        "Literal05":                     (583, 600),
        "PrincipalBillingAllocationPercentage": (601, 618),  # numeric
        #NON-US/CANADA ZIP/POSTAL CODE (1) : (619, 633), # not in database
        "Literal06":                     (634, 634),

        # SEASONAL ADDRESS DATES
        "SeasonalAddressIdentifier1":    (635, 635),
        "FromDate1":                     (636, 643),
        "ToDate1":                       (644, 651),
        "SeasonalAddressIdentifier2":    (669, 669),
        "FromDate2":                     (670, 677),
        "ToDate2":                       (678, 685),
        # "SeasonalAddressIdentifier3":    (),
        # "FromDate3":                     (),
        # "ToDate3":                       (),

        # COST BASIS ACCOUNTING FIELDS
        "CostBasisAccountingSystem":     (686, 689),
        "DispositionMethodForMutualFunds": (690, 691),
        "DispositionMethodForOtherSecurityTypes": (692, 693),
        "DispositionMethodForStocksInDRIPS": (694, 695),
        
        #BOND ELECTION REQUEST FOR COST BASIS REPORTING
        "TreatAllInterestAsOID":         (696, 696),
        "AmortizeTaxablePremiumBonds":   (697, 697),
        "AccrueMarketDiscountBasedOn":   (698, 698),
        "IncludeMarketDiscountInIncomeAnnually": (699, 699),
        "Literal07":                     (700, 705),
        "Literal08":                     (706, 747),
        "Literal09":                     (748, 749),
        "Literal10":                     (750, 750), #X
    }