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

class MutateJobErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MutateJobErrorValue = typing___NewType("MutateJobErrorValue", builtin___int)
    type___MutateJobErrorValue = MutateJobErrorValue
    MutateJobError: _MutateJobError
    class _MutateJobError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MutateJobErrorEnum.MutateJobErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 0)
        UNKNOWN = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 1)
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING = typing___cast(
            MutateJobErrorEnum.MutateJobErrorValue, 2
        )
        EMPTY_OPERATIONS = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 3)
        INVALID_SEQUENCE_TOKEN = typing___cast(
            MutateJobErrorEnum.MutateJobErrorValue, 4
        )
        RESULTS_NOT_READY = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 5)
        INVALID_PAGE_SIZE = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 6)
    UNSPECIFIED = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 0)
    UNKNOWN = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 1)
    CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING = typing___cast(
        MutateJobErrorEnum.MutateJobErrorValue, 2
    )
    EMPTY_OPERATIONS = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 3)
    INVALID_SEQUENCE_TOKEN = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 4)
    RESULTS_NOT_READY = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 5)
    INVALID_PAGE_SIZE = typing___cast(MutateJobErrorEnum.MutateJobErrorValue, 6)
    type___MutateJobError = MutateJobError
    def __init__(self,) -> None: ...

type___MutateJobErrorEnum = MutateJobErrorEnum
