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

class FeedItemQualityApprovalStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedItemQualityApprovalStatusValue = typing___NewType(
        "FeedItemQualityApprovalStatusValue", builtin___int
    )
    type___FeedItemQualityApprovalStatusValue = FeedItemQualityApprovalStatusValue
    FeedItemQualityApprovalStatus: _FeedItemQualityApprovalStatus
    class _FeedItemQualityApprovalStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 0
        )
        UNKNOWN = typing___cast(
            FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 1
        )
        APPROVED = typing___cast(
            FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 2
        )
        DISAPPROVED = typing___cast(
            FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 3
        )
    UNSPECIFIED = typing___cast(
        FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 0
    )
    UNKNOWN = typing___cast(
        FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 1
    )
    APPROVED = typing___cast(
        FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 2
    )
    DISAPPROVED = typing___cast(
        FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusValue, 3
    )
    type___FeedItemQualityApprovalStatus = FeedItemQualityApprovalStatus
    def __init__(self,) -> None: ...

type___FeedItemQualityApprovalStatusEnum = FeedItemQualityApprovalStatusEnum
