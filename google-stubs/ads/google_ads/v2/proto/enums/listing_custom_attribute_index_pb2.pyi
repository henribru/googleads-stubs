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

class ListingCustomAttributeIndexEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ListingCustomAttributeIndexValue = typing___NewType(
        "ListingCustomAttributeIndexValue", builtin___int
    )
    type___ListingCustomAttributeIndexValue = ListingCustomAttributeIndexValue
    ListingCustomAttributeIndex: _ListingCustomAttributeIndex
    class _ListingCustomAttributeIndex(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 0
        )
        UNKNOWN = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 1
        )
        INDEX0 = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 7
        )
        INDEX1 = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 8
        )
        INDEX2 = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 9
        )
        INDEX3 = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 10
        )
        INDEX4 = typing___cast(
            ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 11
        )
    UNSPECIFIED = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 0
    )
    UNKNOWN = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 1
    )
    INDEX0 = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 7
    )
    INDEX1 = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 8
    )
    INDEX2 = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 9
    )
    INDEX3 = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 10
    )
    INDEX4 = typing___cast(
        ListingCustomAttributeIndexEnum.ListingCustomAttributeIndexValue, 11
    )
    type___ListingCustomAttributeIndex = ListingCustomAttributeIndex
    def __init__(self,) -> None: ...

type___ListingCustomAttributeIndexEnum = ListingCustomAttributeIndexEnum
