import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetErrorEnum(proto.Message):
    class AssetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER_NOT_ON_ALLOWLIST_FOR_ASSET_TYPE: int
        DUPLICATE_ASSET: int
        DUPLICATE_ASSET_NAME: int
        ASSET_DATA_IS_MISSING: int
        CANNOT_MODIFY_ASSET_NAME: int
        FIELD_INCOMPATIBLE_WITH_ASSET_TYPE: int
        INVALID_CALL_TO_ACTION_TEXT: int
        LEAD_FORM_INVALID_FIELDS_COMBINATION: int
        LEAD_FORM_MISSING_AGREEMENT: int
        INVALID_ASSET_STATUS: int
        FIELD_CANNOT_BE_MODIFIED_FOR_ASSET_TYPE: int
        SCHEDULES_CANNOT_OVERLAP: int
        PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF: int
        PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT: int
        TOO_MANY_DECIMAL_PLACES_SPECIFIED: int
        DUPLICATE_ASSETS_WITH_DIFFERENT_FIELD_VALUE: int
        CALL_CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED: int
        CALL_CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED: int
        CALL_DISALLOWED_NUMBER_TYPE: int
        CALL_INVALID_CONVERSION_ACTION: int
        CALL_INVALID_COUNTRY_CODE: int
        CALL_INVALID_DOMESTIC_PHONE_NUMBER_FORMAT: int
        CALL_INVALID_PHONE_NUMBER: int
        CALL_PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY: int
        CALL_PREMIUM_RATE_NUMBER_NOT_ALLOWED: int
        CALL_VANITY_PHONE_NUMBER_NOT_ALLOWED: int
        PRICE_HEADER_SAME_AS_DESCRIPTION: int
        MOBILE_APP_INVALID_APP_ID: int
        MOBILE_APP_INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL: int
        NAME_REQUIRED_FOR_ASSET_TYPE: int
        LEAD_FORM_LEGACY_QUALIFYING_QUESTIONS_DISALLOWED: int
        NAME_CONFLICT_FOR_ASSET_TYPE: int
