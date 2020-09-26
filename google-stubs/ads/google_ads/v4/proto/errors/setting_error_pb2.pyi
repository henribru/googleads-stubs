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

class SettingErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SettingErrorValue = typing___NewType("SettingErrorValue", builtin___int)
    type___SettingErrorValue = SettingErrorValue
    SettingError: _SettingError
    class _SettingError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SettingErrorEnum.SettingErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(SettingErrorEnum.SettingErrorValue, 0)
        UNKNOWN = typing___cast(SettingErrorEnum.SettingErrorValue, 1)
        SETTING_TYPE_IS_NOT_AVAILABLE = typing___cast(
            SettingErrorEnum.SettingErrorValue, 3
        )
        SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN = typing___cast(
            SettingErrorEnum.SettingErrorValue, 4
        )
        TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP = typing___cast(
            SettingErrorEnum.SettingErrorValue, 5
        )
        TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL = typing___cast(
            SettingErrorEnum.SettingErrorValue, 6
        )
        TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP = typing___cast(
            SettingErrorEnum.SettingErrorValue, 7
        )
        DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT = typing___cast(
            SettingErrorEnum.SettingErrorValue, 8
        )
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME = typing___cast(
            SettingErrorEnum.SettingErrorValue, 9
        )
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME = typing___cast(
            SettingErrorEnum.SettingErrorValue, 10
        )
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE = typing___cast(
            SettingErrorEnum.SettingErrorValue, 11
        )
        TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN = typing___cast(
            SettingErrorEnum.SettingErrorValue, 12
        )
        SETTING_VALUE_NOT_COMPATIBLE_WITH_CAMPAIGN = typing___cast(
            SettingErrorEnum.SettingErrorValue, 20
        )
    UNSPECIFIED = typing___cast(SettingErrorEnum.SettingErrorValue, 0)
    UNKNOWN = typing___cast(SettingErrorEnum.SettingErrorValue, 1)
    SETTING_TYPE_IS_NOT_AVAILABLE = typing___cast(SettingErrorEnum.SettingErrorValue, 3)
    SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN = typing___cast(
        SettingErrorEnum.SettingErrorValue, 4
    )
    TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP = typing___cast(
        SettingErrorEnum.SettingErrorValue, 5
    )
    TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL = typing___cast(
        SettingErrorEnum.SettingErrorValue, 6
    )
    TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP = typing___cast(
        SettingErrorEnum.SettingErrorValue, 7
    )
    DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT = typing___cast(
        SettingErrorEnum.SettingErrorValue, 8
    )
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME = typing___cast(
        SettingErrorEnum.SettingErrorValue, 9
    )
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME = typing___cast(
        SettingErrorEnum.SettingErrorValue, 10
    )
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE = typing___cast(
        SettingErrorEnum.SettingErrorValue, 11
    )
    TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN = typing___cast(
        SettingErrorEnum.SettingErrorValue, 12
    )
    SETTING_VALUE_NOT_COMPATIBLE_WITH_CAMPAIGN = typing___cast(
        SettingErrorEnum.SettingErrorValue, 20
    )
    type___SettingError = SettingError
    def __init__(self,) -> None: ...

type___SettingErrorEnum = SettingErrorEnum
