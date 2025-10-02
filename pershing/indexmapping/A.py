
def table_index_a():
    return  {
    # ---- Identity block (per spec; 1–23) ----
    "TransactionCode":               (1, 2),
    "RecordIndicatorValue":          (3, 3),           # should be "A"
    "RecordIDSequenceNumber":        (4, 11),
    "AccountNumber":                 (12, 20),
    "IBDNumber":                     (21, 23),

    # ---- Early columns present in your table ----
    "Literal01":                     (24, 24),
    "InvestmentProfessionalNumber":  (25, 28),
    "AccountShortName":              (29, 38),

    # ⚠️ The following early flags/fields exist in your table; add once you confirm  itions from your spec.
    "Literal03":                   (39, 40),
    "TransactionType":             (41, 41),
    "AutoTitledAccount":           (42, 42),
    "AccountTypeCode":             (43, 43),
    "RegistrationType":            (44, 47),
    "NumberedAcctIndicator":       (48, 48),
    "NumberOfAccountTitleLines":   (49, 49),
    "AccountRegistrationLine1":    (50, 81),
    "AccountRegistrationLine2":    (82, 113),
    "AccountRegistrationLine3":    (114, 145),
    "AccountRegistrationLine4":    (146, 177),
    "AccountRegistrationLine5":    (178, 209),
    "AccountRegistrationLine6":    (210, 241),
    "USResidentIndicator":         (242, 242),
    "MarriedIndicator":            (243, 243),
    "TenancyState":                (244, 245),
    "JointTenancyClause":          (246, 249),
    "AgreementExecDate":           (250, 257),  # CCYYMMDD (or MM/DD/CCYY in some feeds)
    "NumberOfTenants":             (258, 259),

    # ---- UGMA/Trust/Plan area (confirm per spec) ----
    # "Literal04":                   (...),
    # "StateGiftGiven":              (...),
    # "DateGiftGiven":               (...),
    # "AgeToTerminate":              (...),
    # "MinorsBirthDate":             (...),
    # "MannerOfGift":                (...),
    # "TypeOfTrust":                 (...),
    # "DateTrustEstablished":        (...),
    # "AmmendDate":                  (...),

    # ---- Status & dates (confirm per spec) ----
    # "TrusteeIndependentAction":    (...),
    # "TrusteeNaturalPersonsIndicator":  (...),
    # "BeneficiaryOfTrustNaturalPersons":  (...),
    # "TrustIsDulyOrganizedIndicator":  (...),
    # "PlanEstablishedDate":         (...),
    # "PlanAmendmentDate":           (...),
    # "Literal05":                   (...),
    # "DateAccountOpened":           (...),
    # "DateAccountInformationUpdated":  (...),
    # "AccountStatusIndicator":      (...),
    # "PendingClosedDate":           (...),
    # "DateAccountClosed":           (...),
    # "ClosingNoticedDate":          (...),
    # "AccountReactivationDate":     (...),
    # "DateAccountReOpened":         (...),

    # ---- Instructions / statement counts (confirm per spec) ----
    "Proceeds":                    (559, 559),
    "TransferInstructions":        (...),
    "IncomeInstructions":          (...),
    "NumberOfConfirms":            (...),
    "NumberOfStatements":          (...),
    "InvestmentObjectiveTransacCode":  (...),
    "Comments":                    (...),

    # ---- Employer fields (confirm per spec) ----
    "EmployerShortName":           (...),
    "EmployerCusip":               (...),
    "EmployerSymbol":              (...),

    # ---- Options/margin flags (confirm per spec) ----
    "MarginPrivilegesRevoked":     (...),
    "StatementReviewDate":         (...),
    "MarginPapersOnFile":          (...),
    "OptionsPapersOnFile":         (...),
    "Literal06":                   (...),
    "GoodFaithMargin":             (...),
    "InvProflDiscretionGranted":   (...),
    "InvAdvisorDiscretionGranted":  (...),
    "ThirdPartyDiscretionGranted":  (...),
    "ThirdPartyName":              (...),
    "RiskFactorCode":              (...),
    "InvestmentObjectiveCode":     (...),

    # ---- Options levels & limits (confirm per spec) ----
    "OptionEquities":              (...),
    "OptionIndex":                 (...),
    "OptionDebt":                  (...),
    "OptionCurrency":              (...),
    "OptionLevel1":                (...),
    "OptionLevel2":                (...),
    "OptionLevel3":                (...),
    "OptionLevel4":                (...),
    "OptionCallLimits":            (...),   # may be numeric text
    "OptionPytLimits":             (...),
    "OptionTotalLimitsPutsAndCalls":  (...),
    "NonUSDollarTrading":          (...),
    "Literal07":                   (...),
    "NonCustomerIndicator":        (...),

    # ---- Fees/commissions (confirm per spec) ----
    "ThirdPartyFeeIndicator":      (...),
    "ThirdPartyFeeApprovalDate":   (...),
    "IntermediaryAccountIndicator":  (...),
    "CommisionSchedule":           (...),
    "GroupIndex":                  (...),
    "MoneyManagerId":              (...),
    "MoneyManagerObjectiveId":     (...),
    "DtcIdConfNumerForNonCODAcct":  (...),
    "CapsMasterMneumonic":         (...),
    "EmployeeId":                  (...),
    "PrimeBrokerFreeFundInd":      (...),
    "FeeBasedAccountIndicator":    (...),
    "BillingType":                 (...),
    "FeeBasedTerminationDate":     (...),
    "EquifaxCreditCheckIndicator":  (...),

    # ---- 401k / plan fields (confirm per spec) ----
    "SelfDirected401kPlanName":    (...),
    "SelfDirected401kAcctType":    (...),
    "PlanType":                    (...),
    "PlanNumber":                  (...),

    # ---- Discounts/controls/signatures (confirm per spec) ----
    "EmployeeRelativeIndicator":   (...),
    "CommissionPercentDiscount":   (...),
    "MutualFundFeesBlockingIndicator":  (...),
    "NameOfInvestProfessionalWhoSigned":  (...),
    "DateInvestmentProfessionalSigned":    (...),
    "NameOfPrincipalWhoSigned":   (...),
    "DatePrincipalSigned":        (...),

    # ---- USA PATRIOT / KYC tail ( itions known, matched to DB column names) ----
    "PEPIndicator":                  (672, 671),
    "PrivateBankingAcctIndicator":   (673, 672),
    "ForeignBankAcctIndicator":      (674, 673),
    "InitialSourceOfFunds":          (675, 677),
    "USAPatriotActExemptReason":     (679, 681),
    "PrimaryCountryOfCitizenship":   (683, 683),
    "CountryOfResidence":            (685, 685),
    "BirthDate":                     (687, 693),   # CCYYMMDD (convert to DATE)

    # ---- More trailing controls (confirm per spec) ----
    "AgeBasedFundRollExepmtIndicator":  (...),
    "MoneyFundReformRetail":      (...),
    "TrustContactStatus":         (...),
    "RegulatoryAccountTypeCategory":  (...),
    "AccountManagedByTrustCoIndicator":  (...),
    "VotingAuthority":            (...),
    "IntUsePrimeBrokerCode":      (...),
    "IntUsePayoutCode":           (...),
    "IntUseTraderNumber":         (...),
    "IntUseProductCode":          (...),
    "IntUseCustomerType":         (...),
    "IntUseAccountPlanType":      (...),
    "IntUsePromotionType":        (...),
    "IntUseInvObj1":              (...),
    "IntUseInvObj2":              (...),
    "IntUseInvObj3":              (...),
    "FulfillmentMethod":          (...),
    "CreditInterestIndicator":    (...),
    "AmaIndicator":               (...),
    "Literal08":                  (...),
    "Literal09":                  (...),

    }