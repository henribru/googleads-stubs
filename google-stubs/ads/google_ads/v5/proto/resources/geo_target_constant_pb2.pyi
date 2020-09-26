# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.geo_target_constant_status_pb2 import (
    GeoTargetConstantStatusEnum as google___ads___googleads___v5___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GeoTargetConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    name: typing___Text = ...
    country_code: typing___Text = ...
    target_type: typing___Text = ...
    status: google___ads___googleads___v5___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum.GeoTargetConstantStatusValue = ...
    canonical_name: typing___Text = ...
    parent_geo_target: typing___Text = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        name: typing___Optional[typing___Text] = None,
        country_code: typing___Optional[typing___Text] = None,
        target_type: typing___Optional[typing___Text] = None,
        status: typing___Optional[
            google___ads___googleads___v5___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum.GeoTargetConstantStatusValue
        ] = None,
        canonical_name: typing___Optional[typing___Text] = None,
        parent_geo_target: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_canonical_name",
            b"_canonical_name",
            "_country_code",
            b"_country_code",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_parent_geo_target",
            b"_parent_geo_target",
            "_target_type",
            b"_target_type",
            "canonical_name",
            b"canonical_name",
            "country_code",
            b"country_code",
            "id",
            b"id",
            "name",
            b"name",
            "parent_geo_target",
            b"parent_geo_target",
            "target_type",
            b"target_type",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_canonical_name",
            b"_canonical_name",
            "_country_code",
            b"_country_code",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_parent_geo_target",
            b"_parent_geo_target",
            "_target_type",
            b"_target_type",
            "canonical_name",
            b"canonical_name",
            "country_code",
            b"country_code",
            "id",
            b"id",
            "name",
            b"name",
            "parent_geo_target",
            b"parent_geo_target",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "target_type",
            b"target_type",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_canonical_name", b"_canonical_name"],
    ) -> typing_extensions___Literal["canonical_name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_country_code", b"_country_code"],
    ) -> typing_extensions___Literal["country_code"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_parent_geo_target", b"_parent_geo_target"
        ],
    ) -> typing_extensions___Literal["parent_geo_target"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_target_type", b"_target_type"]
    ) -> typing_extensions___Literal["target_type"]: ...

type___GeoTargetConstant = GeoTargetConstant
