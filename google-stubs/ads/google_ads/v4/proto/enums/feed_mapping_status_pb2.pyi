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

class FeedMappingStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedMappingStatusValue = typing___NewType("FeedMappingStatusValue", builtin___int)
    type___FeedMappingStatusValue = FeedMappingStatusValue
    FeedMappingStatus: _FeedMappingStatus
    class _FeedMappingStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedMappingStatusEnum.FeedMappingStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 0)
        UNKNOWN = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 1)
        ENABLED = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 2)
        REMOVED = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 3)
    UNSPECIFIED = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 0)
    UNKNOWN = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 1)
    ENABLED = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 2)
    REMOVED = typing___cast(FeedMappingStatusEnum.FeedMappingStatusValue, 3)
    type___FeedMappingStatus = FeedMappingStatus
    def __init__(self,) -> None: ...

type___FeedMappingStatusEnum = FeedMappingStatusEnum