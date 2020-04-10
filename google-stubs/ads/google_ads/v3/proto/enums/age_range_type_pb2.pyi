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

class AgeRangeTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AgeRangeType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "AgeRangeTypeEnum.AgeRangeType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["AgeRangeTypeEnum.AgeRangeType"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "AgeRangeTypeEnum.AgeRangeType"]
        ]: ...
        UNSPECIFIED = typing___cast("AgeRangeTypeEnum.AgeRangeType", 0)
        UNKNOWN = typing___cast("AgeRangeTypeEnum.AgeRangeType", 1)
        AGE_RANGE_18_24 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503001)
        AGE_RANGE_25_34 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503002)
        AGE_RANGE_35_44 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503003)
        AGE_RANGE_45_54 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503004)
        AGE_RANGE_55_64 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503005)
        AGE_RANGE_65_UP = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503006)
        AGE_RANGE_UNDETERMINED = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503999)
    UNSPECIFIED = typing___cast("AgeRangeTypeEnum.AgeRangeType", 0)
    UNKNOWN = typing___cast("AgeRangeTypeEnum.AgeRangeType", 1)
    AGE_RANGE_18_24 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503001)
    AGE_RANGE_25_34 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503002)
    AGE_RANGE_35_44 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503003)
    AGE_RANGE_45_54 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503004)
    AGE_RANGE_55_64 = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503005)
    AGE_RANGE_65_UP = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503006)
    AGE_RANGE_UNDETERMINED = typing___cast("AgeRangeTypeEnum.AgeRangeType", 503999)
    global___AgeRangeType = AgeRangeType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AgeRangeTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AgeRangeTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___AgeRangeTypeEnum = AgeRangeTypeEnum