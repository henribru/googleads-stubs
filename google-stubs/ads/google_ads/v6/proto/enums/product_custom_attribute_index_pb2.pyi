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

class ProductCustomAttributeIndexEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ProductCustomAttributeIndexValue = typing___NewType(
        "ProductCustomAttributeIndexValue", builtin___int
    )
    type___ProductCustomAttributeIndexValue = ProductCustomAttributeIndexValue
    ProductCustomAttributeIndex: _ProductCustomAttributeIndex
    class _ProductCustomAttributeIndex(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 0
        )
        UNKNOWN = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 1
        )
        INDEX0 = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 7
        )
        INDEX1 = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 8
        )
        INDEX2 = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 9
        )
        INDEX3 = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 10
        )
        INDEX4 = typing___cast(
            ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 11
        )
    UNSPECIFIED = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 0
    )
    UNKNOWN = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 1
    )
    INDEX0 = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 7
    )
    INDEX1 = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 8
    )
    INDEX2 = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 9
    )
    INDEX3 = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 10
    )
    INDEX4 = typing___cast(
        ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexValue, 11
    )
    type___ProductCustomAttributeIndex = ProductCustomAttributeIndex
    def __init__(self,) -> None: ...

type___ProductCustomAttributeIndexEnum = ProductCustomAttributeIndexEnum