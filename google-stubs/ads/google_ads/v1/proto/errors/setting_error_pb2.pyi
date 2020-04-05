# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class SettingErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class SettingError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "SettingErrorEnum.SettingError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["SettingErrorEnum.SettingError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "SettingErrorEnum.SettingError"]
        ]: ...
        UNSPECIFIED = typing___cast("SettingErrorEnum.SettingError", 0)
        UNKNOWN = typing___cast("SettingErrorEnum.SettingError", 1)
        SETTING_TYPE_IS_NOT_AVAILABLE = typing___cast(
            "SettingErrorEnum.SettingError", 3
        )
        SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN = typing___cast(
            "SettingErrorEnum.SettingError", 4
        )
        TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP = typing___cast(
            "SettingErrorEnum.SettingError", 5
        )
        TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL = typing___cast(
            "SettingErrorEnum.SettingError", 6
        )
        TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP = typing___cast(
            "SettingErrorEnum.SettingError", 7
        )
        DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT = typing___cast(
            "SettingErrorEnum.SettingError", 8
        )
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME = typing___cast(
            "SettingErrorEnum.SettingError", 9
        )
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME = typing___cast(
            "SettingErrorEnum.SettingError", 10
        )
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE = typing___cast(
            "SettingErrorEnum.SettingError", 11
        )
        TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN = typing___cast(
            "SettingErrorEnum.SettingError", 12
        )
        UNIVERSAL_APP_CAMPAIGN_SETTING_DUPLICATE_DESCRIPTION = typing___cast(
            "SettingErrorEnum.SettingError", 13
        )
        UNIVERSAL_APP_CAMPAIGN_SETTING_DESCRIPTION_LINE_WIDTH_TOO_LONG = typing___cast(
            "SettingErrorEnum.SettingError", 14
        )
        UNIVERSAL_APP_CAMPAIGN_SETTING_APP_ID_CANNOT_BE_MODIFIED = typing___cast(
            "SettingErrorEnum.SettingError", 15
        )
        TOO_MANY_YOUTUBE_MEDIA_IDS_IN_UNIVERSAL_APP_CAMPAIGN = typing___cast(
            "SettingErrorEnum.SettingError", 16
        )
        TOO_MANY_IMAGE_MEDIA_IDS_IN_UNIVERSAL_APP_CAMPAIGN = typing___cast(
            "SettingErrorEnum.SettingError", 17
        )
        MEDIA_INCOMPATIBLE_FOR_UNIVERSAL_APP_CAMPAIGN = typing___cast(
            "SettingErrorEnum.SettingError", 18
        )
        TOO_MANY_EXCLAMATION_MARKS = typing___cast("SettingErrorEnum.SettingError", 19)
    UNSPECIFIED = typing___cast("SettingErrorEnum.SettingError", 0)
    UNKNOWN = typing___cast("SettingErrorEnum.SettingError", 1)
    SETTING_TYPE_IS_NOT_AVAILABLE = typing___cast("SettingErrorEnum.SettingError", 3)
    SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN = typing___cast(
        "SettingErrorEnum.SettingError", 4
    )
    TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP = typing___cast(
        "SettingErrorEnum.SettingError", 5
    )
    TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL = typing___cast(
        "SettingErrorEnum.SettingError", 6
    )
    TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP = typing___cast(
        "SettingErrorEnum.SettingError", 7
    )
    DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT = typing___cast(
        "SettingErrorEnum.SettingError", 8
    )
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME = typing___cast(
        "SettingErrorEnum.SettingError", 9
    )
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME = typing___cast(
        "SettingErrorEnum.SettingError", 10
    )
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE = typing___cast(
        "SettingErrorEnum.SettingError", 11
    )
    TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN = typing___cast(
        "SettingErrorEnum.SettingError", 12
    )
    UNIVERSAL_APP_CAMPAIGN_SETTING_DUPLICATE_DESCRIPTION = typing___cast(
        "SettingErrorEnum.SettingError", 13
    )
    UNIVERSAL_APP_CAMPAIGN_SETTING_DESCRIPTION_LINE_WIDTH_TOO_LONG = typing___cast(
        "SettingErrorEnum.SettingError", 14
    )
    UNIVERSAL_APP_CAMPAIGN_SETTING_APP_ID_CANNOT_BE_MODIFIED = typing___cast(
        "SettingErrorEnum.SettingError", 15
    )
    TOO_MANY_YOUTUBE_MEDIA_IDS_IN_UNIVERSAL_APP_CAMPAIGN = typing___cast(
        "SettingErrorEnum.SettingError", 16
    )
    TOO_MANY_IMAGE_MEDIA_IDS_IN_UNIVERSAL_APP_CAMPAIGN = typing___cast(
        "SettingErrorEnum.SettingError", 17
    )
    MEDIA_INCOMPATIBLE_FOR_UNIVERSAL_APP_CAMPAIGN = typing___cast(
        "SettingErrorEnum.SettingError", 18
    )
    TOO_MANY_EXCLAMATION_MARKS = typing___cast("SettingErrorEnum.SettingError", 19)
    global___SettingError = SettingError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SettingErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> SettingErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___SettingErrorEnum = SettingErrorEnum
