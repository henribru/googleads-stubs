# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.resources.geo_target_constant_pb2 import (
    GeoTargetConstant as google___ads___googleads___v2___resources___geo_target_constant_pb2___GeoTargetConstant,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetGeoTargetConstantRequest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetGeoTargetConstantRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class SuggestGeoTargetConstantsRequest(google___protobuf___message___Message):
    class LocationNames(google___protobuf___message___Message):

        @property
        def names(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

        def __init__(self,
            *,
            names : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> SuggestGeoTargetConstantsRequest.LocationNames: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"names"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"names",b"names"]) -> None: ...

    class GeoTargets(google___protobuf___message___Message):

        @property
        def geo_target_constants(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

        def __init__(self,
            *,
            geo_target_constants : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> SuggestGeoTargetConstantsRequest.GeoTargets: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"geo_target_constants"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"geo_target_constants",b"geo_target_constants"]) -> None: ...


    @property
    def locale(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def location_names(self) -> SuggestGeoTargetConstantsRequest.LocationNames: ...

    @property
    def geo_targets(self) -> SuggestGeoTargetConstantsRequest.GeoTargets: ...

    def __init__(self,
        *,
        locale : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        location_names : typing___Optional[SuggestGeoTargetConstantsRequest.LocationNames] = None,
        geo_targets : typing___Optional[SuggestGeoTargetConstantsRequest.GeoTargets] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SuggestGeoTargetConstantsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"country_code",u"geo_targets",u"locale",u"location_names",u"query"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"country_code",u"geo_targets",u"locale",u"location_names",u"query"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"country_code",b"country_code",u"geo_targets",b"geo_targets",u"locale",b"locale",u"location_names",b"location_names",u"query",b"query"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"country_code",b"country_code",u"geo_targets",b"geo_targets",u"locale",b"locale",u"location_names",b"location_names",u"query",b"query"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"query",b"query"]) -> typing_extensions___Literal["location_names","geo_targets"]: ...

class SuggestGeoTargetConstantsResponse(google___protobuf___message___Message):

    @property
    def geo_target_constant_suggestions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GeoTargetConstantSuggestion]: ...

    def __init__(self,
        *,
        geo_target_constant_suggestions : typing___Optional[typing___Iterable[GeoTargetConstantSuggestion]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SuggestGeoTargetConstantsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"geo_target_constant_suggestions"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"geo_target_constant_suggestions",b"geo_target_constant_suggestions"]) -> None: ...

class GeoTargetConstantSuggestion(google___protobuf___message___Message):

    @property
    def locale(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def reach(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def search_term(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def geo_target_constant(self) -> google___ads___googleads___v2___resources___geo_target_constant_pb2___GeoTargetConstant: ...

    @property
    def geo_target_constant_parents(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___resources___geo_target_constant_pb2___GeoTargetConstant]: ...

    def __init__(self,
        *,
        locale : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        reach : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        search_term : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        geo_target_constant : typing___Optional[google___ads___googleads___v2___resources___geo_target_constant_pb2___GeoTargetConstant] = None,
        geo_target_constant_parents : typing___Optional[typing___Iterable[google___ads___googleads___v2___resources___geo_target_constant_pb2___GeoTargetConstant]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GeoTargetConstantSuggestion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"geo_target_constant",u"locale",u"reach",u"search_term"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"geo_target_constant",u"geo_target_constant_parents",u"locale",u"reach",u"search_term"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"geo_target_constant",b"geo_target_constant",u"locale",b"locale",u"reach",b"reach",u"search_term",b"search_term"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"geo_target_constant",b"geo_target_constant",u"geo_target_constant_parents",b"geo_target_constant_parents",u"locale",b"locale",u"reach",b"reach",u"search_term",b"search_term"]) -> None: ...
