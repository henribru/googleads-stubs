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

class FeedItemTargetStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedItemTargetStatusValue = typing___NewType(
        "FeedItemTargetStatusValue", builtin___int
    )
    type___FeedItemTargetStatusValue = FeedItemTargetStatusValue
    FeedItemTargetStatus: _FeedItemTargetStatus
    class _FeedItemTargetStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedItemTargetStatusEnum.FeedItemTargetStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 0
        )
        UNKNOWN = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 1)
        ENABLED = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 2)
        REMOVED = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 3)
    UNSPECIFIED = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 0)
    UNKNOWN = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 1)
    ENABLED = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 2)
    REMOVED = typing___cast(FeedItemTargetStatusEnum.FeedItemTargetStatusValue, 3)
    type___FeedItemTargetStatus = FeedItemTargetStatus
    def __init__(self,) -> None: ...

type___FeedItemTargetStatusEnum = FeedItemTargetStatusEnum
