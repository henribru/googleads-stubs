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

class MediaTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MediaTypeValue = typing___NewType("MediaTypeValue", builtin___int)
    type___MediaTypeValue = MediaTypeValue
    MediaType: _MediaType
    class _MediaType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MediaTypeEnum.MediaTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(MediaTypeEnum.MediaTypeValue, 0)
        UNKNOWN = typing___cast(MediaTypeEnum.MediaTypeValue, 1)
        IMAGE = typing___cast(MediaTypeEnum.MediaTypeValue, 2)
        ICON = typing___cast(MediaTypeEnum.MediaTypeValue, 3)
        MEDIA_BUNDLE = typing___cast(MediaTypeEnum.MediaTypeValue, 4)
        AUDIO = typing___cast(MediaTypeEnum.MediaTypeValue, 5)
        VIDEO = typing___cast(MediaTypeEnum.MediaTypeValue, 6)
        DYNAMIC_IMAGE = typing___cast(MediaTypeEnum.MediaTypeValue, 7)
    UNSPECIFIED = typing___cast(MediaTypeEnum.MediaTypeValue, 0)
    UNKNOWN = typing___cast(MediaTypeEnum.MediaTypeValue, 1)
    IMAGE = typing___cast(MediaTypeEnum.MediaTypeValue, 2)
    ICON = typing___cast(MediaTypeEnum.MediaTypeValue, 3)
    MEDIA_BUNDLE = typing___cast(MediaTypeEnum.MediaTypeValue, 4)
    AUDIO = typing___cast(MediaTypeEnum.MediaTypeValue, 5)
    VIDEO = typing___cast(MediaTypeEnum.MediaTypeValue, 6)
    DYNAMIC_IMAGE = typing___cast(MediaTypeEnum.MediaTypeValue, 7)
    type___MediaType = MediaType
    def __init__(self,) -> None: ...

type___MediaTypeEnum = MediaTypeEnum