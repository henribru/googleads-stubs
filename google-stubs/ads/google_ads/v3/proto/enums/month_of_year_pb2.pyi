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

class MonthOfYearEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MonthOfYear(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "MonthOfYearEnum.MonthOfYear": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["MonthOfYearEnum.MonthOfYear"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "MonthOfYearEnum.MonthOfYear"]
        ]: ...
        UNSPECIFIED = typing___cast("MonthOfYearEnum.MonthOfYear", 0)
        UNKNOWN = typing___cast("MonthOfYearEnum.MonthOfYear", 1)
        JANUARY = typing___cast("MonthOfYearEnum.MonthOfYear", 2)
        FEBRUARY = typing___cast("MonthOfYearEnum.MonthOfYear", 3)
        MARCH = typing___cast("MonthOfYearEnum.MonthOfYear", 4)
        APRIL = typing___cast("MonthOfYearEnum.MonthOfYear", 5)
        MAY = typing___cast("MonthOfYearEnum.MonthOfYear", 6)
        JUNE = typing___cast("MonthOfYearEnum.MonthOfYear", 7)
        JULY = typing___cast("MonthOfYearEnum.MonthOfYear", 8)
        AUGUST = typing___cast("MonthOfYearEnum.MonthOfYear", 9)
        SEPTEMBER = typing___cast("MonthOfYearEnum.MonthOfYear", 10)
        OCTOBER = typing___cast("MonthOfYearEnum.MonthOfYear", 11)
        NOVEMBER = typing___cast("MonthOfYearEnum.MonthOfYear", 12)
        DECEMBER = typing___cast("MonthOfYearEnum.MonthOfYear", 13)
    UNSPECIFIED = typing___cast("MonthOfYearEnum.MonthOfYear", 0)
    UNKNOWN = typing___cast("MonthOfYearEnum.MonthOfYear", 1)
    JANUARY = typing___cast("MonthOfYearEnum.MonthOfYear", 2)
    FEBRUARY = typing___cast("MonthOfYearEnum.MonthOfYear", 3)
    MARCH = typing___cast("MonthOfYearEnum.MonthOfYear", 4)
    APRIL = typing___cast("MonthOfYearEnum.MonthOfYear", 5)
    MAY = typing___cast("MonthOfYearEnum.MonthOfYear", 6)
    JUNE = typing___cast("MonthOfYearEnum.MonthOfYear", 7)
    JULY = typing___cast("MonthOfYearEnum.MonthOfYear", 8)
    AUGUST = typing___cast("MonthOfYearEnum.MonthOfYear", 9)
    SEPTEMBER = typing___cast("MonthOfYearEnum.MonthOfYear", 10)
    OCTOBER = typing___cast("MonthOfYearEnum.MonthOfYear", 11)
    NOVEMBER = typing___cast("MonthOfYearEnum.MonthOfYear", 12)
    DECEMBER = typing___cast("MonthOfYearEnum.MonthOfYear", 13)
    global___MonthOfYear = MonthOfYear
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MonthOfYearEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MonthOfYearEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___MonthOfYearEnum = MonthOfYearEnum