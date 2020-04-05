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

class FeedAttributeTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedAttributeType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "FeedAttributeTypeEnum.FeedAttributeType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["FeedAttributeTypeEnum.FeedAttributeType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "FeedAttributeTypeEnum.FeedAttributeType"]
        ]: ...
        UNSPECIFIED = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 0)
        UNKNOWN = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 1)
        INT64 = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 2)
        DOUBLE = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 3)
        STRING = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 4)
        BOOLEAN = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 5)
        URL = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 6)
        DATE_TIME = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 7)
        INT64_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 8)
        DOUBLE_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 9)
        STRING_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 10)
        BOOLEAN_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 11)
        URL_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 12)
        DATE_TIME_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 13)
        PRICE = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 14)
    UNSPECIFIED = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 0)
    UNKNOWN = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 1)
    INT64 = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 2)
    DOUBLE = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 3)
    STRING = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 4)
    BOOLEAN = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 5)
    URL = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 6)
    DATE_TIME = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 7)
    INT64_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 8)
    DOUBLE_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 9)
    STRING_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 10)
    BOOLEAN_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 11)
    URL_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 12)
    DATE_TIME_LIST = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 13)
    PRICE = typing___cast("FeedAttributeTypeEnum.FeedAttributeType", 14)
    global___FeedAttributeType = FeedAttributeType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedAttributeTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedAttributeTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___FeedAttributeTypeEnum = FeedAttributeTypeEnum
