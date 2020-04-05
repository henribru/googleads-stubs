# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.simulation_pb2 import (
    CpcBidSimulationPointList as google___ads___googleads___v2___common___simulation_pb2___CpcBidSimulationPointList,
)

from google.ads.google_ads.v2.proto.enums.simulation_modification_method_pb2 import (
    SimulationModificationMethodEnum as google___ads___googleads___v2___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum,
)

from google.ads.google_ads.v2.proto.enums.simulation_type_pb2 import (
    SimulationTypeEnum as google___ads___googleads___v2___enums___simulation_type_pb2___SimulationTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
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

class AdGroupCriterionSimulation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    type = (
        ...
    )  # type: google___ads___googleads___v2___enums___simulation_type_pb2___SimulationTypeEnum.SimulationType
    modification_method = (
        ...
    )  # type: google___ads___googleads___v2___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethod
    @property
    def ad_group_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def cpc_bid_point_list(
        self,
    ) -> google___ads___googleads___v2___common___simulation_pb2___CpcBidSimulationPointList: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad_group_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___simulation_type_pb2___SimulationTypeEnum.SimulationType
        ] = None,
        modification_method: typing___Optional[
            google___ads___googleads___v2___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethod
        ] = None,
        start_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        end_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        cpc_bid_point_list: typing___Optional[
            google___ads___googleads___v2___common___simulation_pb2___CpcBidSimulationPointList
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AdGroupCriterionSimulation: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AdGroupCriterionSimulation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "criterion_id",
            b"criterion_id",
            "end_date",
            b"end_date",
            "point_list",
            b"point_list",
            "start_date",
            b"start_date",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "criterion_id",
            b"criterion_id",
            "end_date",
            b"end_date",
            "modification_method",
            b"modification_method",
            "point_list",
            b"point_list",
            "resource_name",
            b"resource_name",
            "start_date",
            b"start_date",
            "type",
            b"type",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["point_list", b"point_list"]
    ) -> typing_extensions___Literal["cpc_bid_point_list"]: ...

global___AdGroupCriterionSimulation = AdGroupCriterionSimulation
