# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.common.simulation_pb2 import (
    BidModifierSimulationPointList as google___ads___googleads___v6___common___simulation_pb2___BidModifierSimulationPointList,
)
from google.ads.google_ads.v6.proto.enums.simulation_modification_method_pb2 import (
    SimulationModificationMethodEnum as google___ads___googleads___v6___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum,
)
from google.ads.google_ads.v6.proto.enums.simulation_type_pb2 import (
    SimulationTypeEnum as google___ads___googleads___v6___enums___simulation_type_pb2___SimulationTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CampaignCriterionSimulation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    campaign_id: builtin___int = ...
    criterion_id: builtin___int = ...
    type: google___ads___googleads___v6___enums___simulation_type_pb2___SimulationTypeEnum.SimulationTypeValue = ...
    modification_method: google___ads___googleads___v6___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethodValue = ...
    start_date: typing___Text = ...
    end_date: typing___Text = ...
    @property
    def bid_modifier_point_list(
        self,
    ) -> google___ads___googleads___v6___common___simulation_pb2___BidModifierSimulationPointList: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        campaign_id: typing___Optional[builtin___int] = None,
        criterion_id: typing___Optional[builtin___int] = None,
        type: typing___Optional[
            google___ads___googleads___v6___enums___simulation_type_pb2___SimulationTypeEnum.SimulationTypeValue
        ] = None,
        modification_method: typing___Optional[
            google___ads___googleads___v6___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethodValue
        ] = None,
        start_date: typing___Optional[typing___Text] = None,
        end_date: typing___Optional[typing___Text] = None,
        bid_modifier_point_list: typing___Optional[
            google___ads___googleads___v6___common___simulation_pb2___BidModifierSimulationPointList
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_campaign_id",
            b"_campaign_id",
            "_criterion_id",
            b"_criterion_id",
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "bid_modifier_point_list",
            b"bid_modifier_point_list",
            "campaign_id",
            b"campaign_id",
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
            "_campaign_id",
            b"_campaign_id",
            "_criterion_id",
            b"_criterion_id",
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "bid_modifier_point_list",
            b"bid_modifier_point_list",
            "campaign_id",
            b"campaign_id",
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
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_campaign_id", b"_campaign_id"]
    ) -> typing_extensions___Literal["campaign_id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_criterion_id", b"_criterion_id"],
    ) -> typing_extensions___Literal["criterion_id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_end_date", b"_end_date"]
    ) -> typing_extensions___Literal["end_date"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_start_date", b"_start_date"]
    ) -> typing_extensions___Literal["start_date"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["point_list", b"point_list"]
    ) -> typing_extensions___Literal["bid_modifier_point_list"]: ...

type___CampaignCriterionSimulation = CampaignCriterionSimulation