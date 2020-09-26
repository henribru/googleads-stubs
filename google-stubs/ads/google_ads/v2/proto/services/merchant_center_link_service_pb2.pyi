# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v2.proto.resources.merchant_center_link_pb2 import (
    MerchantCenterLink as google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
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

class ListMerchantCenterLinksRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    def __init__(
        self, *, customer_id: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["customer_id", b"customer_id"]
    ) -> None: ...

type___ListMerchantCenterLinksRequest = ListMerchantCenterLinksRequest

class ListMerchantCenterLinksResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def merchant_center_links(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink
    ]: ...
    def __init__(
        self,
        *,
        merchant_center_links: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink
            ]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "merchant_center_links", b"merchant_center_links"
        ],
    ) -> None: ...

type___ListMerchantCenterLinksResponse = ListMerchantCenterLinksResponse

class GetMerchantCenterLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetMerchantCenterLinkRequest = GetMerchantCenterLinkRequest

class MutateMerchantCenterLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    @property
    def operation(self) -> type___MerchantCenterLinkOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operation: typing___Optional[type___MerchantCenterLinkOperation] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["operation", b"operation"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id", b"customer_id", "operation", b"operation"
        ],
    ) -> None: ...

type___MutateMerchantCenterLinkRequest = MutateMerchantCenterLinkRequest

class MerchantCenterLinkOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def update(
        self,
    ) -> google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        update: typing___Optional[
            google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink
        ] = None,
        remove: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["update", "remove"]: ...

type___MerchantCenterLinkOperation = MerchantCenterLinkOperation

class MutateMerchantCenterLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def result(self) -> type___MutateMerchantCenterLinkResult: ...
    def __init__(
        self,
        *,
        result: typing___Optional[type___MutateMerchantCenterLinkResult] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> None: ...

type___MutateMerchantCenterLinkResponse = MutateMerchantCenterLinkResponse

class MutateMerchantCenterLinkResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateMerchantCenterLinkResult = MutateMerchantCenterLinkResult
