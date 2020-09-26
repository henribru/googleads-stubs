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

class AssetFieldTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AssetFieldTypeValue = typing___NewType("AssetFieldTypeValue", builtin___int)
    type___AssetFieldTypeValue = AssetFieldTypeValue
    AssetFieldType: _AssetFieldType
    class _AssetFieldType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AssetFieldTypeEnum.AssetFieldTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 0)
        UNKNOWN = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 1)
        HEADLINE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 2)
        DESCRIPTION = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 3)
        MANDATORY_AD_TEXT = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 4)
        MARKETING_IMAGE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 5)
        MEDIA_BUNDLE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 6)
        YOUTUBE_VIDEO = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 7)
        BOOK_ON_GOOGLE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 8)
    UNSPECIFIED = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 0)
    UNKNOWN = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 1)
    HEADLINE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 2)
    DESCRIPTION = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 3)
    MANDATORY_AD_TEXT = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 4)
    MARKETING_IMAGE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 5)
    MEDIA_BUNDLE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 6)
    YOUTUBE_VIDEO = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 7)
    BOOK_ON_GOOGLE = typing___cast(AssetFieldTypeEnum.AssetFieldTypeValue, 8)
    type___AssetFieldType = AssetFieldType
    def __init__(self,) -> None: ...

type___AssetFieldTypeEnum = AssetFieldTypeEnum
