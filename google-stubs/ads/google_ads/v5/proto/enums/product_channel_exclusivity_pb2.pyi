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

class ProductChannelExclusivityEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ProductChannelExclusivityValue = typing___NewType(
        "ProductChannelExclusivityValue", builtin___int
    )
    type___ProductChannelExclusivityValue = ProductChannelExclusivityValue
    ProductChannelExclusivity: _ProductChannelExclusivity
    class _ProductChannelExclusivity(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ProductChannelExclusivityEnum.ProductChannelExclusivityValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 0
        )
        UNKNOWN = typing___cast(
            ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 1
        )
        SINGLE_CHANNEL = typing___cast(
            ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 2
        )
        MULTI_CHANNEL = typing___cast(
            ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 3
        )
    UNSPECIFIED = typing___cast(
        ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 0
    )
    UNKNOWN = typing___cast(
        ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 1
    )
    SINGLE_CHANNEL = typing___cast(
        ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 2
    )
    MULTI_CHANNEL = typing___cast(
        ProductChannelExclusivityEnum.ProductChannelExclusivityValue, 3
    )
    type___ProductChannelExclusivity = ProductChannelExclusivity
    def __init__(self,) -> None: ...

type___ProductChannelExclusivityEnum = ProductChannelExclusivityEnum