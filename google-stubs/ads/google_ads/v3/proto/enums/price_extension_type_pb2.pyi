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

class PriceExtensionTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    PriceExtensionTypeValue = typing___NewType("PriceExtensionTypeValue", builtin___int)
    type___PriceExtensionTypeValue = PriceExtensionTypeValue
    PriceExtensionType: _PriceExtensionType
    class _PriceExtensionType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            PriceExtensionTypeEnum.PriceExtensionTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 0)
        UNKNOWN = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 1)
        BRANDS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 2)
        EVENTS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 3)
        LOCATIONS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 4)
        NEIGHBORHOODS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 5)
        PRODUCT_CATEGORIES = typing___cast(
            PriceExtensionTypeEnum.PriceExtensionTypeValue, 6
        )
        PRODUCT_TIERS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 7)
        SERVICES = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 8)
        SERVICE_CATEGORIES = typing___cast(
            PriceExtensionTypeEnum.PriceExtensionTypeValue, 9
        )
        SERVICE_TIERS = typing___cast(
            PriceExtensionTypeEnum.PriceExtensionTypeValue, 10
        )
    UNSPECIFIED = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 0)
    UNKNOWN = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 1)
    BRANDS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 2)
    EVENTS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 3)
    LOCATIONS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 4)
    NEIGHBORHOODS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 5)
    PRODUCT_CATEGORIES = typing___cast(
        PriceExtensionTypeEnum.PriceExtensionTypeValue, 6
    )
    PRODUCT_TIERS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 7)
    SERVICES = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 8)
    SERVICE_CATEGORIES = typing___cast(
        PriceExtensionTypeEnum.PriceExtensionTypeValue, 9
    )
    SERVICE_TIERS = typing___cast(PriceExtensionTypeEnum.PriceExtensionTypeValue, 10)
    type___PriceExtensionType = PriceExtensionType
    def __init__(self,) -> None: ...

type___PriceExtensionTypeEnum = PriceExtensionTypeEnum
