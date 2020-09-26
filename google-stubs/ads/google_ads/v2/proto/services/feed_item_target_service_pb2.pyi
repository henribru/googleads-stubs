# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v2.proto.resources.feed_item_target_pb2 import (
    FeedItemTarget as google___ads___googleads___v2___resources___feed_item_target_pb2___FeedItemTarget,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

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

class GetFeedItemTargetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetFeedItemTargetRequest = GetFeedItemTargetRequest

class MutateFeedItemTargetsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___FeedItemTargetOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[type___FeedItemTargetOperation]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id", b"customer_id", "operations", b"operations"
        ],
    ) -> None: ...

type___MutateFeedItemTargetsRequest = MutateFeedItemTargetsRequest

class FeedItemTargetOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v2___resources___feed_item_target_pb2___FeedItemTarget: ...
    def __init__(
        self,
        *,
        create: typing___Optional[
            google___ads___googleads___v2___resources___feed_item_target_pb2___FeedItemTarget
        ] = None,
        remove: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation", "remove", b"remove"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation", "remove", b"remove"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "remove"]: ...

type___FeedItemTargetOperation = FeedItemTargetOperation

class MutateFeedItemTargetsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MutateFeedItemTargetResult
    ]: ...
    def __init__(
        self,
        *,
        results: typing___Optional[
            typing___Iterable[type___MutateFeedItemTargetResult]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["results", b"results"]
    ) -> None: ...

type___MutateFeedItemTargetsResponse = MutateFeedItemTargetsResponse

class MutateFeedItemTargetResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateFeedItemTargetResult = MutateFeedItemTargetResult
