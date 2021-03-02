# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FeedItemValidationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedItemValidationErrorValue = typing___NewType(
        "FeedItemValidationErrorValue", builtin___int
    )
    type___FeedItemValidationErrorValue = FeedItemValidationErrorValue
    FeedItemValidationError: _FeedItemValidationError
    class _FeedItemValidationError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 0
        )
        UNKNOWN = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 1
        )
        STRING_TOO_SHORT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 2
        )
        STRING_TOO_LONG = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 3
        )
        VALUE_NOT_SPECIFIED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 4
        )
        INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 5
        )
        INVALID_PHONE_NUMBER = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 6
        )
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 7
        )
        PREMIUM_RATE_NUMBER_NOT_ALLOWED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 8
        )
        DISALLOWED_NUMBER_TYPE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 9
        )
        VALUE_OUT_OF_RANGE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 10
        )
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 11
        )
        CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 99
        )
        INVALID_COUNTRY_CODE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 13
        )
        INVALID_APP_ID = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 14
        )
        MISSING_ATTRIBUTES_FOR_FIELDS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 15
        )
        INVALID_TYPE_ID = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 16
        )
        INVALID_EMAIL_ADDRESS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 17
        )
        INVALID_HTTPS_URL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 18
        )
        MISSING_DELIVERY_ADDRESS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 19
        )
        START_DATE_AFTER_END_DATE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 20
        )
        MISSING_FEED_ITEM_START_TIME = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 21
        )
        MISSING_FEED_ITEM_END_TIME = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 22
        )
        MISSING_FEED_ITEM_ID = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 23
        )
        VANITY_PHONE_NUMBER_NOT_ALLOWED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 24
        )
        INVALID_REVIEW_EXTENSION_SNIPPET = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 25
        )
        INVALID_NUMBER_FORMAT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 26
        )
        INVALID_DATE_FORMAT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 27
        )
        INVALID_PRICE_FORMAT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 28
        )
        UNKNOWN_PLACEHOLDER_FIELD = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 29
        )
        MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 30
        )
        REVIEW_EXTENSION_SOURCE_INELIGIBLE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 31
        )
        HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 32
        )
        DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 33
        )
        QUOTES_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 34
        )
        INVALID_FORM_ENCODED_PARAMS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 35
        )
        INVALID_URL_PARAMETER_NAME = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 36
        )
        NO_GEOCODING_RESULT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 37
        )
        SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 38
        )
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 39
        )
        INVALID_PLACEHOLDER_FIELD_ID = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 40
        )
        INVALID_URL_TAG = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 41
        )
        LIST_TOO_LONG = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 42
        )
        INVALID_ATTRIBUTES_COMBINATION = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 43
        )
        DUPLICATE_VALUES = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 44
        )
        INVALID_CALL_CONVERSION_ACTION_ID = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 45
        )
        CANNOT_SET_WITHOUT_FINAL_URLS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 46
        )
        APP_ID_DOESNT_EXIST_IN_APP_STORE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 47
        )
        INVALID_FINAL_URL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 48
        )
        INVALID_TRACKING_URL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 49
        )
        INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 50
        )
        LIST_TOO_SHORT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 51
        )
        INVALID_USER_ACTION = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 52
        )
        INVALID_TYPE_NAME = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 53
        )
        INVALID_EVENT_CHANGE_STATUS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 54
        )
        INVALID_SNIPPETS_HEADER = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 55
        )
        INVALID_ANDROID_APP_LINK = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 56
        )
        NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 57
        )
        RESERVED_KEYWORD_OTHER = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 58
        )
        DUPLICATE_OPTION_LABELS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 59
        )
        DUPLICATE_OPTION_PREFILLS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 60
        )
        UNEQUAL_LIST_LENGTHS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 61
        )
        INCONSISTENT_CURRENCY_CODES = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 62
        )
        PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 63
        )
        ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 64
        )
        PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 65
        )
        UNSUPPORTED_VALUE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 66
        )
        INVALID_FINAL_MOBILE_URL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 67
        )
        INVALID_KEYWORDLESS_AD_RULE_LABEL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 68
        )
        VALUE_TRACK_PARAMETER_NOT_SUPPORTED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 69
        )
        UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 70
        )
        INVALID_IOS_APP_LINK = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 71
        )
        MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 72
        )
        PROMOTION_INVALID_TIME = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 73
        )
        PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 74
        )
        PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 75
        )
        TOO_MANY_DECIMAL_PLACES_SPECIFIED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 76
        )
        AD_CUSTOMIZERS_NOT_ALLOWED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 77
        )
        INVALID_LANGUAGE_CODE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 78
        )
        UNSUPPORTED_LANGUAGE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 79
        )
        IF_FUNCTION_NOT_ALLOWED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 80
        )
        INVALID_FINAL_URL_SUFFIX = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 81
        )
        INVALID_TAG_IN_FINAL_URL_SUFFIX = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 82
        )
        INVALID_FINAL_URL_SUFFIX_FORMAT = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 83
        )
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 84
        )
        ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 85
        )
        NO_DELIVERY_OPTION_IS_SET = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 86
        )
        INVALID_CONVERSION_REPORTING_STATE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 87
        )
        IMAGE_SIZE_WRONG = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 88
        )
        EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 89
        )
        AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 90
        )
        INVALID_LATITUDE_VALUE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 91
        )
        INVALID_LONGITUDE_VALUE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 92
        )
        TOO_MANY_LABELS = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 93
        )
        INVALID_IMAGE_URL = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 94
        )
        MISSING_LATITUDE_VALUE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 95
        )
        MISSING_LONGITUDE_VALUE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 96
        )
        ADDRESS_NOT_FOUND = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 97
        )
        ADDRESS_NOT_TARGETABLE = typing___cast(
            FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 98
        )
    UNSPECIFIED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 0
    )
    UNKNOWN = typing___cast(FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 1)
    STRING_TOO_SHORT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 2
    )
    STRING_TOO_LONG = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 3
    )
    VALUE_NOT_SPECIFIED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 4
    )
    INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 5
    )
    INVALID_PHONE_NUMBER = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 6
    )
    PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 7
    )
    PREMIUM_RATE_NUMBER_NOT_ALLOWED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 8
    )
    DISALLOWED_NUMBER_TYPE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 9
    )
    VALUE_OUT_OF_RANGE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 10
    )
    CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 11
    )
    CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 99
    )
    INVALID_COUNTRY_CODE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 13
    )
    INVALID_APP_ID = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 14
    )
    MISSING_ATTRIBUTES_FOR_FIELDS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 15
    )
    INVALID_TYPE_ID = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 16
    )
    INVALID_EMAIL_ADDRESS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 17
    )
    INVALID_HTTPS_URL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 18
    )
    MISSING_DELIVERY_ADDRESS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 19
    )
    START_DATE_AFTER_END_DATE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 20
    )
    MISSING_FEED_ITEM_START_TIME = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 21
    )
    MISSING_FEED_ITEM_END_TIME = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 22
    )
    MISSING_FEED_ITEM_ID = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 23
    )
    VANITY_PHONE_NUMBER_NOT_ALLOWED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 24
    )
    INVALID_REVIEW_EXTENSION_SNIPPET = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 25
    )
    INVALID_NUMBER_FORMAT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 26
    )
    INVALID_DATE_FORMAT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 27
    )
    INVALID_PRICE_FORMAT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 28
    )
    UNKNOWN_PLACEHOLDER_FIELD = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 29
    )
    MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 30
    )
    REVIEW_EXTENSION_SOURCE_INELIGIBLE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 31
    )
    HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 32
    )
    DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 33
    )
    QUOTES_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 34
    )
    INVALID_FORM_ENCODED_PARAMS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 35
    )
    INVALID_URL_PARAMETER_NAME = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 36
    )
    NO_GEOCODING_RESULT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 37
    )
    SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 38
    )
    CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 39
    )
    INVALID_PLACEHOLDER_FIELD_ID = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 40
    )
    INVALID_URL_TAG = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 41
    )
    LIST_TOO_LONG = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 42
    )
    INVALID_ATTRIBUTES_COMBINATION = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 43
    )
    DUPLICATE_VALUES = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 44
    )
    INVALID_CALL_CONVERSION_ACTION_ID = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 45
    )
    CANNOT_SET_WITHOUT_FINAL_URLS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 46
    )
    APP_ID_DOESNT_EXIST_IN_APP_STORE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 47
    )
    INVALID_FINAL_URL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 48
    )
    INVALID_TRACKING_URL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 49
    )
    INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 50
    )
    LIST_TOO_SHORT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 51
    )
    INVALID_USER_ACTION = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 52
    )
    INVALID_TYPE_NAME = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 53
    )
    INVALID_EVENT_CHANGE_STATUS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 54
    )
    INVALID_SNIPPETS_HEADER = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 55
    )
    INVALID_ANDROID_APP_LINK = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 56
    )
    NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 57
    )
    RESERVED_KEYWORD_OTHER = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 58
    )
    DUPLICATE_OPTION_LABELS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 59
    )
    DUPLICATE_OPTION_PREFILLS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 60
    )
    UNEQUAL_LIST_LENGTHS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 61
    )
    INCONSISTENT_CURRENCY_CODES = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 62
    )
    PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 63
    )
    ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 64
    )
    PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 65
    )
    UNSUPPORTED_VALUE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 66
    )
    INVALID_FINAL_MOBILE_URL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 67
    )
    INVALID_KEYWORDLESS_AD_RULE_LABEL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 68
    )
    VALUE_TRACK_PARAMETER_NOT_SUPPORTED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 69
    )
    UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 70
    )
    INVALID_IOS_APP_LINK = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 71
    )
    MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 72
    )
    PROMOTION_INVALID_TIME = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 73
    )
    PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 74
    )
    PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 75
    )
    TOO_MANY_DECIMAL_PLACES_SPECIFIED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 76
    )
    AD_CUSTOMIZERS_NOT_ALLOWED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 77
    )
    INVALID_LANGUAGE_CODE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 78
    )
    UNSUPPORTED_LANGUAGE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 79
    )
    IF_FUNCTION_NOT_ALLOWED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 80
    )
    INVALID_FINAL_URL_SUFFIX = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 81
    )
    INVALID_TAG_IN_FINAL_URL_SUFFIX = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 82
    )
    INVALID_FINAL_URL_SUFFIX_FORMAT = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 83
    )
    CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 84
    )
    ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 85
    )
    NO_DELIVERY_OPTION_IS_SET = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 86
    )
    INVALID_CONVERSION_REPORTING_STATE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 87
    )
    IMAGE_SIZE_WRONG = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 88
    )
    EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 89
    )
    AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 90
    )
    INVALID_LATITUDE_VALUE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 91
    )
    INVALID_LONGITUDE_VALUE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 92
    )
    TOO_MANY_LABELS = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 93
    )
    INVALID_IMAGE_URL = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 94
    )
    MISSING_LATITUDE_VALUE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 95
    )
    MISSING_LONGITUDE_VALUE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 96
    )
    ADDRESS_NOT_FOUND = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 97
    )
    ADDRESS_NOT_TARGETABLE = typing___cast(
        FeedItemValidationErrorEnum.FeedItemValidationErrorValue, 98
    )
    type___FeedItemValidationError = FeedItemValidationError
    def __init__(self,) -> None: ...

type___FeedItemValidationErrorEnum = FeedItemValidationErrorEnum