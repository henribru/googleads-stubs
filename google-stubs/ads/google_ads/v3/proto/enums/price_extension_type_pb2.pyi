# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class PriceExtensionTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PriceExtensionType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "PriceExtensionTypeEnum.PriceExtensionType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["PriceExtensionTypeEnum.PriceExtensionType"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "PriceExtensionTypeEnum.PriceExtensionType"]
        ]: ...
        UNSPECIFIED = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 0)
        UNKNOWN = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 1)
        BRANDS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 2)
        EVENTS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 3)
        LOCATIONS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 4)
        NEIGHBORHOODS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 5)
        PRODUCT_CATEGORIES = typing___cast(
            "PriceExtensionTypeEnum.PriceExtensionType", 6
        )
        PRODUCT_TIERS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 7)
        SERVICES = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 8)
        SERVICE_CATEGORIES = typing___cast(
            "PriceExtensionTypeEnum.PriceExtensionType", 9
        )
        SERVICE_TIERS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 10)
    UNSPECIFIED = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 0)
    UNKNOWN = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 1)
    BRANDS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 2)
    EVENTS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 3)
    LOCATIONS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 4)
    NEIGHBORHOODS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 5)
    PRODUCT_CATEGORIES = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 6)
    PRODUCT_TIERS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 7)
    SERVICES = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 8)
    SERVICE_CATEGORIES = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 9)
    SERVICE_TIERS = typing___cast("PriceExtensionTypeEnum.PriceExtensionType", 10)
    global___PriceExtensionType = PriceExtensionType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PriceExtensionTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> PriceExtensionTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___PriceExtensionTypeEnum = PriceExtensionTypeEnum