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

class GoogleAdsFieldDataTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class GoogleAdsFieldDataType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls
        ) -> typing___List["GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 0
        )
        UNKNOWN = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 1)
        BOOLEAN = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 2)
        DATE = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 3)
        DOUBLE = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 4)
        ENUM = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 5)
        FLOAT = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 6)
        INT32 = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 7)
        INT64 = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 8)
        MESSAGE = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 9)
        RESOURCE_NAME = typing___cast(
            "GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 10
        )
        STRING = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 11)
        UINT64 = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 12)
    UNSPECIFIED = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 0)
    UNKNOWN = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 1)
    BOOLEAN = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 2)
    DATE = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 3)
    DOUBLE = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 4)
    ENUM = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 5)
    FLOAT = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 6)
    INT32 = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 7)
    INT64 = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 8)
    MESSAGE = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 9)
    RESOURCE_NAME = typing___cast(
        "GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 10
    )
    STRING = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 11)
    UINT64 = typing___cast("GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType", 12)
    global___GoogleAdsFieldDataType = GoogleAdsFieldDataType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GoogleAdsFieldDataTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GoogleAdsFieldDataTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___GoogleAdsFieldDataTypeEnum = GoogleAdsFieldDataTypeEnum
