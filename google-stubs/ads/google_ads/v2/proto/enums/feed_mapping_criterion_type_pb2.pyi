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

class FeedMappingCriterionTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedMappingCriterionTypeValue = typing___NewType(
        "FeedMappingCriterionTypeValue", builtin___int
    )
    type___FeedMappingCriterionTypeValue = FeedMappingCriterionTypeValue
    FeedMappingCriterionType: _FeedMappingCriterionType
    class _FeedMappingCriterionType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 0
        )
        UNKNOWN = typing___cast(
            FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 1
        )
        LOCATION_EXTENSION_TARGETING = typing___cast(
            FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 4
        )
        DSA_PAGE_FEED = typing___cast(
            FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 3
        )
    UNSPECIFIED = typing___cast(
        FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 0
    )
    UNKNOWN = typing___cast(
        FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 1
    )
    LOCATION_EXTENSION_TARGETING = typing___cast(
        FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 4
    )
    DSA_PAGE_FEED = typing___cast(
        FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue, 3
    )
    type___FeedMappingCriterionType = FeedMappingCriterionType
    def __init__(self,) -> None: ...

type___FeedMappingCriterionTypeEnum = FeedMappingCriterionTypeEnum
