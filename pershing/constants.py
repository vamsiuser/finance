from pershing.indexmapping.acct.A import ACCT_A
from pershing.indexmapping.acct.A5 import ACCT_5
from pershing.indexmapping.acct.A7 import ACCT_7
from pershing.indexmapping.acct.B import ACCT_B
from pershing.indexmapping.acct.C import ACCT_C
from pershing.indexmapping.acct.D import ACCT_D
from pershing.indexmapping.acct.E import ACCT_E
from pershing.indexmapping.acct.A4 import ACCT_4
from pershing.indexmapping.acct.F import ACCT_F
from pershing.indexmapping.acct.G import ACC_G
from pershing.indexmapping.acct.H import ACCT_H
from pershing.indexmapping.acct.HEADER import ACC_HEADER
from pershing.indexmapping.acct.I import ACCT_I
from pershing.indexmapping.acct.J import ACCT_J
from pershing.indexmapping.acct.K import ACCT_K
from pershing.indexmapping.acct.L import ACCT_L
from pershing.indexmapping.acct.M import ACCT_M
from pershing.indexmapping.acct.N import ACCT_N
from pershing.indexmapping.acct.P import ACCT_P
from pershing.indexmapping.acct.R import ACCT_R
from pershing.indexmapping.acct.S import ACCT_S
from pershing.indexmapping.acct.T import ACCT_T
from pershing.indexmapping.acct.TAILER import ACCT_TAILER
from pershing.indexmapping.acct.U import ACCT_U
from pershing.indexmapping.acct.W import ACCT_W
from pershing.indexmapping.acct.X import ACCT_X

ACCT_A_RETIREMENT_TYPES = ["CPPS", "CUST", "DLJI", "JNTN", "NPLJ", "NPLT", "N52C", "N52T", "TODI", "TODJ", "TRST", "529C", "529T"]
ACCT_A_RETIREMENT_COLUMNS = {
        "USResidentIndicator":           (242, 242),
        "MarriedIndicator":              (243, 243),
        "TenancyState":                  (244, 245),
        "JointTenancyClause":            (246, 249),
        "AgreementExecDate":             (250, 257),   # CCYYMMDD (or convert from MM/DD/CCYY if your feed uses that)
        "NumberOfTenants":               (258, 259),
        "Literal04":                     (260, 262),
        }
ACCT_A_CUSTODIAN_TYPES = ["CUST", "N52C","529C"]
ACCT_A_CUSTODIAN_COLUMNS = {
        "StateGiftGiven":                (242, 243),
        "DateGiftGiven":                 (244, 251),
        "AgeToTerminate":                (252, 253),
        "MinorsBirthDate":               (254, 261),
        "MannerOfGift":                  (262, 262),
        }
ACCT_A_TRUST_TYPES = []
ACCT_A_TRUST_COLUMNS = {
        "TypeOfTrust":                   (242, 242),
        "DateTrustEstablished":          (243,250),
        "AmmendDate":                    (251, 258),
        "TrusteeIndependentAction":      (259, 259),
}
ACCT_A_CPPS_TYPES =  ["CPPS"]
ACCT_A_CPPS_COLUMNS = {
        "PlanEstablishedDate":           (242, 249),
        "PlanAmendmentDate":             (250, 257),
}
        # "TrusteeNaturalPersonsIndicator":(),,
        # "BeneficiaryOfTrustNaturalPersons": (...),
        # "TrustIsDulyOrganizedIndicator": (...),

ACCT_A_DATEFIELDS = ["AccountReactivationDate","BirthDate","ClosingNoticedDate","DateAccountClosed","DateAccountReOpened","DateInvestmentProfessionalSigned","DatePrincipalSigned","FeeBasedTerminationDate","PendingClosedDate","StatementReviewDate","ThirdPartyFeeApprovalDate"]
ACCT_B_DATEFIELDS =["DateTaxIDAppliedFor","W8W9DateSigned","W8W9EffectiveDate","DateFirstBNoticeStatusIssued","DateFirstBNoticeStatusSatisfied","DateSecondBNoticeStatusIssued","DateSecondBNoticeStatusSatisfied","DateCNoticeStatusIssued","DateCNoticeStatusSatisfied","OriginalAccountOpenDate","LargeTraderTypeLastChangeDate","AccountFundingDate","FutureStatementCurrencyDate","LastMonthBooksRecordsMailedDate","LastMonthBooksRecordsSentOutsidePershingDate","FullyPaidLendingAgreementDate","DateSweepActivated","DateSweepDetailsChanged","DvpRestrictionExpirationDate"]
ACCT_C_DATEFIELDS = ["MostRecentMailReturnDate", "SecondMostRecentMailReturnDate", "ThirdMostRecentMailReturnDate", "FromDate1", "ToDate1", "FromDate2", "ToDate2", "FromDate3", "ToDate3"]
ACCT_5_DATEFIELDS = ["InvestmentTimeHorizon", "SecuritizedProductDisclosureMailingDate", "LastInvestmentReviewDate", "LastAdministrativeReviewDate"]


EXTRA_LAYOUT = {"HEADER": ACC_HEADER, "TRAILER": ACCT_TAILER, "4": ACCT_4, "5": ACCT_5, "7": ACCT_7,
    "A": ACCT_A, "B": ACCT_B, "C": ACCT_C, "D": ACCT_D, "E": ACCT_E, "F": ACCT_F,"G": ACC_G, "H": ACCT_H, 
    "I": ACCT_I, "J": ACCT_J, "K": ACCT_K, "L": ACCT_L, "M": ACCT_M, "N": ACCT_N, "P": ACCT_P, "R": ACCT_R,
    "S": ACCT_S, "T": ACCT_T, "U": ACCT_U, "W": ACCT_W, "X": ACCT_X}