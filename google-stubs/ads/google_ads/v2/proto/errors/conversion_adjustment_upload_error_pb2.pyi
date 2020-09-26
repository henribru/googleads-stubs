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

class ConversionAdjustmentUploadErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConversionAdjustmentUploadErrorValue = typing___NewType(
        "ConversionAdjustmentUploadErrorValue", builtin___int
    )
    type___ConversionAdjustmentUploadErrorValue = ConversionAdjustmentUploadErrorValue
    ConversionAdjustmentUploadError: _ConversionAdjustmentUploadError
    class _ConversionAdjustmentUploadError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 0
        )
        UNKNOWN = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 1
        )
        TOO_RECENT_CONVERSION_ACTION = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 2
        )
        INVALID_CONVERSION_ACTION = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 3
        )
        CONVERSION_ALREADY_RETRACTED = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 4
        )
        CONVERSION_NOT_FOUND = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 5
        )
        CONVERSION_EXPIRED = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 6
        )
        ADJUSTMENT_PRECEDES_CONVERSION = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 7
        )
        MORE_RECENT_RESTATEMENT_FOUND = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 8
        )
        TOO_RECENT_CONVERSION = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 9
        )
        CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE = typing___cast(
            ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 10
        )
    UNSPECIFIED = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 0
    )
    UNKNOWN = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 1
    )
    TOO_RECENT_CONVERSION_ACTION = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 2
    )
    INVALID_CONVERSION_ACTION = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 3
    )
    CONVERSION_ALREADY_RETRACTED = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 4
    )
    CONVERSION_NOT_FOUND = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 5
    )
    CONVERSION_EXPIRED = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 6
    )
    ADJUSTMENT_PRECEDES_CONVERSION = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 7
    )
    MORE_RECENT_RESTATEMENT_FOUND = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 8
    )
    TOO_RECENT_CONVERSION = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 9
    )
    CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE = typing___cast(
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorValue, 10
    )
    type___ConversionAdjustmentUploadError = ConversionAdjustmentUploadError
    def __init__(self,) -> None: ...

type___ConversionAdjustmentUploadErrorEnum = ConversionAdjustmentUploadErrorEnum
