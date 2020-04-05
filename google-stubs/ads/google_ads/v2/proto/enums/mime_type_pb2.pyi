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

class MimeTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MimeType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "MimeTypeEnum.MimeType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["MimeTypeEnum.MimeType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[typing___Tuple[builtin___str, "MimeTypeEnum.MimeType"]]: ...
        UNSPECIFIED = typing___cast("MimeTypeEnum.MimeType", 0)
        UNKNOWN = typing___cast("MimeTypeEnum.MimeType", 1)
        IMAGE_JPEG = typing___cast("MimeTypeEnum.MimeType", 2)
        IMAGE_GIF = typing___cast("MimeTypeEnum.MimeType", 3)
        IMAGE_PNG = typing___cast("MimeTypeEnum.MimeType", 4)
        FLASH = typing___cast("MimeTypeEnum.MimeType", 5)
        TEXT_HTML = typing___cast("MimeTypeEnum.MimeType", 6)
        PDF = typing___cast("MimeTypeEnum.MimeType", 7)
        MSWORD = typing___cast("MimeTypeEnum.MimeType", 8)
        MSEXCEL = typing___cast("MimeTypeEnum.MimeType", 9)
        RTF = typing___cast("MimeTypeEnum.MimeType", 10)
        AUDIO_WAV = typing___cast("MimeTypeEnum.MimeType", 11)
        AUDIO_MP3 = typing___cast("MimeTypeEnum.MimeType", 12)
        HTML5_AD_ZIP = typing___cast("MimeTypeEnum.MimeType", 13)
    UNSPECIFIED = typing___cast("MimeTypeEnum.MimeType", 0)
    UNKNOWN = typing___cast("MimeTypeEnum.MimeType", 1)
    IMAGE_JPEG = typing___cast("MimeTypeEnum.MimeType", 2)
    IMAGE_GIF = typing___cast("MimeTypeEnum.MimeType", 3)
    IMAGE_PNG = typing___cast("MimeTypeEnum.MimeType", 4)
    FLASH = typing___cast("MimeTypeEnum.MimeType", 5)
    TEXT_HTML = typing___cast("MimeTypeEnum.MimeType", 6)
    PDF = typing___cast("MimeTypeEnum.MimeType", 7)
    MSWORD = typing___cast("MimeTypeEnum.MimeType", 8)
    MSEXCEL = typing___cast("MimeTypeEnum.MimeType", 9)
    RTF = typing___cast("MimeTypeEnum.MimeType", 10)
    AUDIO_WAV = typing___cast("MimeTypeEnum.MimeType", 11)
    AUDIO_MP3 = typing___cast("MimeTypeEnum.MimeType", 12)
    HTML5_AD_ZIP = typing___cast("MimeTypeEnum.MimeType", 13)
    global___MimeType = MimeType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MimeTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MimeTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___MimeTypeEnum = MimeTypeEnum
