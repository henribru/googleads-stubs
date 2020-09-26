# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.served_asset_field_type_pb2 import (
    ServedAssetFieldTypeEnum as google___ads___googleads___v5___enums___served_asset_field_type_pb2___ServedAssetFieldTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AdTextAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    text: typing___Text = ...
    pinned_field: google___ads___googleads___v5___enums___served_asset_field_type_pb2___ServedAssetFieldTypeEnum.ServedAssetFieldTypeValue = ...
    def __init__(
        self,
        *,
        text: typing___Optional[typing___Text] = None,
        pinned_field: typing___Optional[
            google___ads___googleads___v5___enums___served_asset_field_type_pb2___ServedAssetFieldTypeEnum.ServedAssetFieldTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["_text", b"_text", "text", b"text"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_text", b"_text", "pinned_field", b"pinned_field", "text", b"text"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_text", b"_text"]
    ) -> typing_extensions___Literal["text"]: ...

type___AdTextAsset = AdTextAsset

class AdImageAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    asset: typing___Text = ...
    def __init__(self, *, asset: typing___Optional[typing___Text] = None,) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["_asset", b"_asset", "asset", b"asset"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["_asset", b"_asset", "asset", b"asset"],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_asset", b"_asset"]
    ) -> typing_extensions___Literal["asset"]: ...

type___AdImageAsset = AdImageAsset

class AdVideoAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    asset: typing___Text = ...
    def __init__(self, *, asset: typing___Optional[typing___Text] = None,) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["_asset", b"_asset", "asset", b"asset"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["_asset", b"_asset", "asset", b"asset"],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_asset", b"_asset"]
    ) -> typing_extensions___Literal["asset"]: ...

type___AdVideoAsset = AdVideoAsset

class AdMediaBundleAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    asset: typing___Text = ...
    def __init__(self, *, asset: typing___Optional[typing___Text] = None,) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["_asset", b"_asset", "asset", b"asset"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["_asset", b"_asset", "asset", b"asset"],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_asset", b"_asset"]
    ) -> typing_extensions___Literal["asset"]: ...

type___AdMediaBundleAsset = AdMediaBundleAsset
