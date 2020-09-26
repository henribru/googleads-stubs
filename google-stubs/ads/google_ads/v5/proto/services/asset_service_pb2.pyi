# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.response_content_type_pb2 import (
    ResponseContentTypeEnum as google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum,
)

from google.ads.google_ads.v5.proto.resources.asset_pb2 import (
    Asset as google___ads___googleads___v5___resources___asset_pb2___Asset,
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

class GetAssetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetAssetRequest = GetAssetRequest

class MutateAssetsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    response_content_type: google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum.ResponseContentTypeValue = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___AssetOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[typing___Iterable[type___AssetOperation]] = None,
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

type___MutateAssetsRequest = MutateAssetsRequest

class AssetOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v5___resources___asset_pb2___Asset: ...
    def __init__(
        self,
        *,
        create: typing___Optional[
            google___ads___googleads___v5___resources___asset_pb2___Asset
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create"]: ...

type___AssetOperation = AssetOperation

class MutateAssetsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MutateAssetResult
    ]: ...
    def __init__(
        self,
        *,
        results: typing___Optional[typing___Iterable[type___MutateAssetResult]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["results", b"results"]
    ) -> None: ...

type___MutateAssetsResponse = MutateAssetsResponse

class MutateAssetResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def asset(
        self,
    ) -> google___ads___googleads___v5___resources___asset_pb2___Asset: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        asset: typing___Optional[
            google___ads___googleads___v5___resources___asset_pb2___Asset
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["asset", b"asset"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "asset", b"asset", "resource_name", b"resource_name"
        ],
    ) -> None: ...

type___MutateAssetResult = MutateAssetResult
