# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class DynamicSearchAdsSearchTermView(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    @property
    def search_term(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def headline(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def landing_page(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def page_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        search_term : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        headline : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        landing_page : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        page_url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DynamicSearchAdsSearchTermView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"headline",u"landing_page",u"page_url",u"search_term"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"headline",u"landing_page",u"page_url",u"resource_name",u"search_term"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"headline",b"headline",u"landing_page",b"landing_page",u"page_url",b"page_url",u"search_term",b"search_term"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"headline",b"headline",u"landing_page",b"landing_page",u"page_url",b"page_url",u"resource_name",b"resource_name",u"search_term",b"search_term"]) -> None: ...
