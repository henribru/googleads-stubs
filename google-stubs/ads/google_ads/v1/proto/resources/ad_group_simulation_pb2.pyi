# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.simulation_pb2 import (
    CpcBidSimulationPointList as google___ads___googleads___v1___common___simulation_pb2___CpcBidSimulationPointList,
    CpvBidSimulationPointList as google___ads___googleads___v1___common___simulation_pb2___CpvBidSimulationPointList,
    TargetCpaSimulationPointList as google___ads___googleads___v1___common___simulation_pb2___TargetCpaSimulationPointList,
)

from google.ads.google_ads.v1.proto.enums.simulation_modification_method_pb2 import (
    SimulationModificationMethodEnum as google___ads___googleads___v1___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum,
)

from google.ads.google_ads.v1.proto.enums.simulation_type_pb2 import (
    SimulationTypeEnum as google___ads___googleads___v1___enums___simulation_type_pb2___SimulationTypeEnum,
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


class AdGroupSimulation(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    type = ... # type: google___ads___googleads___v1___enums___simulation_type_pb2___SimulationTypeEnum.SimulationType.ClosedValueType
    modification_method = ... # type: google___ads___googleads___v1___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethod.ClosedValueType

    @property
    def ad_group_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def cpc_bid_point_list(self) -> google___ads___googleads___v1___common___simulation_pb2___CpcBidSimulationPointList: ...

    @property
    def cpv_bid_point_list(self) -> google___ads___googleads___v1___common___simulation_pb2___CpvBidSimulationPointList: ...

    @property
    def target_cpa_point_list(self) -> google___ads___googleads___v1___common___simulation_pb2___TargetCpaSimulationPointList: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ad_group_id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        type : typing___Optional[google___ads___googleads___v1___enums___simulation_type_pb2___SimulationTypeEnum.SimulationType.ClosedValueType] = None,
        modification_method : typing___Optional[google___ads___googleads___v1___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethod.ClosedValueType] = None,
        start_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        end_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        cpc_bid_point_list : typing___Optional[google___ads___googleads___v1___common___simulation_pb2___CpcBidSimulationPointList] = None,
        cpv_bid_point_list : typing___Optional[google___ads___googleads___v1___common___simulation_pb2___CpvBidSimulationPointList] = None,
        target_cpa_point_list : typing___Optional[google___ads___googleads___v1___common___simulation_pb2___TargetCpaSimulationPointList] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupSimulation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group_id",u"cpc_bid_point_list",u"cpv_bid_point_list",u"end_date",u"point_list",u"start_date",u"target_cpa_point_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group_id",u"cpc_bid_point_list",u"cpv_bid_point_list",u"end_date",u"modification_method",u"point_list",u"resource_name",u"start_date",u"target_cpa_point_list",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group_id",b"ad_group_id",u"cpc_bid_point_list",b"cpc_bid_point_list",u"cpv_bid_point_list",b"cpv_bid_point_list",u"end_date",b"end_date",u"point_list",b"point_list",u"start_date",b"start_date",u"target_cpa_point_list",b"target_cpa_point_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group_id",b"ad_group_id",u"cpc_bid_point_list",b"cpc_bid_point_list",u"cpv_bid_point_list",b"cpv_bid_point_list",u"end_date",b"end_date",u"modification_method",b"modification_method",u"point_list",b"point_list",u"resource_name",b"resource_name",u"start_date",b"start_date",u"target_cpa_point_list",b"target_cpa_point_list",u"type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"point_list",b"point_list"]) -> typing_extensions___Literal["cpc_bid_point_list","cpv_bid_point_list","target_cpa_point_list"]: ...
