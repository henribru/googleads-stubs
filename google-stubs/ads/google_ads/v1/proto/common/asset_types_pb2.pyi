# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.mime_type_pb2 import (
    MimeTypeEnum as google___ads___googleads___v1___enums___mime_type_pb2___MimeTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BytesValue as google___protobuf___wrappers_pb2___BytesValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class YoutubeVideoAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def youtube_video_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        youtube_video_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> YoutubeVideoAsset: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> YoutubeVideoAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "youtube_video_id", b"youtube_video_id"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "youtube_video_id", b"youtube_video_id"
        ],
    ) -> None: ...

global___YoutubeVideoAsset = YoutubeVideoAsset

class MediaBundleAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def data(self) -> google___protobuf___wrappers_pb2___BytesValue: ...
    def __init__(
        self,
        *,
        data: typing___Optional[google___protobuf___wrappers_pb2___BytesValue] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MediaBundleAsset: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MediaBundleAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["data", b"data"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["data", b"data"]
    ) -> None: ...

global___MediaBundleAsset = MediaBundleAsset

class ImageAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    mime_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___mime_type_pb2___MimeTypeEnum.MimeType
    @property
    def data(self) -> google___protobuf___wrappers_pb2___BytesValue: ...
    @property
    def file_size(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def full_size(self) -> global___ImageDimension: ...
    def __init__(
        self,
        *,
        data: typing___Optional[google___protobuf___wrappers_pb2___BytesValue] = None,
        file_size: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        mime_type: typing___Optional[
            google___ads___googleads___v1___enums___mime_type_pb2___MimeTypeEnum.MimeType
        ] = None,
        full_size: typing___Optional[global___ImageDimension] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImageAsset: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ImageAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "data", b"data", "file_size", b"file_size", "full_size", b"full_size"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "data",
            b"data",
            "file_size",
            b"file_size",
            "full_size",
            b"full_size",
            "mime_type",
            b"mime_type",
        ],
    ) -> None: ...

global___ImageAsset = ImageAsset

class ImageDimension(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def height_pixels(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def width_pixels(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        height_pixels: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        width_pixels: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        url: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImageDimension: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ImageDimension: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "height_pixels",
            b"height_pixels",
            "url",
            b"url",
            "width_pixels",
            b"width_pixels",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "height_pixels",
            b"height_pixels",
            "url",
            b"url",
            "width_pixels",
            b"width_pixels",
        ],
    ) -> None: ...

global___ImageDimension = ImageDimension

class TextAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        text: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TextAsset: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TextAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["text", b"text"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["text", b"text"]
    ) -> None: ...

global___TextAsset = TextAsset
