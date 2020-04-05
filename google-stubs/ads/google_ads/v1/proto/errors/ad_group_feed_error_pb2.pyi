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

class AdGroupFeedErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AdGroupFeedError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "AdGroupFeedErrorEnum.AdGroupFeedError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["AdGroupFeedErrorEnum.AdGroupFeedError"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "AdGroupFeedErrorEnum.AdGroupFeedError"]
        ]: ...
        UNSPECIFIED = typing___cast("AdGroupFeedErrorEnum.AdGroupFeedError", 0)
        UNKNOWN = typing___cast("AdGroupFeedErrorEnum.AdGroupFeedError", 1)
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 2
        )
        CANNOT_CREATE_FOR_REMOVED_FEED = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 3
        )
        ADGROUP_FEED_ALREADY_EXISTS = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 4
        )
        CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 5
        )
        INVALID_PLACEHOLDER_TYPE = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 6
        )
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 7
        )
        NO_EXISTING_LOCATION_CUSTOMER_FEED = typing___cast(
            "AdGroupFeedErrorEnum.AdGroupFeedError", 8
        )
    UNSPECIFIED = typing___cast("AdGroupFeedErrorEnum.AdGroupFeedError", 0)
    UNKNOWN = typing___cast("AdGroupFeedErrorEnum.AdGroupFeedError", 1)
    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
        "AdGroupFeedErrorEnum.AdGroupFeedError", 2
    )
    CANNOT_CREATE_FOR_REMOVED_FEED = typing___cast(
        "AdGroupFeedErrorEnum.AdGroupFeedError", 3
    )
    ADGROUP_FEED_ALREADY_EXISTS = typing___cast(
        "AdGroupFeedErrorEnum.AdGroupFeedError", 4
    )
    CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED = typing___cast(
        "AdGroupFeedErrorEnum.AdGroupFeedError", 5
    )
    INVALID_PLACEHOLDER_TYPE = typing___cast("AdGroupFeedErrorEnum.AdGroupFeedError", 6)
    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = typing___cast(
        "AdGroupFeedErrorEnum.AdGroupFeedError", 7
    )
    NO_EXISTING_LOCATION_CUSTOMER_FEED = typing___cast(
        "AdGroupFeedErrorEnum.AdGroupFeedError", 8
    )
    global___AdGroupFeedError = AdGroupFeedError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AdGroupFeedErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AdGroupFeedErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___AdGroupFeedErrorEnum = AdGroupFeedErrorEnum
