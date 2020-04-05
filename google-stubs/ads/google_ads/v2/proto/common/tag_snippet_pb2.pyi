# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.tracking_code_page_format_pb2 import (
    TrackingCodePageFormatEnum as google___ads___googleads___v2___enums___tracking_code_page_format_pb2___TrackingCodePageFormatEnum,
)

from google.ads.google_ads.v2.proto.enums.tracking_code_type_pb2 import (
    TrackingCodeTypeEnum as google___ads___googleads___v2___enums___tracking_code_type_pb2___TrackingCodeTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class TagSnippet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: google___ads___googleads___v2___enums___tracking_code_type_pb2___TrackingCodeTypeEnum.TrackingCodeType
    page_format = ... # type: google___ads___googleads___v2___enums___tracking_code_page_format_pb2___TrackingCodePageFormatEnum.TrackingCodePageFormat

    @property
    def global_site_tag(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def event_snippet(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        type : typing___Optional[google___ads___googleads___v2___enums___tracking_code_type_pb2___TrackingCodeTypeEnum.TrackingCodeType] = None,
        page_format : typing___Optional[google___ads___googleads___v2___enums___tracking_code_page_format_pb2___TrackingCodePageFormatEnum.TrackingCodePageFormat] = None,
        global_site_tag : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        event_snippet : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TagSnippet: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TagSnippet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"event_snippet",b"event_snippet",u"global_site_tag",b"global_site_tag"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"event_snippet",b"event_snippet",u"global_site_tag",b"global_site_tag",u"page_format",b"page_format",u"type",b"type"]) -> None: ...
global___TagSnippet = TagSnippet
