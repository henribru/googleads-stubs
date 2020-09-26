# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v4.proto.common.matching_function_pb2 import (
    MatchingFunction as google___ads___googleads___v4___common___matching_function_pb2___MatchingFunction,
)

from google.ads.google_ads.v4.proto.enums.feed_link_status_pb2 import (
    FeedLinkStatusEnum as google___ads___googleads___v4___enums___feed_link_status_pb2___FeedLinkStatusEnum,
)

from google.ads.google_ads.v4.proto.enums.placeholder_type_pb2 import (
    PlaceholderTypeEnum as google___ads___googleads___v4___enums___placeholder_type_pb2___PlaceholderTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CustomerFeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    placeholder_types: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        google___ads___googleads___v4___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderTypeValue
    ] = ...
    status: google___ads___googleads___v4___enums___feed_link_status_pb2___FeedLinkStatusEnum.FeedLinkStatusValue = ...
    @property
    def feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def matching_function(
        self,
    ) -> google___ads___googleads___v4___common___matching_function_pb2___MatchingFunction: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        feed: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        placeholder_types: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v4___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderTypeValue
            ]
        ] = None,
        matching_function: typing___Optional[
            google___ads___googleads___v4___common___matching_function_pb2___MatchingFunction
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v4___enums___feed_link_status_pb2___FeedLinkStatusEnum.FeedLinkStatusValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "feed", b"feed", "matching_function", b"matching_function"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "feed",
            b"feed",
            "matching_function",
            b"matching_function",
            "placeholder_types",
            b"placeholder_types",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

type___CustomerFeed = CustomerFeed
