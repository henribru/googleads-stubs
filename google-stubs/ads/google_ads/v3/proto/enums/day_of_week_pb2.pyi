# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class DayOfWeekEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    DayOfWeekValue = typing___NewType("DayOfWeekValue", builtin___int)
    type___DayOfWeekValue = DayOfWeekValue
    DayOfWeek: _DayOfWeek
    class _DayOfWeek(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            DayOfWeekEnum.DayOfWeekValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(DayOfWeekEnum.DayOfWeekValue, 0)
        UNKNOWN = typing___cast(DayOfWeekEnum.DayOfWeekValue, 1)
        MONDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 2)
        TUESDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 3)
        WEDNESDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 4)
        THURSDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 5)
        FRIDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 6)
        SATURDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 7)
        SUNDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 8)
    UNSPECIFIED = typing___cast(DayOfWeekEnum.DayOfWeekValue, 0)
    UNKNOWN = typing___cast(DayOfWeekEnum.DayOfWeekValue, 1)
    MONDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 2)
    TUESDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 3)
    WEDNESDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 4)
    THURSDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 5)
    FRIDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 6)
    SATURDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 7)
    SUNDAY = typing___cast(DayOfWeekEnum.DayOfWeekValue, 8)
    type___DayOfWeek = DayOfWeek
    def __init__(self,) -> None: ...

type___DayOfWeekEnum = DayOfWeekEnum
