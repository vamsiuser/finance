ACCT_R = {
    "TransactionCode":                  (1, 2),
    "RecordIndicatorValue":             (3, 3),
    "RecordIDSequenceNumber":           (4, 11),
    "AccountNumber":                    (12, 20),
    "IBDNumber":                        (21, 23),
    "Literal01":                        (24, 24),
    "InvestmentProfessionalNumber":     (25, 28),
    "AccountShortName":                 (29, 38),
    "Literal03":                        (39, 40),

    "RetirementAccountTransactionCode": (41, 41),
    "ParticipantMaritalStatus":         (42, 42),
    "SexOfParticipant":                 (43, 43),
    "CustodianCode":                    (44, 47),
    "TypeOfRetirementPlan":             (48, 51),
    "TypeOfRetirementAccount":          (52, 52),
    "RetirementPlanNumber":             (53, 62),
    "SelfDirectedIndicator":            (63, 63),
    "AssetWillIndicator":               (64, 64),

    # DATES
    "BrokerDealerConversionDate":       (65, 72),
    "AdoptionAgreementDate":            (73, 80),
    "DatePlanEstablished":              (81, 88),
    "CustodianDate":                    (89, 96),
    "PlanAmendmentDate":                (97, 104),
    "SpousalConsentDate":               (105, 112),

    "EducationDisabilityIndicator":     (113, 113),
    "DisabilityStartDate":              (114, 121),
    "DateOfDeath":                      (122, 129),

    # RELATED ACCOUNTS
    "RelatedBrokerageAccountNumber1":   (130, 138),
    "RelatedBrokerageAccountNumber2":   (139, 147),
    "RelatedBrokerageAccountNumber3":   (148, 156),

    # EMPLOYER INFORMATION AND ADDRESS
    "EmployerName":                     (157, 188),
    "EmployerTIN":                      (189, 197),
    "TrustAdministrator":               (198, 229),
    "EmployerAddressTransactionCode":   (230, 230),
    "SpecialHandlingIndicator":         (231, 231),
    "AttentionLinePrefix":              (232, 235),
    "EmployerAttentionLineDetail":      (236, 263),
    "EmployerAddressLine1":             (264, 295),
    "EmployerAddressLine2":             (296, 327),
    "EmployerAddressLine3":             (328, 359),
    "EmployerAddressLine4":             (360, 391),
    "City":                             (392, 406),
    "State":                            (407, 408),
    "Zip":                              (409, 423),
    "CountryCode":                      (424, 425),

    "Literal04":                        (426, 525),

    # E-MAIL INFORMATION
    "EmailAddress":                     (526, 575),

    # TELEPHONE NUMBER 1
    "TelephoneTransactionCode1":        (576, 576),
    "USInternationalIndicator1":        (577, 577),
    "TelephoneTypeID1":                 (578, 578),
    "TelephoneNumber1":                 (579, 638),
    "TelephoneExtension1":              (639, 645),

    # TELEPHONE NUMBER 2
    "TelephoneTransactionCode2":        (646, 646),
    "USInternationalIndicator2":        (647, 647),
    "TelephoneTypeID2":                 (648, 648),
    "TelephoneNumber2":                 (649, 708),
    "TelephoneExtension2":              (709, 715),

    "MutualFundIndicator":              (716, 716),
    "Literal05":                        (717, 748),
    "Literal06":                        (749, 749),
    "Literal07":                        (750, 750),
}