# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.enums.geo_targeting_type_pb2 import (
    GeoTargetingTypeEnum as google___ads___googleads___v3___enums___geo_targeting_type_pb2___GeoTargetingTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class GeographicView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    location_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___geo_targeting_type_pb2___GeoTargetingTypeEnum.GeoTargetingType
    @property
    def country_criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        location_type: typing___Optional[
            google___ads___googleads___v3___enums___geo_targeting_type_pb2___GeoTargetingTypeEnum.GeoTargetingType
        ] = None,
        country_criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GeographicView: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GeographicView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "country_criterion_id", b"country_criterion_id"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "country_criterion_id",
            b"country_criterion_id",
            "location_type",
            b"location_type",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

global___GeographicView = GeographicView