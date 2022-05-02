import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExtensionFeedItemErrorEnum(proto.Message):
    class ExtensionFeedItemError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        VALUE_OUT_OF_RANGE: int
        URL_LIST_TOO_LONG: int
        CANNOT_HAVE_RESTRICTION_ON_EMPTY_GEO_TARGETING: int
        CANNOT_SET_WITH_FINAL_URLS: int
        CANNOT_SET_WITHOUT_FINAL_URLS: int
        INVALID_PHONE_NUMBER: int
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY: int
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED: int
        PREMIUM_RATE_NUMBER_NOT_ALLOWED: int
        DISALLOWED_NUMBER_TYPE: int
        INVALID_DOMESTIC_PHONE_NUMBER_FORMAT: int
        VANITY_PHONE_NUMBER_NOT_ALLOWED: int
        INVALID_CALL_CONVERSION_ACTION: int
        CUSTOMER_NOT_ON_ALLOWLIST_FOR_CALLTRACKING: int
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY: int
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED: int
        INVALID_APP_ID: int
        QUOTES_IN_REVIEW_EXTENSION_SNIPPET: int
        HYPHENS_IN_REVIEW_EXTENSION_SNIPPET: int
        REVIEW_EXTENSION_SOURCE_INELIGIBLE: int
        SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT: int
        INCONSISTENT_CURRENCY_CODES: int
        PRICE_EXTENSION_HAS_DUPLICATED_HEADERS: int
        PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION: int
        PRICE_EXTENSION_HAS_TOO_FEW_ITEMS: int
        PRICE_EXTENSION_HAS_TOO_MANY_ITEMS: int
        UNSUPPORTED_VALUE: int
        UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE: int
        INVALID_DEVICE_PREFERENCE: int
        INVALID_SCHEDULE_END: int
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE: int
        INVALID_SNIPPETS_HEADER: int
        CANNOT_OPERATE_ON_REMOVED_FEED_ITEM: int
        PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY: int
        CONFLICTING_CALL_CONVERSION_SETTINGS: int
        EXTENSION_TYPE_MISMATCH: int
        EXTENSION_SUBTYPE_REQUIRED: int
        EXTENSION_TYPE_UNSUPPORTED: int
        CANNOT_OPERATE_ON_FEED_WITH_MULTIPLE_MAPPINGS: int
        CANNOT_OPERATE_ON_FEED_WITH_KEY_ATTRIBUTES: int
        INVALID_PRICE_FORMAT: int
        PROMOTION_INVALID_TIME: int
        TOO_MANY_DECIMAL_PLACES_SPECIFIED: int
        CONCRETE_EXTENSION_TYPE_REQUIRED: int
        SCHEDULE_END_NOT_AFTER_START: int
