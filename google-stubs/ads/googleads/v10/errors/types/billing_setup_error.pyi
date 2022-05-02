import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BillingSetupErrorEnum(proto.Message):
    class BillingSetupError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_USE_EXISTING_AND_NEW_ACCOUNT: int
        CANNOT_REMOVE_STARTED_BILLING_SETUP: int
        CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT: int
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS: int
        INVALID_PAYMENTS_ACCOUNT: int
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY: int
        INVALID_START_TIME_TYPE: int
        THIRD_PARTY_ALREADY_HAS_BILLING: int
        BILLING_SETUP_IN_PROGRESS: int
        NO_SIGNUP_PERMISSION: int
        CHANGE_OF_BILL_TO_IN_PROGRESS: int
        PAYMENTS_PROFILE_NOT_FOUND: int
        PAYMENTS_ACCOUNT_NOT_FOUND: int
        PAYMENTS_PROFILE_INELIGIBLE: int
        PAYMENTS_ACCOUNT_INELIGIBLE: int
        CUSTOMER_NEEDS_INTERNAL_APPROVAL: int
        PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH: int
        FUTURE_START_TIME_PROHIBITED: int
