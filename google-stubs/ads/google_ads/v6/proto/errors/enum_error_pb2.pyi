# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class EnumErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    EnumErrorValue = typing___NewType("EnumErrorValue", builtin___int)
    type___EnumErrorValue = EnumErrorValue
    EnumError: _EnumError
    class _EnumError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            EnumErrorEnum.EnumErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(EnumErrorEnum.EnumErrorValue, 0)
        UNKNOWN = typing___cast(EnumErrorEnum.EnumErrorValue, 1)
        ENUM_VALUE_NOT_PERMITTED = typing___cast(EnumErrorEnum.EnumErrorValue, 3)
    UNSPECIFIED = typing___cast(EnumErrorEnum.EnumErrorValue, 0)
    UNKNOWN = typing___cast(EnumErrorEnum.EnumErrorValue, 1)
    ENUM_VALUE_NOT_PERMITTED = typing___cast(EnumErrorEnum.EnumErrorValue, 3)
    type___EnumError = EnumError
    def __init__(self,) -> None: ...

type___EnumErrorEnum = EnumErrorEnum