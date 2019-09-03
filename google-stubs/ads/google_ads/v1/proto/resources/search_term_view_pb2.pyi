# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.search_term_targeting_status_pb2 import (
    SearchTermTargetingStatusEnum as google___ads___googleads___v1___enums___search_term_targeting_status_pb2___SearchTermTargetingStatusEnum,
)

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


class SearchTermView(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v1___enums___search_term_targeting_status_pb2___SearchTermTargetingStatusEnum.SearchTermTargetingStatus.ClosedValueType

    @property
    def search_term(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        search_term : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad_group : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        status : typing___Optional[google___ads___googleads___v1___enums___search_term_targeting_status_pb2___SearchTermTargetingStatusEnum.SearchTermTargetingStatus.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SearchTermView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group",u"search_term"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",u"resource_name",u"search_term",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"search_term",b"search_term"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"resource_name",b"resource_name",u"search_term",b"search_term",u"status",b"status"]) -> None: ...
