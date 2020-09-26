# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UrlFieldErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    UrlFieldErrorValue = typing___NewType("UrlFieldErrorValue", builtin___int)
    type___UrlFieldErrorValue = UrlFieldErrorValue
    UrlFieldError: _UrlFieldError
    class _UrlFieldError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            UrlFieldErrorEnum.UrlFieldErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 0)
        UNKNOWN = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 1)
        INVALID_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 2
        )
        INVALID_TAG_IN_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 3
        )
        MISSING_TRACKING_URL_TEMPLATE_TAG = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 4
        )
        MISSING_PROTOCOL_IN_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 5
        )
        INVALID_PROTOCOL_IN_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 6
        )
        MALFORMED_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 7
        )
        MISSING_HOST_IN_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 8
        )
        INVALID_TLD_IN_TRACKING_URL_TEMPLATE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 9
        )
        REDUNDANT_NESTED_TRACKING_URL_TEMPLATE_TAG = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 10
        )
        INVALID_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 11)
        INVALID_TAG_IN_FINAL_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 12
        )
        REDUNDANT_NESTED_FINAL_URL_TAG = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 13
        )
        MISSING_PROTOCOL_IN_FINAL_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 14
        )
        INVALID_PROTOCOL_IN_FINAL_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 15
        )
        MALFORMED_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 16)
        MISSING_HOST_IN_FINAL_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 17
        )
        INVALID_TLD_IN_FINAL_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 18
        )
        INVALID_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 19
        )
        INVALID_TAG_IN_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 20
        )
        REDUNDANT_NESTED_FINAL_MOBILE_URL_TAG = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 21
        )
        MISSING_PROTOCOL_IN_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 22
        )
        INVALID_PROTOCOL_IN_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 23
        )
        MALFORMED_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 24
        )
        MISSING_HOST_IN_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 25
        )
        INVALID_TLD_IN_FINAL_MOBILE_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 26
        )
        INVALID_FINAL_APP_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 27)
        INVALID_TAG_IN_FINAL_APP_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 28
        )
        REDUNDANT_NESTED_FINAL_APP_URL_TAG = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 29
        )
        MULTIPLE_APP_URLS_FOR_OSTYPE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 30
        )
        INVALID_OSTYPE = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 31)
        INVALID_PROTOCOL_FOR_APP_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 32
        )
        INVALID_PACKAGE_ID_FOR_APP_URL = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 33
        )
        URL_CUSTOM_PARAMETERS_COUNT_EXCEEDS_LIMIT = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 34
        )
        INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_KEY = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 39
        )
        INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_VALUE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 40
        )
        INVALID_TAG_IN_URL_CUSTOM_PARAMETER_VALUE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 41
        )
        REDUNDANT_NESTED_URL_CUSTOM_PARAMETER_TAG = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 42
        )
        MISSING_PROTOCOL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 43)
        INVALID_PROTOCOL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 52)
        INVALID_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 44)
        DESTINATION_URL_DEPRECATED = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 45
        )
        INVALID_TAG_IN_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 46)
        MISSING_URL_TAG = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 47)
        DUPLICATE_URL_ID = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 48)
        INVALID_URL_ID = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 49)
        FINAL_URL_SUFFIX_MALFORMED = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 50
        )
        INVALID_TAG_IN_FINAL_URL_SUFFIX = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 51
        )
        INVALID_TOP_LEVEL_DOMAIN = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 53
        )
        MALFORMED_TOP_LEVEL_DOMAIN = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 54
        )
        MALFORMED_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 55)
        MISSING_HOST = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 56)
        NULL_CUSTOM_PARAMETER_VALUE = typing___cast(
            UrlFieldErrorEnum.UrlFieldErrorValue, 57
        )
    UNSPECIFIED = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 0)
    UNKNOWN = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 1)
    INVALID_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 2
    )
    INVALID_TAG_IN_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 3
    )
    MISSING_TRACKING_URL_TEMPLATE_TAG = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 4
    )
    MISSING_PROTOCOL_IN_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 5
    )
    INVALID_PROTOCOL_IN_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 6
    )
    MALFORMED_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 7
    )
    MISSING_HOST_IN_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 8
    )
    INVALID_TLD_IN_TRACKING_URL_TEMPLATE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 9
    )
    REDUNDANT_NESTED_TRACKING_URL_TEMPLATE_TAG = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 10
    )
    INVALID_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 11)
    INVALID_TAG_IN_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 12)
    REDUNDANT_NESTED_FINAL_URL_TAG = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 13
    )
    MISSING_PROTOCOL_IN_FINAL_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 14
    )
    INVALID_PROTOCOL_IN_FINAL_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 15
    )
    MALFORMED_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 16)
    MISSING_HOST_IN_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 17)
    INVALID_TLD_IN_FINAL_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 18)
    INVALID_FINAL_MOBILE_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 19)
    INVALID_TAG_IN_FINAL_MOBILE_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 20
    )
    REDUNDANT_NESTED_FINAL_MOBILE_URL_TAG = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 21
    )
    MISSING_PROTOCOL_IN_FINAL_MOBILE_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 22
    )
    INVALID_PROTOCOL_IN_FINAL_MOBILE_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 23
    )
    MALFORMED_FINAL_MOBILE_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 24)
    MISSING_HOST_IN_FINAL_MOBILE_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 25
    )
    INVALID_TLD_IN_FINAL_MOBILE_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 26
    )
    INVALID_FINAL_APP_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 27)
    INVALID_TAG_IN_FINAL_APP_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 28
    )
    REDUNDANT_NESTED_FINAL_APP_URL_TAG = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 29
    )
    MULTIPLE_APP_URLS_FOR_OSTYPE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 30
    )
    INVALID_OSTYPE = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 31)
    INVALID_PROTOCOL_FOR_APP_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 32
    )
    INVALID_PACKAGE_ID_FOR_APP_URL = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 33
    )
    URL_CUSTOM_PARAMETERS_COUNT_EXCEEDS_LIMIT = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 34
    )
    INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_KEY = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 39
    )
    INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_VALUE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 40
    )
    INVALID_TAG_IN_URL_CUSTOM_PARAMETER_VALUE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 41
    )
    REDUNDANT_NESTED_URL_CUSTOM_PARAMETER_TAG = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 42
    )
    MISSING_PROTOCOL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 43)
    INVALID_PROTOCOL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 52)
    INVALID_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 44)
    DESTINATION_URL_DEPRECATED = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 45)
    INVALID_TAG_IN_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 46)
    MISSING_URL_TAG = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 47)
    DUPLICATE_URL_ID = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 48)
    INVALID_URL_ID = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 49)
    FINAL_URL_SUFFIX_MALFORMED = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 50)
    INVALID_TAG_IN_FINAL_URL_SUFFIX = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 51
    )
    INVALID_TOP_LEVEL_DOMAIN = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 53)
    MALFORMED_TOP_LEVEL_DOMAIN = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 54)
    MALFORMED_URL = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 55)
    MISSING_HOST = typing___cast(UrlFieldErrorEnum.UrlFieldErrorValue, 56)
    NULL_CUSTOM_PARAMETER_VALUE = typing___cast(
        UrlFieldErrorEnum.UrlFieldErrorValue, 57
    )
    type___UrlFieldError = UrlFieldError
    def __init__(self,) -> None: ...

type___UrlFieldErrorEnum = UrlFieldErrorEnum
