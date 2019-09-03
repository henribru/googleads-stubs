# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.mime_type_pb2 import (
    MimeTypeEnum as google___ads___googleads___v2___enums___mime_type_pb2___MimeTypeEnum,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BytesValue as google___protobuf___wrappers_pb2___BytesValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class YoutubeVideoAsset(google___protobuf___message___Message):

    @property
    def youtube_video_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        youtube_video_id : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> YoutubeVideoAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"youtube_video_id"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"youtube_video_id"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"youtube_video_id",b"youtube_video_id"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"youtube_video_id",b"youtube_video_id"]) -> None: ...

class MediaBundleAsset(google___protobuf___message___Message):

    @property
    def data(self) -> google___protobuf___wrappers_pb2___BytesValue: ...

    def __init__(self,
        *,
        data : typing___Optional[google___protobuf___wrappers_pb2___BytesValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MediaBundleAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"data"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> None: ...

class ImageAsset(google___protobuf___message___Message):
    mime_type = ... # type: google___ads___googleads___v2___enums___mime_type_pb2___MimeTypeEnum.MimeType.ClosedValueType

    @property
    def data(self) -> google___protobuf___wrappers_pb2___BytesValue: ...

    @property
    def file_size(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def full_size(self) -> ImageDimension: ...

    def __init__(self,
        *,
        data : typing___Optional[google___protobuf___wrappers_pb2___BytesValue] = None,
        file_size : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        mime_type : typing___Optional[google___ads___googleads___v2___enums___mime_type_pb2___MimeTypeEnum.MimeType.ClosedValueType] = None,
        full_size : typing___Optional[ImageDimension] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ImageAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data",u"file_size",u"full_size"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"data",u"file_size",u"full_size",u"mime_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data",u"file_size",b"file_size",u"full_size",b"full_size"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"file_size",b"file_size",u"full_size",b"full_size",u"mime_type",b"mime_type"]) -> None: ...

class ImageDimension(google___protobuf___message___Message):

    @property
    def height_pixels(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def width_pixels(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        height_pixels : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        width_pixels : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ImageDimension: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"height_pixels",u"url",u"width_pixels"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"height_pixels",u"url",u"width_pixels"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"height_pixels",b"height_pixels",u"url",b"url",u"width_pixels",b"width_pixels"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"height_pixels",b"height_pixels",u"url",b"url",u"width_pixels",b"width_pixels"]) -> None: ...

class TextAsset(google___protobuf___message___Message):

    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TextAsset: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"text"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"text",b"text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"text",b"text"]) -> None: ...
