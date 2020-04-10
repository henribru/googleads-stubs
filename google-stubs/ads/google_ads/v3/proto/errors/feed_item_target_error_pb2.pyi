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

class FeedItemTargetErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedItemTargetError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "FeedItemTargetErrorEnum.FeedItemTargetError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["FeedItemTargetErrorEnum.FeedItemTargetError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "FeedItemTargetErrorEnum.FeedItemTargetError"]
        ]: ...
        UNSPECIFIED = typing___cast("FeedItemTargetErrorEnum.FeedItemTargetError", 0)
        UNKNOWN = typing___cast("FeedItemTargetErrorEnum.FeedItemTargetError", 1)
        MUST_SET_TARGET_ONEOF_ON_CREATE = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 2
        )
        FEED_ITEM_TARGET_ALREADY_EXISTS = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 3
        )
        FEED_ITEM_SCHEDULES_CANNOT_OVERLAP = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 4
        )
        TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 5
        )
        TOO_MANY_SCHEDULES_PER_DAY = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 6
        )
        CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 7
        )
        DUPLICATE_AD_SCHEDULE = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 8
        )
        DUPLICATE_KEYWORD = typing___cast(
            "FeedItemTargetErrorEnum.FeedItemTargetError", 9
        )
    UNSPECIFIED = typing___cast("FeedItemTargetErrorEnum.FeedItemTargetError", 0)
    UNKNOWN = typing___cast("FeedItemTargetErrorEnum.FeedItemTargetError", 1)
    MUST_SET_TARGET_ONEOF_ON_CREATE = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 2
    )
    FEED_ITEM_TARGET_ALREADY_EXISTS = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 3
    )
    FEED_ITEM_SCHEDULES_CANNOT_OVERLAP = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 4
    )
    TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 5
    )
    TOO_MANY_SCHEDULES_PER_DAY = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 6
    )
    CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 7
    )
    DUPLICATE_AD_SCHEDULE = typing___cast(
        "FeedItemTargetErrorEnum.FeedItemTargetError", 8
    )
    DUPLICATE_KEYWORD = typing___cast("FeedItemTargetErrorEnum.FeedItemTargetError", 9)
    global___FeedItemTargetError = FeedItemTargetError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemTargetErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItemTargetErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___FeedItemTargetErrorEnum = FeedItemTargetErrorEnum