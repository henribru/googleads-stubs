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

class BudgetStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    BudgetStatusValue = typing___NewType("BudgetStatusValue", builtin___int)
    type___BudgetStatusValue = BudgetStatusValue
    BudgetStatus: _BudgetStatus
    class _BudgetStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            BudgetStatusEnum.BudgetStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(BudgetStatusEnum.BudgetStatusValue, 0)
        UNKNOWN = typing___cast(BudgetStatusEnum.BudgetStatusValue, 1)
        ENABLED = typing___cast(BudgetStatusEnum.BudgetStatusValue, 2)
        REMOVED = typing___cast(BudgetStatusEnum.BudgetStatusValue, 3)
    UNSPECIFIED = typing___cast(BudgetStatusEnum.BudgetStatusValue, 0)
    UNKNOWN = typing___cast(BudgetStatusEnum.BudgetStatusValue, 1)
    ENABLED = typing___cast(BudgetStatusEnum.BudgetStatusValue, 2)
    REMOVED = typing___cast(BudgetStatusEnum.BudgetStatusValue, 3)
    type___BudgetStatus = BudgetStatus
    def __init__(self,) -> None: ...

type___BudgetStatusEnum = BudgetStatusEnum
