# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.geo_target_constant_status_pb2 import (
    GeoTargetConstantStatusEnum as google___ads___googleads___v2___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum,
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


class GeoTargetConstant(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v2___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum.GeoTargetConstantStatus.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def target_type(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def canonical_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        target_type : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        status : typing___Optional[google___ads___googleads___v2___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum.GeoTargetConstantStatus.ClosedValueType] = None,
        canonical_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GeoTargetConstant: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"canonical_name",u"country_code",u"id",u"name",u"target_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"canonical_name",u"country_code",u"id",u"name",u"resource_name",u"status",u"target_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"canonical_name",b"canonical_name",u"country_code",b"country_code",u"id",b"id",u"name",b"name",u"target_type",b"target_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"canonical_name",b"canonical_name",u"country_code",b"country_code",u"id",b"id",u"name",b"name",u"resource_name",b"resource_name",u"status",b"status",u"target_type",b"target_type"]) -> None: ...
