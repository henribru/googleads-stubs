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

class IdErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    IdErrorValue = typing___NewType("IdErrorValue", builtin___int)
    type___IdErrorValue = IdErrorValue
    IdError: _IdError
    class _IdError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            IdErrorEnum.IdErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(IdErrorEnum.IdErrorValue, 0)
        UNKNOWN = typing___cast(IdErrorEnum.IdErrorValue, 1)
        NOT_FOUND = typing___cast(IdErrorEnum.IdErrorValue, 2)
    UNSPECIFIED = typing___cast(IdErrorEnum.IdErrorValue, 0)
    UNKNOWN = typing___cast(IdErrorEnum.IdErrorValue, 1)
    NOT_FOUND = typing___cast(IdErrorEnum.IdErrorValue, 2)
    type___IdError = IdError
    def __init__(self,) -> None: ...

type___IdErrorEnum = IdErrorEnum
