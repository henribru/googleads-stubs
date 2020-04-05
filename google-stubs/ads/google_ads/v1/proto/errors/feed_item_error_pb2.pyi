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

class FeedItemErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedItemError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "FeedItemErrorEnum.FeedItemError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["FeedItemErrorEnum.FeedItemError"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "FeedItemErrorEnum.FeedItemError"]
        ]: ...
        UNSPECIFIED = typing___cast("FeedItemErrorEnum.FeedItemError", 0)
        UNKNOWN = typing___cast("FeedItemErrorEnum.FeedItemError", 1)
        CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING = typing___cast(
            "FeedItemErrorEnum.FeedItemError", 2
        )
        CANNOT_OPERATE_ON_REMOVED_FEED_ITEM = typing___cast(
            "FeedItemErrorEnum.FeedItemError", 3
        )
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE = typing___cast(
            "FeedItemErrorEnum.FeedItemError", 4
        )
        KEY_ATTRIBUTES_NOT_FOUND = typing___cast("FeedItemErrorEnum.FeedItemError", 5)
        INVALID_URL = typing___cast("FeedItemErrorEnum.FeedItemError", 6)
        MISSING_KEY_ATTRIBUTES = typing___cast("FeedItemErrorEnum.FeedItemError", 7)
        KEY_ATTRIBUTES_NOT_UNIQUE = typing___cast("FeedItemErrorEnum.FeedItemError", 8)
        CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE = typing___cast(
            "FeedItemErrorEnum.FeedItemError", 9
        )
        SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE = typing___cast(
            "FeedItemErrorEnum.FeedItemError", 10
        )
    UNSPECIFIED = typing___cast("FeedItemErrorEnum.FeedItemError", 0)
    UNKNOWN = typing___cast("FeedItemErrorEnum.FeedItemError", 1)
    CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING = typing___cast(
        "FeedItemErrorEnum.FeedItemError", 2
    )
    CANNOT_OPERATE_ON_REMOVED_FEED_ITEM = typing___cast(
        "FeedItemErrorEnum.FeedItemError", 3
    )
    DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE = typing___cast(
        "FeedItemErrorEnum.FeedItemError", 4
    )
    KEY_ATTRIBUTES_NOT_FOUND = typing___cast("FeedItemErrorEnum.FeedItemError", 5)
    INVALID_URL = typing___cast("FeedItemErrorEnum.FeedItemError", 6)
    MISSING_KEY_ATTRIBUTES = typing___cast("FeedItemErrorEnum.FeedItemError", 7)
    KEY_ATTRIBUTES_NOT_UNIQUE = typing___cast("FeedItemErrorEnum.FeedItemError", 8)
    CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE = typing___cast(
        "FeedItemErrorEnum.FeedItemError", 9
    )
    SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE = typing___cast(
        "FeedItemErrorEnum.FeedItemError", 10
    )
    global___FeedItemError = FeedItemError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItemErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___FeedItemErrorEnum = FeedItemErrorEnum
