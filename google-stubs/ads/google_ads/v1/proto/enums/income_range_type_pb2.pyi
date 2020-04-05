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

class IncomeRangeTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class IncomeRangeType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "IncomeRangeTypeEnum.IncomeRangeType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["IncomeRangeTypeEnum.IncomeRangeType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "IncomeRangeTypeEnum.IncomeRangeType"]
        ]: ...
        UNSPECIFIED = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 0)
        UNKNOWN = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 1)
        INCOME_RANGE_0_50 = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510001)
        INCOME_RANGE_50_60 = typing___cast(
            "IncomeRangeTypeEnum.IncomeRangeType", 510002
        )
        INCOME_RANGE_60_70 = typing___cast(
            "IncomeRangeTypeEnum.IncomeRangeType", 510003
        )
        INCOME_RANGE_70_80 = typing___cast(
            "IncomeRangeTypeEnum.IncomeRangeType", 510004
        )
        INCOME_RANGE_80_90 = typing___cast(
            "IncomeRangeTypeEnum.IncomeRangeType", 510005
        )
        INCOME_RANGE_90_UP = typing___cast(
            "IncomeRangeTypeEnum.IncomeRangeType", 510006
        )
        INCOME_RANGE_UNDETERMINED = typing___cast(
            "IncomeRangeTypeEnum.IncomeRangeType", 510000
        )
    UNSPECIFIED = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 0)
    UNKNOWN = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 1)
    INCOME_RANGE_0_50 = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510001)
    INCOME_RANGE_50_60 = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510002)
    INCOME_RANGE_60_70 = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510003)
    INCOME_RANGE_70_80 = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510004)
    INCOME_RANGE_80_90 = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510005)
    INCOME_RANGE_90_UP = typing___cast("IncomeRangeTypeEnum.IncomeRangeType", 510006)
    INCOME_RANGE_UNDETERMINED = typing___cast(
        "IncomeRangeTypeEnum.IncomeRangeType", 510000
    )
    global___IncomeRangeType = IncomeRangeType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> IncomeRangeTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> IncomeRangeTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___IncomeRangeTypeEnum = IncomeRangeTypeEnum
