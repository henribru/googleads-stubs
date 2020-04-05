# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

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


class TargetingDimensionEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TargetingDimension(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'TargetingDimensionEnum.TargetingDimension': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['TargetingDimensionEnum.TargetingDimension']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'TargetingDimensionEnum.TargetingDimension']]: ...
        UNSPECIFIED = typing___cast('TargetingDimensionEnum.TargetingDimension', 0)
        UNKNOWN = typing___cast('TargetingDimensionEnum.TargetingDimension', 1)
        KEYWORD = typing___cast('TargetingDimensionEnum.TargetingDimension', 2)
        AUDIENCE = typing___cast('TargetingDimensionEnum.TargetingDimension', 3)
        TOPIC = typing___cast('TargetingDimensionEnum.TargetingDimension', 4)
        GENDER = typing___cast('TargetingDimensionEnum.TargetingDimension', 5)
        AGE_RANGE = typing___cast('TargetingDimensionEnum.TargetingDimension', 6)
        PLACEMENT = typing___cast('TargetingDimensionEnum.TargetingDimension', 7)
        PARENTAL_STATUS = typing___cast('TargetingDimensionEnum.TargetingDimension', 8)
        INCOME_RANGE = typing___cast('TargetingDimensionEnum.TargetingDimension', 9)
    UNSPECIFIED = typing___cast('TargetingDimensionEnum.TargetingDimension', 0)
    UNKNOWN = typing___cast('TargetingDimensionEnum.TargetingDimension', 1)
    KEYWORD = typing___cast('TargetingDimensionEnum.TargetingDimension', 2)
    AUDIENCE = typing___cast('TargetingDimensionEnum.TargetingDimension', 3)
    TOPIC = typing___cast('TargetingDimensionEnum.TargetingDimension', 4)
    GENDER = typing___cast('TargetingDimensionEnum.TargetingDimension', 5)
    AGE_RANGE = typing___cast('TargetingDimensionEnum.TargetingDimension', 6)
    PLACEMENT = typing___cast('TargetingDimensionEnum.TargetingDimension', 7)
    PARENTAL_STATUS = typing___cast('TargetingDimensionEnum.TargetingDimension', 8)
    INCOME_RANGE = typing___cast('TargetingDimensionEnum.TargetingDimension', 9)
    global___TargetingDimension = TargetingDimension


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetingDimensionEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetingDimensionEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___TargetingDimensionEnum = TargetingDimensionEnum
