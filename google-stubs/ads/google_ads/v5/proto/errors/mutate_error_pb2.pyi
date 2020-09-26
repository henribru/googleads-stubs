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

class MutateErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MutateErrorValue = typing___NewType("MutateErrorValue", builtin___int)
    type___MutateErrorValue = MutateErrorValue
    MutateError: _MutateError
    class _MutateError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MutateErrorEnum.MutateErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(MutateErrorEnum.MutateErrorValue, 0)
        UNKNOWN = typing___cast(MutateErrorEnum.MutateErrorValue, 1)
        RESOURCE_NOT_FOUND = typing___cast(MutateErrorEnum.MutateErrorValue, 3)
        ID_EXISTS_IN_MULTIPLE_MUTATES = typing___cast(
            MutateErrorEnum.MutateErrorValue, 7
        )
        INCONSISTENT_FIELD_VALUES = typing___cast(MutateErrorEnum.MutateErrorValue, 8)
        MUTATE_NOT_ALLOWED = typing___cast(MutateErrorEnum.MutateErrorValue, 9)
        RESOURCE_NOT_IN_GOOGLE_ADS = typing___cast(MutateErrorEnum.MutateErrorValue, 10)
        RESOURCE_ALREADY_EXISTS = typing___cast(MutateErrorEnum.MutateErrorValue, 11)
        RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY = typing___cast(
            MutateErrorEnum.MutateErrorValue, 12
        )
        RESOURCE_READ_ONLY = typing___cast(MutateErrorEnum.MutateErrorValue, 13)
    UNSPECIFIED = typing___cast(MutateErrorEnum.MutateErrorValue, 0)
    UNKNOWN = typing___cast(MutateErrorEnum.MutateErrorValue, 1)
    RESOURCE_NOT_FOUND = typing___cast(MutateErrorEnum.MutateErrorValue, 3)
    ID_EXISTS_IN_MULTIPLE_MUTATES = typing___cast(MutateErrorEnum.MutateErrorValue, 7)
    INCONSISTENT_FIELD_VALUES = typing___cast(MutateErrorEnum.MutateErrorValue, 8)
    MUTATE_NOT_ALLOWED = typing___cast(MutateErrorEnum.MutateErrorValue, 9)
    RESOURCE_NOT_IN_GOOGLE_ADS = typing___cast(MutateErrorEnum.MutateErrorValue, 10)
    RESOURCE_ALREADY_EXISTS = typing___cast(MutateErrorEnum.MutateErrorValue, 11)
    RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY = typing___cast(
        MutateErrorEnum.MutateErrorValue, 12
    )
    RESOURCE_READ_ONLY = typing___cast(MutateErrorEnum.MutateErrorValue, 13)
    type___MutateError = MutateError
    def __init__(self,) -> None: ...

type___MutateErrorEnum = MutateErrorEnum
