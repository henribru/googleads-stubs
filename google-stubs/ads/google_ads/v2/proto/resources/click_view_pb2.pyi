# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.click_location_pb2 import (
    ClickLocation as google___ads___googleads___v2___common___click_location_pb2___ClickLocation,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ClickView(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    @property
    def gclid(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def area_of_interest(self) -> google___ads___googleads___v2___common___click_location_pb2___ClickLocation: ...

    @property
    def location_of_presence(self) -> google___ads___googleads___v2___common___click_location_pb2___ClickLocation: ...

    @property
    def page_number(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def ad_group_ad(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        gclid : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        area_of_interest : typing___Optional[google___ads___googleads___v2___common___click_location_pb2___ClickLocation] = None,
        location_of_presence : typing___Optional[google___ads___googleads___v2___common___click_location_pb2___ClickLocation] = None,
        page_number : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ad_group_ad : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ClickView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group_ad",u"area_of_interest",u"gclid",u"location_of_presence",u"page_number"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group_ad",u"area_of_interest",u"gclid",u"location_of_presence",u"page_number",u"resource_name"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group_ad",b"ad_group_ad",u"area_of_interest",b"area_of_interest",u"gclid",b"gclid",u"location_of_presence",b"location_of_presence",u"page_number",b"page_number"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group_ad",b"ad_group_ad",u"area_of_interest",b"area_of_interest",u"gclid",b"gclid",u"location_of_presence",b"location_of_presence",u"page_number",b"page_number",u"resource_name",b"resource_name"]) -> None: ...
