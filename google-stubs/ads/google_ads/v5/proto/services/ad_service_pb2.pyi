# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.response_content_type_pb2 import (
    ResponseContentTypeEnum as google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum,
)

from google.ads.google_ads.v5.proto.resources.ad_pb2 import (
    Ad as google___ads___googleads___v5___resources___ad_pb2___Ad,
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

class GetAdRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetAdRequest = GetAdRequest

class MutateAdsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    response_content_type: google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum.ResponseContentTypeValue = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___AdOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[typing___Iterable[type___AdOperation]] = None,
        response_content_type: typing___Optional[
            google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum.ResponseContentTypeValue
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "response_content_type",
            b"response_content_type",
        ],
    ) -> None: ...

type___MutateAdsRequest = MutateAdsRequest

class AdOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def update(self) -> google___ads___googleads___v5___resources___ad_pb2___Ad: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        update: typing___Optional[
            google___ads___googleads___v5___resources___ad_pb2___Ad
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "operation",
            b"operation",
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
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["update"]: ...

type___AdOperation = AdOperation

class MutateAdsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MutateAdResult
    ]: ...
    def __init__(
        self,
        *,
        results: typing___Optional[typing___Iterable[type___MutateAdResult]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["results", b"results"]
    ) -> None: ...

type___MutateAdsResponse = MutateAdsResponse

class MutateAdResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def ad(self) -> google___ads___googleads___v5___resources___ad_pb2___Ad: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad: typing___Optional[
            google___ads___googleads___v5___resources___ad_pb2___Ad
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["ad", b"ad"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad", b"ad", "resource_name", b"resource_name"
        ],
    ) -> None: ...

type___MutateAdResult = MutateAdResult
