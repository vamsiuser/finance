table_index_a = {
    "TransactionCode":               (1, 2),
    "RecordIndicatorValue":          (3, 3),
    "RecordIDSequenceNumber":        (4, 11),
    "AccountNumber":                 (12, 20),
    "IBDNumber":                     (21, 23),
    "Literal01":                     (24, 24),
    "InvestmentProfessionalNumber":  (25, 28),
    "AccountShortName":              (29, 38),

    # early flags / registration block
    "Literal03":                     (39, 40),
    "TransactionType":               (41, 41),
    "AutoTitledAccount":             (42, 42),
    "AccountTypeCode":               (43, 43),
    "RegistrationType":              (44, 47),
    "NumberedAcctIndicator":         (48, 48),
    "NumberOfAccountTitleLines":     (49, 49),
    "AccountRegistrationLine1":      (50, 81),
    "AccountRegistrationLine2":      (82, 113),
    "AccountRegistrationLine3":      (114, 145),
    "AccountRegistrationLine4":      (146, 177),
    "AccountRegistrationLine5":      (178, 209),
    "AccountRegistrationLine6":      (210, 241),
    "USResidentIndicator":           (242, 242),
    "MarriedIndicator":              (243, 243),
    "TenancyState":                  (244, 245),
    "JointTenancyClause":            (246, 249),
    "AgreementExecDate":             (250, 257),   # CCYYMMDD (or convert from MM/DD/CCYY if your feed uses that)
    "NumberOfTenants":               (258, 259),

    # gift / trust / plan section – fill from spec
    # "Literal04":                     (...),
    # "StateGiftGiven":                (...),
    # "DateGiftGiven":                 (...),
    # "AgeToTerminate":                (...),
    # "MinorsBirthDate":               (...),
    # "MannerOfGift":                  (...),
    # "TypeOfTrust":                   (...),
    # "DateTrustEstablished":          (...),
    # "AmmendDate":                    (...),
    # "TrusteeIndependentAction":      (...),
    # "TrusteeNaturalPersonsIndicator":(...),
    # "BeneficiaryOfTrustNaturalPersons": (...),
    # "TrustIsDulyOrganizedIndicator": (...),
    # "PlanEstablishedDate":           (...),
    # "PlanAmendmentDate":             (...),

    # account status / dates – fill from spec
    # "Literal05":                     (...),
    # "DateAccountOpened":             (...),
    # "DateAccountInformationUpdated": (...),
    # "AccountStatusIndicator":        (...),
    # "PendingClosedDate":             (...),
    # "DateAccountClosed":             (...),
    # "ClosingNoticedDate":            (...),
    # "AccountReactivationDate":       (...),
    # "DateAccountReOpened":           (...),

    # instructions & counts – (you set Proceeds=559; keep if confirmed, else fill later)
    "Proceeds":                      (559, 559),
    # "TransferInstructions":          (...),
    # "IncomeInstructions":            (...),
    # "NumberOfConfirms":              (...),
    # "NumberOfStatements":            (...),
    # "InvestmentObjectiveTransacCode":(...),
    # "Comments":                      (...),

    # employer – fill from spec
    # "EmployerShortName":             (...),
    # "EmployerCusip":                 (...),
    # "EmployerSymbol":                (...),

    # margin/options flags – fill from spec
    # "MarginPrivilegesRevoked":       (...),
    # "StatementReviewDate":           (...),
    # "MarginPapersOnFile":            (...),
    # "OptionsPapersOnFile":           (...),
    # "Literal06":                     (...),
    # "GoodFaithMargin":               (...),
    # "InvProflDiscretionGranted":     (...),
    # "InvAdvisorDiscretionGranted":   (...),
    # "ThirdPartyDiscretionGranted":   (...),
    # "ThirdPartyName":                (...),
    # "RiskFactorCode":                (...),
    # "InvestmentObjectiveCode":       (...),

    # option levels & limits – fill from spec
    # "OptionEquities":                (...),
    # "OptionIndex":                   (...),
    # "OptionDebt":                    (...),
    # "OptionCurrency":                (...),
    # "OptionLevel1":                  (...),
    # "OptionLevel2":                  (...),
    # "OptionLevel3":                  (...),
    # "OptionLevel4":                  (...),
    # "OptionCallLimits":              (...),
    # "OptionPytLimits":               (...),
    # "OptionTotalLimitsPutsAndCalls": (...),
    # "NonUSDollarTrading":            (...),
    # "Literal07":                     (...),
    # "NonCustomerIndicator":          (...),

    # fees / routing – fill from spec
    # "ThirdPartyFeeIndicator":        (...),
    # "ThirdPartyFeeApprovalDate":     (...),
    # "IntermediaryAccountIndicator":  (...),
    # "CommisionSchedule":             (...),
    # "GroupIndex":                    (...),
    # "MoneyManagerId":                (...),
    # "MoneyManagerObjectiveId":       (...),
    # "DtcIdConfNumerForNonCODAcct":   (...),
    # "CapsMasterMneumonic":           (...),
    # "EmployeeId":                    (...),
    # "PrimeBrokerFreeFundInd":        (...),
    # "FeeBasedAccountIndicator":      (...),
    # "BillingType":                   (...),
    # "FeeBasedTerminationDate":       (...),
    # "EquifaxCreditCheckIndicator":   (...),

    # plans – fill from spec
    # "SelfDirected401kPlanName":      (...),
    # "SelfDirected401kAcctType":      (...),
    # "PlanType":                      (...),
    # "PlanNumber":                    (...),

    # discounts / signatures – fill from spec
    # "EmployeeRelativeIndicator":     (...),
    # "CommissionPercentDiscount":     (...),
    # "MutualFundFeesBlockingIndicator": (...),
    # "NameOfInvestProfessionalWhoSigned": (...),
    # "DateInvestmentProfessionalSigned":   (...),
    # "NameOfPrincipalWhoSigned":      (...),
    # "DatePrincipalSigned":           (...),

    # ---- PATRIOT / KYC tail (fixed & corrected) ----
    "PEPIndicator":                  (671, 671),
    "PrivateBankingAcctIndicator":   (672, 672),
    "ForeignBankAcctIndicator":      (673, 673),
    "InitialSourceOfFunds":          (674, 677),
    "USAPatriotActExemptReason":     (678, 681),
    "PrimaryCountryOfCitizenship":   (682, 683),
    "CountryOfResidence":            (684, 685),
    "BirthDate":                     (686, 693),   # CCYYMMDD

    # trailing internal / fulfillment – fill from spec
    # "AgeBasedFundRollExepmtIndicator": (...),
    # "MoneyFundReformRetail":        (...),
    # "TrustContactStatus":           (...),
    # "RegulatoryAccountTypeCategory":(...),
    # "AccountManagedByTrustCoIndicator": (...),
    # "VotingAuthority":              (...),
    # "IntUsePrimeBrokerCode":        (...),
    # "IntUsePayoutCode":             (...),
    # "IntUseTraderNumber":           (...),
    # "IntUseProductCode":            (...),
    # "IntUseCustomerType":           (...),
    # "IntUseAccountPlanType":        (...),
    # "IntUsePromotionType":          (...),
    # "IntUseInvObj1":                (...),
    # "IntUseInvObj2":                (...),
    # "IntUseInvObj3":                (...),
    # "FulfillmentMethod":            (...),
    # "CreditInterestIndicator":      (...),
    # "AmaIndicator":                 (...),
    # "Literal08":                    (...),
    # "Literal09":                    (...),
}

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
    return (start, end_inclusive)

