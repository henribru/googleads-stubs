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

class ProductConditionEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ProductConditionValue = typing___NewType("ProductConditionValue", builtin___int)
    type___ProductConditionValue = ProductConditionValue
    ProductCondition: _ProductCondition
    class _ProductCondition(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ProductConditionEnum.ProductConditionValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ProductConditionEnum.ProductConditionValue, 0)
        UNKNOWN = typing___cast(ProductConditionEnum.ProductConditionValue, 1)
        NEW = typing___cast(ProductConditionEnum.ProductConditionValue, 3)
        REFURBISHED = typing___cast(ProductConditionEnum.ProductConditionValue, 4)
        USED = typing___cast(ProductConditionEnum.ProductConditionValue, 5)
    UNSPECIFIED = typing___cast(ProductConditionEnum.ProductConditionValue, 0)
    UNKNOWN = typing___cast(ProductConditionEnum.ProductConditionValue, 1)
    NEW = typing___cast(ProductConditionEnum.ProductConditionValue, 3)
    REFURBISHED = typing___cast(ProductConditionEnum.ProductConditionValue, 4)
    USED = typing___cast(ProductConditionEnum.ProductConditionValue, 5)
    type___ProductCondition = ProductCondition
    def __init__(self,) -> None: ...

type___ProductConditionEnum = ProductConditionEnum
