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

class FeedItemValidationStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedItemValidationStatusValue = typing___NewType(
        "FeedItemValidationStatusValue", builtin___int
    )
    type___FeedItemValidationStatusValue = FeedItemValidationStatusValue
    FeedItemValidationStatus: _FeedItemValidationStatus
    class _FeedItemValidationStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedItemValidationStatusEnum.FeedItemValidationStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 0
        )
        UNKNOWN = typing___cast(
            FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 1
        )
        PENDING = typing___cast(
            FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 2
        )
        INVALID = typing___cast(
            FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 3
        )
        VALID = typing___cast(
            FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 4
        )
    UNSPECIFIED = typing___cast(
        FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 0
    )
    UNKNOWN = typing___cast(
        FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 1
    )
    PENDING = typing___cast(
        FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 2
    )
    INVALID = typing___cast(
        FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 3
    )
    VALID = typing___cast(FeedItemValidationStatusEnum.FeedItemValidationStatusValue, 4)
    type___FeedItemValidationStatus = FeedItemValidationStatus
    def __init__(self,) -> None: ...

type___FeedItemValidationStatusEnum = FeedItemValidationStatusEnum