EXTRA_LAYOUT = {
    
    "HEADER": {
        "Literal01": (1, 18),
        "FileDescription": (19, 36),
        "Literal02": (38, 46),
        "DateOfData": (47, 56),
        "Literal03": (58, 67),
        "RemoteID": (68, 71),
        "Literal04": (73, 85),
        "RunDate": (86, 95),
        "RunTime": (97, 104),   
        "FileModificationType": (118, 127),
        "Literal08": (750, 750),
        "RefreshOrUpdate": (118, 127),
        "EndMarker": (749, 750),
    },

    "TRAILER": {
        "Literal01":              (1, 18),    # "EOF      PERSHING"
        "FileDescription":        (19, 36),
        "Literal02":              (37, 46),
        "DateOfData":             (47, 56),   # MM/DD/CCYY
        "Literal03":              (57, 67),
        "RemoteID":               (68, 71),
        "Literal04":              (72, 83),   # " ENDS HERE. "
        "Literal05":              (84, 105),  # "TOTAL DETAIL RECORDS:"
        "DetailRecordCount":      (106, 115),
        "Literal06":              (116, 118),
        "FileModificationType":   (119, 127),
        "Literal07":              (128, 749),
        "Literal08":              (750, 750),
    },
    "4": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # '4'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "RecordTransactionCode":         pos(41, 41),
        # … suitability block …

        # Tail AML/limits (confirmed tail)
        "4210ExemptStatus":              pos(728, 728),
        "MSFTAReceived":                 pos(729, 729),
        "CoveredSecuritiesLimit":        pos(730, 739),
        "AccountIsHighRisk":             pos(740, 740),
        "MTMLimit":                      pos(741, 747),
        # 748–750 padding / marker
    },

    # =========================
    # RECORD 5 — CDD
    # =========================
    "5": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # '5'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal02":                     pos(39, 40),
        "RecordTransactionCode":         pos(41, 41),
        "CertificationDate":             pos(42, 49),   # CCYYMMDD
        "FinCENCertificationFormCertifiedBy": pos(50, 81),
        "PositionHeldByFinCENCertifier": pos(82, 121),
        # … (add remaining flags/indicators per your table)
    },

    # =========================
    # RECORD 7 — Trust/Bank Custody + IDs
    # =========================
    "7": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # '7'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "RecordTransactionCode":         pos(41, 41),
        "SequenceNumber":                pos(42, 44),
        "AccountHolderType":             pos(45, 47),
        "AccountHolderParticipantRole":  pos(48, 51),
        "TypeOfTrust":                   pos(52, 52),
        "DateTrustEstablished":          pos(53, 60),   # CCYYMMDD
        "TrustAmendmentDate":            pos(61, 68),   # CCYYMMDD
        "TrusteeIndependentAction":      pos(69, 69),
        # … (add remaining trust perms/indicators, LEI, etc.)
    },
    "A": table_index_a,

    "B": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'B'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "TaxIDType":                     pos(41, 41),
        "TaxIDNumber":                   pos(42, 50),
        "DateTaxIDAppliedFor":           pos(51, 58),   # CCYYMMDD
        "W8W9Indicator":                 pos(59, 60),
        "W8W9DateSigned":                pos(61, 68),   # CCYYMMDD
        "W8W9EffectiveDate":             pos(69, 76),   # CCYYMMDD
        "W8W9DocumentType":              pos(77, 80),
        "TaxStatus":                     pos(81, 81),

        # Notices / statuses / etc. → fill with your spec ranges
        # "BNoticeReasonCode": pos(...), "FirstBNoticeStatus": pos(...),
        # "DateFirstBNoticeStatusIssued": pos(...), "Literal04": pos(...),
        # "DateFirstBNoticeStatusSatisfied": pos(...), "SecondBNoticeStatus": pos(...),
        # "DateSecondBNoticeStatusIssued": pos(...), "Literal05": pos(...),
        # "DateSecondBNoticeStatusSatisfied": pos(...), "CNoticeStatus": pos(...),
        # "DateCNoticeStatusIssued": pos(...), "DateCNoticeStatusSatisfied": pos(...),
        # "OldAccountNumber": pos(...), "OriginalAccountOpenDate": pos(...),
        # "UnidentifiedLargeTraderID": pos(...), "Literal06": pos(...),
        # "LargeTraderTypeCode": pos(...), "LargeTraderTypeLastChangeDate": pos(...),
        # "Literal07": pos(...), "Literal08": pos(...), "InitialSourceOfFunds": pos(...),
        # "FinanceAway": pos(...), "AccountFundingDate": pos(...), "Literal09": pos(...),
        # "StatementCurrencyCode": pos(...), "FutureStatementCurrencyCode": pos(...),
        # "FutureStatementCurrencyDate": pos(...),

        # routing, digital, investment professionals, alerts, bank links, sweep, etc. …
        # (add ranges as you confirm them from your PDF)
    },

    "C": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'C'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # Address (1)
        "AddressTransactionCode1":       pos(41, 41),
        "SpecialHandlingIndicator1":     pos(42, 42),
        "DeliveryIdentifier1":           pos(43, 43),
        "AttentionLinePrefix1":          pos(44, 47),
        "AttentionLineDetail1":          pos(48, 75),
        "Address1Line1":                 pos(76, 107),
        "Address1Line2":                 pos(108, 139),
        "Address1Line3":                 pos(140, 171),
        "Address1Line4":                 pos(172, 203),
        "City1":                         pos(204, 218),
        "State1":                        pos(219, 220),
        "Zip1":                          pos(221, 235),
        "NonUSOrCanadaCity1":            pos(204, 235),
        "CountryCode1":                  pos(236, 237),

        "Literal04":                     pos(238, 238),
        "MostRecentMailReturnDate":      pos(239, 246), # CCYYMMDD
        "MostRecentReturnComment":       pos(247, 267),
        "MostRecentReturnMailType":      pos(268, 271),
        "SecondMostRecentMailReturnDate":pos(272, 279),
        "SecondMostRecentReturnComment": pos(280, 300),
        "SecondMostRecentReturnMailType":pos(301, 304),
        "ThirdMostRecentMailReturnDate": pos(305, 312),
        "ThirdMostRecentReturnComment":  pos(313, 333),
        "ThirdMostRecentReturnMailType": pos(334, 337),

        # Address (2)
        "AddressTransactionCode2":       pos(338, 338),
        "SpecialHandlingIndicator2":     pos(339, 339),
        "DeliveryIdentifier2":           pos(340, 340),
        "AttentionLinePrefix2":          pos(341, 344),
        "AttentionLineDetail2":          pos(345, 372),
        "Address2Line1":                 pos(373, 404),
        "Address2Line2":                 pos(405, 436),
        "Address2Line3":                 pos(437, 468),
        "Address2Line4":                 pos(469, 500),
        "City2":                         pos(501, 515),
        "State2":                        pos(516, 517),
        "Zip2":                          pos(518, 532),
        "NonUSOrCanadaCity2":            pos(501, 532),
        "CountryCode2":                  pos(533, 534),

        "AccountDescription":            pos(535, 566),
        "MailingAddressIndicator":       pos(567, 567),

        "Literal05":                     pos(568, 600),
        "PrincipalBillingAllocationPercentage": pos(601, 606),  # numeric
        "Literal06":                     pos(607, 622),

        # Seasonal windows (approx slots; confirm):
        "SeasonalAddressIdentifier1":    pos(623, 623),
        "FromDate1":                     pos(624, 631),
        "ToDate1":                       pos(632, 639),
        "SeasonalAddressIdentifier2":    pos(640, 640),
        "FromDate2":                     pos(641, 648),
        "ToDate2":                       pos(649, 656),
        "SeasonalAddressIdentifier3":    pos(657, 657),
        "FromDate3":                     pos(658, 665),
        "ToDate3":                       pos(666, 673),

        # Cost basis / tax opts (tail)
        "CostBasisAccountingSystem":     pos(674, 677),
        "DispositionMethodForMutualFunds": pos(678, 679),
        "DispositionMethodForOtherSecurityTypes": pos(680, 681),
        "DispositionMethodForStocksInDRIPS": pos(682, 683),
        "TreatAllInterestAsOID":         pos(684, 684),
        "AmortizeTaxablePremiumBonds":   pos(685, 685),
        "AccrueMarketDiscountBasedOn":   pos(686, 686),
        "IncludeMarketDiscountInIncomeAnnually": pos(687, 687),

        "Literal07":                     pos(688, 693),
        "Literal08":                     pos(694, 735),
        "Literal09":                     pos(736, 737),
        "Literal10":                     pos(738, 738),
    },
    "D": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'D'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # Address (3)
        "AddressTransactionCode3":       pos(41, 41),
        "SpecialHandlingIndicator3":     pos(42, 42),
        "DeliveryIdentifier3":           pos(43, 43),
        "AttentionLinePrefix3":          pos(44, 47),
        "AttentionLineDetail3":          pos(48, 75),
        "Address3Line1":                 pos(76, 107),
        "Address3Line2":                 pos(108, 139),
        "Address3Line3":                 pos(140, 171),
        "Address3Line4":                 pos(172, 203),
        "City3":                         pos(204, 218),
        "State3":                        pos(219, 220),
        "Zip3":                          pos(221, 235),
        "NonUSOrCanadaCity3":            pos(204, 235),
        "CountryCode3":                  pos(236, 237),
        "MailingAddressIndicator3":      pos(238, 238),

        "Literal04":                     pos(239, 337),

        # Address (4)
        "AddressTransactionCode4":       pos(338, 338),
        "SpecialHandlingIndicator4":     pos(339, 339),
        "DeliveryIdentifier4":           pos(340, 340),
        "AttentionLinePrefix4":          pos(341, 344),
        "AttentionLineDetail4":          pos(345, 372),
        "Address4Line1":                 pos(373, 404),
        "Address4Line2":                 pos(405, 436),
        "Address4Line3":                 pos(437, 468),
        "Address4Line4":                 pos(469, 500),
        "City4":                         pos(501, 515),
        "State4":                        pos(516, 517),
        "Zip4":                          pos(518, 532),
        "NonUSOrCanadaCity4":            pos(501, 532),
        "CountryCode4":                  pos(533, 534),
        "MailingAddressIndicator4":      pos(535, 535),

        "Literal05":                     pos(536, 749),
        "Literal06":                     pos(750, 750),
    },

    # =========================
    # RECORD E — Address 5 & 6
    # =========================
    "E": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'E'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # Address (5)
        "AddressTransactionCode5":       pos(41, 41),
        "SpecialHandlingIndicator5":     pos(42, 42),
        "DeliveryIdentifier5":           pos(43, 43),
        "AttentionLinePrefix5":          pos(44, 47),
        "AttentionLineDetail5":          pos(48, 75),
        "Address5Line1":                 pos(76, 107),
        "Address5Line2":                 pos(108, 139),
        "Address5Line3":                 pos(140, 171),
        "Address5Line4":                 pos(172, 203),
        "City5":                         pos(204, 218),
        "State5":                        pos(219, 220),
        "Zip5":                          pos(221, 235),
        "NonUSOrCanadaCity5":            pos(204, 235),
        "CountryCode5":                  pos(236, 237),
        "MailingAddressIndicator5":      pos(238, 238),

        "Literal04":                     pos(239, 337),

        # Address (6)
        "AddressTransactionCode6":       pos(338, 338),
        "SpecialHandlingIndicator6":     pos(339, 339),
        "DeliveryIdentifier6":           pos(340, 340),
        "AttentionLinePrefix6":          pos(341, 344),
        "AttentionLineDetail6":          pos(345, 372),
        "Address6Line1":                 pos(373, 404),
        "Address6Line2":                 pos(405, 436),
        "Address6Line3":                 pos(437, 468),
        "Address6Line4":                 pos(469, 500),
        "City6":                         pos(501, 515),
        "State6":                        pos(516, 517),
        "Zip6":                          pos(518, 532),
        "NonUSOrCanadaCity6":            pos(501, 532),
        "CountryCode6":                  pos(533, 534),
        "MailingAddressIndicator6":      pos(535, 535),

        "Literal05":                     pos(536, 749),
        "Literal06":                     pos(750, 750),
    },

    # =========================
    # RECORD F — Address 7 + tax-servicer
    # =========================
    "F": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'F'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "AddressTransactionCode7":       pos(41, 41),
        "SpecialHandlingIndicator7":     pos(42, 42),
        "DeliveryIdentifier7":           pos(43, 43),
        "AttentionLinePrefix7":          pos(44, 47),
        "AttentionLineDetail7":          pos(48, 75),
        "Address7Line1":                 pos(76, 107),
        "Address7Line2":                 pos(108, 139),
        "Address7Line3":                 pos(140, 171),
        "Address7Line4":                 pos(172, 203),
        "City7":                         pos(204, 218),
        "State7":                        pos(219, 220),
        "Zip7":                          pos(221, 235),
        "NonUSOrCanadaCity7":            pos(204, 235),
        "CountryCode7":                  pos(236, 237),
        "MailingAddressIndicator7":      pos(238, 238),

        "Literal04":                     pos(239, 337),

        # Tax servicer group (typical slots; confirm with spec)
        "TaxServicer":                   pos(338, 341),
        "TaxGroupID":                    pos(342, 353),
        "TaxGroupIDStatus":              pos(354, 354),
        "TaxGroupDescription":           pos(355, 394),

        "Literal05":                     pos(395, 749),
        # "Literal05"/tail may be longer; adjust if needed
    },

    # =========================
    # RECORD 4 — KYC/AML tail
    # =========================

    # =========================
    # RECORD G — Participant core + addresses
    # =========================
    "G": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'G'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "AccountHolderParticipantTransactionCode": pos(41, 41),
        "SequenceNumber":                pos(42, 44),
        "AccountHolderType":             pos(45, 47),
        "AccountHolderParticipantRole1": pos(48, 51),
        "AccountHolderParticipantNameType1": pos(52, 52),
        "AccountHolderParticipantSuffix1": pos(53, 84),
        "AccountHolderParticipantFirstName1": pos(85, 116),
        "AccountHolderParticipantMiddleName1": pos(117, 148),
        "AccountHolderParticipantLastName1": pos(149, 180),

        # Address block 1
        "DeliveryIdentifier1":           pos(181, 181),
        "SpecialHandlingIndicator1":     pos(182, 182),
        "AttentionLinePrefix1":          pos(183, 186),
        "AttentionLineDetail1":          pos(187, 214),
        "StreetAddress1Line1":           pos(215, 246),
        "StreetAddress1Line2":           pos(247, 278),
        "StreetAddress1Line3":           pos(279, 310),
        "StreetAddress1Line4":           pos(311, 342),
        "City1":                         pos(343, 357),
        "State1":                        pos(358, 359),
        "Zip1":                          pos(360, 374),
        "NonUSOrCanadaCity1":            pos(343, 374),
        "CountryCode1":                  pos(375, 376),

        "Literal4":                      pos(377, 378),

        # Address block 2
        "DeliveryIdentifier2":           pos(379, 379),
        "SpecialHandlingIndicator2":     pos(380, 380),
        "AttentionLinePrefix2":          pos(381, 384),
        "AttentionLineDetail2":          pos(385, 412),
        "StreetAddress2Line1":           pos(413, 444),
        "StreetAddress2Line2":           pos(445, 476),
        "StreetAddress2Line3":           pos(477, 508),
        "StreetAddress2Line4":           pos(509, 540),
        "City2":                         pos(541, 555),
        "State2":                        pos(556, 557),
        "Zip2":                          pos(558, 572),
        "NonUSOrCanadaCity2":            pos(541, 572),
        "CountryCode2":                  pos(573, 574),

        "Literal5":                      pos(575, 576),

        # core participant attributes (confirm/extend with spec)
        "NaturalNonNaturalIndicator":    pos(577, 577),
        "ConfirmationReceiptIndicator":  pos(578, 578),
        "StatementReceiptIndicator":     pos(579, 579),
        "YearsOfInvestExperience":       pos(580, 581),
        "Gender":                        pos(582, 582),
        "ProxyIndicator":                pos(583, 583),
        "AccountHolderParticipantBirthDate": pos(584, 591),  # CCYYMMDD
        "AccountHolderParticipantPrimaryCitizenship": pos(592, 593),
        "AccountHolderParticipantCountryOfResidence": pos(594, 595),
        "IndentityVerificationMethod":   pos(596, 599),
        "TaxIDType":                     pos(600, 600),
        "TaxIDNumber":                   pos(601, 609),
        "TaxExemptionIndicator":         pos(610, 610),
        "W9OnFile":                      pos(611, 611),
        "CustomerBankCode":              pos(612, 615),
        "CorporateBusinessID":           pos(616, 647),
        "CountryOfTheFormationOrganization": pos(648, 649),
        "StateOfIncorporation":          pos(650, 651),
        "EmployeeOfThisIBD":             pos(652, 652),
        "RelatedToEmployeeOfThisIBD":    pos(653, 653),
        "EmployeeOfAnotherIBD":          pos(654, 654),
        "RelatedToEmployeeOfAnotherIBD": pos(655, 655),
        "EmployeeStatusCode":            pos(656, 659),
        "Occupation":                    pos(660, 674),
        "TaxBracket":                    pos(675, 678),
        "YearsEmployeed":                pos(679, 680),
        "TypeOfBusiness":                pos(681, 715),
        "EmployerName":                  pos(716, 747),
        "AccountHolderParticipantDiscretion": pos(748, 748),
        "MaritalStatus":                 pos(749, 749),
        "Literal7":                      pos(750, 750),
    },
    "H": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),   # 'H'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "AccountHolderParticipantTransactionCode": pos(41, 41),
        "SequenceNumber":                pos(42, 44),
        "AccountHolderType":             pos(45, 47),

        # income/net worth bands
        "JointAccountIncomeNetWorthIndicator": pos(48, 48),
        "MinimumAnnualIncomeAmount":     pos(49, 62),
        "MaximumAnnualIncomeAmount":     pos(63, 76),
        "MinimumNetWorthAmount":         pos(77, 90),
        "MaximumNetWorthAmount":         pos(91, 104),

        # phone blocks (1..7) — show first two; repeat pattern for the rest
        "PhoneTransactionCode1":         pos(105, 105),
        "USInternationalIndicator1":     pos(106, 106),
        "PhoneTypeID1":                  pos(107, 107),
        "PhoneNumber1":                  pos(108, 155),
        "PhoneExtension1":               pos(156, 162),

        "PhoneTransactionCode2":         pos(163, 163),
        "USInternationalIndicator2":     pos(164, 164),
        "PhoneTypeID2":                  pos(165, 165),
        "PhoneNumber2":                  pos(166, 213),
        "PhoneExtension2":               pos(214, 220),

        # … add 3..7 similarly …

        # "ConsolidatedLiquidNetWorthIndicator": (… , …),
        # "MinimumLiquidNetWorthAmount":  pos(… , …),
        # "MaximumLiquidNetWorthAmount":  pos(… , …),

        # "Literal04":                     pos(… , …),

        # "AccountHolderParticipantRoleCode": pos(… , …),
        # "ParticipantShortName":          pos(… , …),
        # "ParticipantMailRecipientIndicator": pos(… , …),

        # "Literal05":                     pos(… , …),
        # "EmailAddress":                  pos(… , …),

        # ID docs 1/2 (add exact ranges from spec)
        # "TypeOfUnexpiredPhotoGovernmentID1": pos(...), "UnexpiredPhotoGovernmentIDNumber1": pos(...),
        # "CountryOfUnexpiredPhotoGovernmentID1": pos(...), "StateOfUnexpiredPhotoGovernmentID1": pos(...),
        # "ExpirationDateOfUnexpiredPhotoGovernmentID1": pos(...), "IssueDateOfUnexpiredPhotoGovernmentID1": pos(...),
        # "TypeOfUnexpiredPhotoGovernmentID2": pos(...), "UnexpiredPhotoGovernmentIDNumber2": pos(...),
        # ...

        # "SpecifiedAdultIndicator":       pos(… , …),
        # "Literal06":                     pos(… , …),
        # "Literal07":                     pos(… , …),
    },

    # =========================
    # RECORD I / J — Custom fields (1–10 / 11–15)
    # =========================
    "I": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),   # 'I'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),
        # Then pairs of (LabelN, DetailN, StatusN) … add your exact ranges
        # "CustomFieldTransactionCode1": pos(...),
        # "CustomFieldLabel1": pos(...), "CustomFieldDetailText1": pos(...), "CustomFieldStatusIndicator1": pos(...),
        # ...
    },
    "J": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),   # 'J'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),
        # "CustomFieldTransactionCode2": pos(...),
        # "CustomFieldLabel11": pos(...), "CustomFieldDetailText11": pos(...), "CustomFieldStatusIndicator11": pos(...),
        # ...
    },

    # =========================
    # RECORD K — Custom fields (16–25)
    # =========================
    "K": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),   # 'K'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),

        "SecondarySequenceNumber":       pos(39, 40),
        "CustomFieldTransactionCode3":   pos(41, 41),

        # Then (Label16/Detail16/Status16 + Literal04), … up to 25 + Literal13/Literal14
        # "CustomFieldLabel16": pos(...), "CustomFieldDetailText16": pos(...), "CustomFieldStatusIndicator16": pos(...),
        # "Literal04": pos(...),
        # ...
    },

    # =========================
    # RECORD L — Advisory summary
    # =========================
    "L": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),   # 'L'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "AdvisoryAccountTransactionCode": pos(41, 41),
        "InceptionDate":                 pos(42, 49),   # CCYYMMDD
        "AdvisoryProgramCode":           pos(50, 59),
        "AdvisoryProductTypeCode":       pos(60, 69),
        "AdvisoryProgramProductTypeLongName": pos(70, 189),
        "AdvisoryMoneyManagerCode":      pos(190, 199),
        "AdvisoryMoneyManagerName":      pos(200, 319),
        "AdvisoryManagementStyleCode":   pos(320, 329),
        "AdvisoryManagementStyle":       pos(330, 449),

        "Literal04":                     pos(450, 749),
        # "Literal05": end marker if present in your table
    },
    "M": {
        # identity block
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'M'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # per-record header (common ACCT convention)
        "RecordTransactionCode":         pos(41, 41),
        "SequenceNumber":                pos(42, 44),
        "AccountHolderType":             pos(45, 47),
        "AccountHolderParticipantRoleCode": pos(48, 51),

        # suitability experience/knowledge bands (fill from spec)
        # "GeneralInvestmentKnowledge":    (..., ...),
        # "YearEquityInvestmentExperienceBegan": (..., ...),
        # "EquityInvestKnowledgeCode":     (..., ...),
        # "YearOptionInvestmentExperienceBegan": (..., ...),
        # "OptionInvestmentKnowledgeCode": (..., ...),
        # "YearFixedIncomeInvestmentExperienceBegan": (..., ...),
        # "FixedIncomeInvestmentKnowledgeCode": (..., ...),
        # "YearMutualFundInvestmentExperienceBegan": (..., ...),
        # "MutualFundInvestmentKnowledgeCode": (..., ...),
        # "YearUITInvestmentExperienceBegan": (..., ...),
        # "UITInvestmentKnowledgeCode":    (..., ...),
        # "YearETFInvestmentExperienceBegan": (..., ...),
        # "ETFInvestKnowCode":             (..., ...),
        # "YearRealEstateInvestmentExperienceBegan": (..., ...),
        # "RealEstateInvestmentKnowledgeCode": (..., ...),
        # "YearInsuranceInvestmentExperienceBegan": (..., ...),
        # "InsuranceInvestmentKnowledgeCode": (..., ...),
        # "YearVariableAnnuityInvestmentExperienceBegan": (..., ...),
        # "VariableAnnuityInvestmentKnowledgeCode": (..., ...),
        # "YearFixedAnnuityInvestmentExperienceBegan": (..., ...),
        # "FixedAnnuityInvestmentKnowledgeCode": (..., ...),
        # "YearPreciousMetalsInvestmentExperienceBegan": (..., ...),
        # "PreciousMetalsInvestmentKnowledgeCode": (..., ...),
        # "YearCommodityAndFuturesInvestmentExperienceBegan": (..., ...),
        # "CommodityAndFuturesInvestmentKnowledgeCode": (..., ...),
        # "OtherInvestType":               (..., ...),
        # "YearOtherTypeInvestmentExperienceBegan": (..., ...),
        # "OtherInvestmentKnowledgeCode":  (..., ...),

        # # docs + related employee / dependents
        # "Literal04":                     (..., ...),
        # "Literal05":                     (..., ...),
        # "DocumentCode":                  (..., ...),
        # "DocumentReceivedDate":          (..., ...),
        # "DocumentExpirationDate":        (..., ...),
        # "RelatedToEmployeeOfThisIbdEmployeeID": (..., ...),
        # "NumberOfDependents":            (..., ...),

        # # bank address block
        # "BankName":                      (..., ...),
        # "AttentionLinePrefix":           (..., ...),
        # "AttentionLineDetail":           (..., ...),
        # "BankAddressLine1":              (..., ...),
        # "BankAddressLine2":              (..., ...),
        # "BankAddressLine3":              (..., ...),
        # "BankAddressLine4":              (..., ...),
        # "City":                          (..., ...),
        # "State":                         (..., ...),
        # "ZipCode":                       (..., ...),
        # "Country":                       (..., ...),

        # "Literal06":                     (..., ...),
        # "Literal07":                     (..., ...),
        # "ClientID":                      (..., ...),
        # "Literal08":                     (..., ...),
        # LastUpdateDate is stamped in code
    },

    # =========================
    # N — Business Parties (1..32 blocks)
    # =========================
    "N": {
        # identity
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'N'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # Repeating groups; fill each quartet + literal from spec:
        # BusinessParty{n}TransactionCode, ID, RoleCode, HasDiscretion, Literal{n+3}
        # "BusinessParty1TransactionCode": (..., ...),
        # "BusinessParty1ID":              (..., ...),
        # "BusinessParty1RoleCode":        (..., ...),
        # "BusinessParty1HasDiscretion":   (..., ...),
        # "Literal04":                     (..., ...),

        # # ... repeat for 2..32 ...

        # "SecondarySequenceNumber":       (..., ...),
        # "Literal36":                     (..., ...),
        # LastUpdateDate stamped
    },

    # =========================
    # P — Alerts / DTC / FED / CEDEL / Routing
    # =========================
    "P": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'P'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # "ParentID":                      (..., ...),
        # "InstitutionID":                 (..., ...),
        # "InstitutionAccountNumber":      (..., ...),
        # "AlertAcronym":                  (..., ...),
        # "AlertAccessCode":               (..., ...),
        # "ConfirmationOption":            (..., ...),
        # "BirthDate":                     (..., ...),
        # "Literal04":                     (..., ...),
        # "CountryOfCitizenship":          (..., ...),

        # # DTC / FED / EURO / CEDEL / Physical
        # "DTCTransactionCode":            (..., ...),
        # "LocationProductCode":           (..., ...),
        # "InstitutionNumber":             (..., ...),
        # "InstitutionName":               (..., ...),
        # "AgentNumber":                   (..., ...),
        # "AgentName":                     (..., ...),
        # "AgentInternalNumber":           (..., ...),
        # "AgentInternalName":             (..., ...),
        # "ClearingAgentNumber":           (..., ...),
        # "ClearingAgentName":             (..., ...),
        # "FirstDTCIpNumber":              (..., ...),
        # "FirstIPAccountNumber":          (..., ...),
        # "SecondDTCIpNumber":             (..., ...),
        # "SecondIPAccountNumber":         (..., ...),

        # "FedTransactionCode":            (..., ...),
        # "FedLocationProductCode":        (..., ...),
        # "ABANumber":                     (..., ...),
        # "InternalAccountNumber":         (..., ...),
        # "FederalWireBankName":           (..., ...),

        # "EUROTransactionCode":           (..., ...),
        # "EUROLocationProductCode":       (..., ...),
        # "EUROClearNumber":               (..., ...),
        # "EUROClearAccountNumber":        (..., ...),

        # "CEDTransactionCode":            (..., ...),
        # "CEDLocationProductCode":        (..., ...),
        # "CEDELNumber":                   (..., ...),
        # "CEDELAccountNumber":            (..., ...),

        # "PhysicalTransactionCode":       (..., ...),
        # "PhysicalLocationProductCode":   (..., ...),
        # "AccountNumberForPhysicalDelivery": (..., ...),

        # "OtherInstructions1":            (..., ...),
        # "OtherInstructions2":            (..., ...),
        # "OtherInstructions3":            (..., ...),
        # "OtherInstructions4":            (..., ...),
        # "OtherInstructions5":            (..., ...),
        # "OtherInstructions6":            (..., ...),
        # "Literal05":                     (..., ...),
    },

    # =========================
    # R — Retirement account
    # =========================
    "R": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'R'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # "RetirementAccountTransactionCode": (..., ...),
        # "ParticipantMaritalStatus":      (..., ...),
        # "SexOfParticipant":              (..., ...),
        # "CustodianCode":                 (..., ...),
        # "TypeOfRetirementPlan":          (..., ...),
        # "TypeOfRetirementAccount":       (..., ...),
        # "RetirementPlanNumber":          (..., ...),
        # "SelfDirectedIndicator":         (..., ...),
        # "AssetWillIndicator":            (..., ...),

        # # dates
        # "BrokerDealerConversionDate":    (..., ...),
        # "AdoptionAgreementDate":         (..., ...),
        # "DatePlanEstablished":           (..., ...),
        # "CustodianDate":                 (..., ...),
        # "PlanAmendmentDate":             (..., ...),
        # "SpousalConsentDate":            (..., ...),
        # "EducationDisabilityIndicator":  (..., ...),
        # "DisabilityStartDate":           (..., ...),
        # "DateOfDeath":                   (..., ...),

        # # related accounts & employer block
        # "RelatedBrokerageAccountNumber1": (..., ...),
        # "RelatedBrokerageAccountNumber2": (..., ...),
        # "RelatedBrokerageAccountNumber3": (..., ...),
        # "EmployerName":                  (..., ...),
        # "EmployerTIN":                   (..., ...),
        # "TrustAdministrator":            (..., ...),
        # "EmployerAddressTransactionCode": (..., ...),
        # "SpecialHandlingIndicator":      (..., ...),
        # "AttentionLinePrefix":           (..., ...),
        # "EmployerAttentionLineDetail":   (..., ...),
        # "EmployerAddressLine1":          (..., ...),
        # "EmployerAddressLine2":          (..., ...),
        # "EmployerAddressLine3":          (..., ...),
        # "EmployerAddressLine4":          (..., ...),
        # "City":                          (..., ...),
        # "State":                         (..., ...),
        # "Zip":                           (..., ...),
        # "CountryCode":                   (..., ...),

        # "Literal04":                     (..., ...),
        # "EmailAddress":                  (..., ...),

        # # phones 1..2
        # "TelephoneTransactionCode1":     (..., ...),
        # "USInternationalIndicator1":     (..., ...),
        # "TelephoneTypeID1":              (..., ...),
        # "TelephoneNumber1":              (..., ...),
        # "TelephoneExtension1":           (..., ...),
        # "TelephoneTransactionCode2":     (..., ...),
        # "USInternationalIndicator2":     (..., ...),
        # "TelephoneTypeID2":              (..., ...),
        # "TelephoneNumber2":              (..., ...),
        # "TelephoneExtension2":           (..., ...),

        # "MutualFundIndicator":           (..., ...),
        # "Literal05":                     (..., ...),
        # "Literal06":                     (..., ...),
        # "Literal07":                     (..., ...),
    },

    # =========================
    # S — More phones + original beneficiary DOB
    # =========================
    "S": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'S'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # phones 3..7 (match R’s widths)
        # "TelephoneTransactionCode3":     (..., ...),
        # "USInternationalIndicator3":     (..., ...),
        # "TelephoneTypeID3":              (..., ...),
        # "TelephoneNumber3":              (..., ...),
        # "TelephoneExtension3":           (..., ...),
        # "TelephoneTransactionCode4":     (..., ...),
        # "USInternationalIndicator4":     (..., ...),
        # "TelephoneTypeID4":              (..., ...),
        # "TelephoneNumber4":              (..., ...),
        # "TelephoneExtension4":           (..., ...),
        # "TelephoneTransactionCode5":     (..., ...),
        # "USInternationalIndicator5":     (..., ...),
        # "TelephoneTypeID5":              (..., ...),
        # "TelephoneNumber5":              (..., ...),
        # "TelephoneExtension5":           (..., ...),
        # "TelephoneTransactionCode6":     (..., ...),
        # "USInternationalIndicator6":     (..., ...),
        # "TelephoneTypeID6":              (..., ...),
        # "TelephoneNumber6":              (..., ...),
        # "TelephoneExtension6":           (..., ...),
        # "TelephoneTransactionCode7":     (..., ...),
        # "USInternationalIndicator7":     (..., ...),
        # "TelephoneTypeID7":              (..., ...),
        # "TelephoneNumber7":              (..., ...),
        # "TelephoneExtension7":           (..., ...),

        # "Literal05":                     (..., ...),
        # "OriginalBeneficiaryDateOfBirth": (..., ...),
        # "Literal06":                     (..., ...),
        # "Literal07":                     (..., ...),
    },

    # =========================
    # T — Beneficiaries (core + address + phones)
    # =========================
    "T": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'T'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "BeneficiaryTransactionCode":    pos(41, 41),
        "BeneficiaryType":               pos(42, 42),
        "SequenceNumber":                pos(43, 45),
        # "Literal04":                     (..., ...),
        # "BeneficiaryRelationshipIndicator": (..., ...),
        # "PrimaryCountryOfCitizenship":   (..., ...),
        # "Literal05":                     (..., ...),
        # "SexOfBeneficiary":              (..., ...),
        # "BeneficiaryBirthDate":          (..., ...),
        # "TaxIDType":                     (..., ...),
        # "BeneficiaryTaxIDNumber":        (..., ...),
        # "PercentAllocation":             (..., ...),

        # "BeneficiaryNameType":           (..., ...),
        # "BeneficiaryPrefixEntityLine1":  (..., ...),
        # "BeneficiaryFirstNameEntityLine2": (..., ...),
        # "BeneficiaryMiddleNameEntityLine3": (..., ...),
        # "BeneficiaryLastNameEntityLine4": (..., ...),

        # "Literal06":                     (..., ...),
        # "BeneficiaryAddressTransactionCode": (..., ...),
        # "SpecialHandlingIndicator":      (..., ...),
        # "AttentionLinePrefix":           (..., ...),
        # "BeneficiaryAttentionLineDetail": (..., ...),
        # "BeneficiaryAddressLine1":       (..., ...),
        # "BeneficiaryAddressLine2":       (..., ...),
        # "BeneficiaryAddressLine3":       (..., ...),
        # "BeneficiaryAddressLine4":       (..., ...),
        # "City":                          (..., ...),
        # "State":                         (..., ...),
        # "Zip":                           (..., ...),
        # "NonUSOrCanadaCity":             (..., ...),
        # "CountryCode":                   (..., ...),

        # "Literal07":                     (..., ...),
        # "BeneficiaryPhoneTransactionCode1": (..., ...),
        # "BeneficiaryUSInternationalIndicator1": (..., ...),
        # "BeneficiaryPhoneTypeID1":       (..., ...),
        # "BeneficiaryPhoneNumber1":       (..., ...),
        # "BeneficiaryPhoneExtension1":    (..., ...),
        # "BeneficiaryPhoneTransactionCode2": (..., ...),
        # "BeneficiaryUSInternationalIndicator2": (..., ...),
        # "BeneficiaryPhoneTypeID2":       (..., ...),
        # "BeneficiaryPhoneNumber2":       (..., ...),
        # "BeneficiaryPhoneExtension2":    (..., ...),
        # "BeneficiaryPhoneTransactionCode3": (..., ...),
        # "BeneficiaryUSInternationalIndicator3": (..., ...),
        # "BeneficiaryPhoneTypeID3":       (..., ...),
        # "BeneficiaryPhoneNumber3":       (..., ...),
        # "BeneficiaryPhoneExtension3":    (..., ...),

        # "BeneficiaryPaymentAmount":      (..., ...),
        # "PerStripesBeneficiaryDesignation": (..., ...),
        # "ExternalClientIDSuppliedByCustomer": (..., ...),
        # "InternalPershingAssignedClientID": (..., ...),
        # "TypeOfTrust":                   (..., ...),
        # "DateTrustEstablished":          (..., ...),
        # "Literal08":                     (..., ...),
        # "Literal09":                     (..., ...),
    },

    # =========================
    # U — Beneficiary extras (phones 4..7 + trustee + address + email)
    # =========================
    "U": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'U'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "BeneficiaryTransactionCode":    pos(41, 41),
        "BeneficiaryType":               pos(42, 42),
        "SequenceNumber":                pos(43, 45),
        # "Literal04":                     (..., ...),

        # phones 4..7
        # "BeneficiaryPhoneTransactionCode4": (..., ...),
        # "BeneficiaryUSInternationalIndicator4": (..., ...),
        # "BeneficiaryPhoneTypeID4":       (..., ...),
        # "BeneficiaryPhoneNumber4":       (..., ...),
        # "BeneficiaryPhoneExtension4":    (..., ...),
        # "BeneficiaryPhoneTransactionCode5": (..., ...),
        # "BeneficiaryUSInternationalIndicator5": (..., ...),
        # "BeneficiaryPhoneTypeID5":       (..., ...),
        # "BeneficiaryPhoneNumber5":       (..., ...),
        # "BeneficiaryPhoneExtension5":    (..., ...),
        # "BeneficiaryPhoneTransactionCode6": (..., ...),
        # "BeneficiaryUSInternationalIndicator6": (..., ...),
        # "BeneficiaryPhoneTypeID6":       (..., ...),
        # "BeneficiaryPhoneNumber6":       (..., ...),
        # "BeneficiaryPhoneExtension6":    (..., ...),
        # "BeneficiaryPhoneTransactionCode7": (..., ...),
        # "BeneficiaryUSInternationalIndicator7": (..., ...),
        # "BeneficiaryPhoneTypeID7":       (..., ...),
        # "BeneficiaryPhoneNumber7":       (..., ...),
        # "BeneficiaryPhoneExtension7":    (..., ...),

        # # trustee + address + email
        # "BeneficiaryTrustTransactionCode": (..., ...),
        # "BeneficiaryTrusteeNameTypeCode":  (..., ...),
        # "BeneficiaryTrusteePrefixEntityLine1": (..., ...),
        # "BeneficiaryTrusteeFirstNameEntityLine2": (..., ...),
        # "BeneficiaryTrusteeMiddleNameEntityLine3": (..., ...),
        # "BeneficiaryTrusteeLastNameEntityLine4": (..., ...),

        # "BeneficiaryAddressTransactionCode": (..., ...),
        # "SpecialHandlingIndicator":      (..., ...),
        # "AttentionLinePrefix":           (..., ...),
        # "BeneficiaryAttentionLineDetail": (..., ...),
        # "BeneficiaryAddressLine1":       (..., ...),
        # "BeneficiaryAddressLine2":       (..., ...),
        # "BeneficiaryAddressLine3":       (..., ...),
        # "BeneficiaryAddressLine4":       (..., ...),
        # "City":                          (..., ...),
        # "State":                         (..., ...),
        # "Zip":                           (..., ...),
        # "NonUSOrCanadaCity":             (..., ...),
        # "CountryCode":                   (..., ...),
        # "BeneficiaryEmailAddress":       (..., ...),

        # "Literal05":                     (..., ...),
        # "Literal06":                     (..., ...),
    },
    
    
    "W": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'W'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        # Flags near start (adjust with your spec if they shift)
        "RecordTransactionCode":         pos(41, 41),
        "NonUSDollarTrading":            pos(42, 42),
        "BaseCurrency":                  pos(43, 45),

        # ... many middle fields (phones, delivery, etc.) ...

        "EmailAddress":                  pos(646, 695),
        "ExternalPositionsIndicator":    pos(696, 696),
        "PurgeEligibleIndicator":        pos(697, 697),
        "AdvisoryAcctIndicator":         pos(698, 698),
        "ProductProfileCode":            pos(699, 702),
        "CentsPerShareDiscount":         pos(703, 704),
        "CountryOfTaxResidency":         pos(746, 749),
        # end marker: 750
    },
    "X": {
        "TransactionCode":               pos(1, 2),
        "RecordIndicatorValue":          pos(3, 3),     # 'X'
        "RecordIDSequenceNumber":        pos(4, 11),
        "AccountNumber":                 pos(12, 20),
        "IBDNumber":                     pos(21, 23),
        "Literal01":                     pos(24, 24),
        "InvestmentProfessionalNumber":  pos(25, 28),
        "AccountShortName":              pos(29, 38),
        "Literal03":                     pos(39, 40),

        "RecordTransactionCode":         pos(41, 41),
        "SequenceNumber":                pos(42, 44),
        "AccountHolderType":             pos(45, 47),

    #     "Literal04":                     (..., ...),
    #     "AttentionLinePrefix":           (..., ...),
    #     "AttentionLineDetail":           (..., ...),
    #     "StreetAddressLine1":            (..., ...),
    #     "StreetAddressLine2":            (..., ...),
    #     "StreetAddressLine3":            (..., ...),
    #     "StreetAddressLine4":            (..., ...),
    #     "City":                          (..., ...),
    #     "State":                         (..., ...),
    #     "Zip":                           (..., ...),
    #     "CountryCode":                   (..., ...),

    #     "Literal05":                     (..., ...),
    #     "EmployeeOfThisIBD":             (..., ...),
    #     "RelatedToEmployeeOfThisIBD":    (..., ...),
    #     "EmployeeFirstName":             (..., ...),
    #     "EmployeeLastName":              (..., ...),
    #     "EmployeeSuffix":                (..., ...),
    #     "RelationshipToEmployee":        (..., ...),
    #     "EmployeeOfAnotherIBD":          (..., ...),
    #     "AnotherIBDName":                (..., ...),
    #     "RelatedToEmployeeOfAnotherIBD": (..., ...),
    #     "RelatedToEmployeeIBDName":      (..., ...),
    #     "RelatedToEmployeeFirstName":    (..., ...),
    #     "RelatedToEmployeeLastName":     (..., ...),
    #     "RelatedToEmployeeSuffix":       (..., ...),
    #     "RelationshipToEmployeeOfAnotherIBD": (..., ...),
    #     "OtherBrockerageAccounts":       (..., ...),
    #     "NameOfIBDWhereAccountHeld":     (..., ...),
    #     "HolderParticipantOrImmediateFamilyMember": (..., ...),
    #     "Affiliation":                   (..., ...),
    #     "HolderParticipantSeniorOfficer": (..., ...),
    #     "NameOfPublicCompany":           (..., ...),
    #     "IDVerificationComments":        (..., ...),

    #     "AccountHolderParticipantRoleCode": (..., ...),
    #     "BeneficiaryPercentAllocation":  (..., ...),
    #     "RelationshipToPrimaryHolderCode": (..., ...),
    #     "Literal06":                     (..., ...),
    #     "PrimaryHolderRelationshipToDecedent": (..., ...),
    #     "DateOfDeath":                   (..., ...),

    #     "LargeTraderIDPrefix":           (..., ...),
    #     "Literal07":                     (..., ...),
    #     "LargeTraderIDSuffix":           (..., ...),
    #     "Literal08":                     (..., ...),
    #     "AdditionalCountryOfCitizenship1": (..., ...),
    #     "AdditionalCountryOfCitizenship2": (..., ...),
    #     "AdditionalCountryOfCitizenship3": (..., ...),
    #     "AdditionalCountryOfCitizenship4": (..., ...),
    #     "AdditionalCountryOfCitizenship5": (..., ...),
    #     "USResidentAlien":               (..., ...),
    #     "CountryOfBirth":                (..., ...),
    #     "PerStirpesBeneficiaryDesignation": (..., ...),
    #     "InternalPershingAssignedClientID": (..., ...),
    #     "Literal09":                     (..., ...),
    #     "FormedOnDate":                  (..., ...),
    #     "Literal10":                     (..., ...),
    },
}