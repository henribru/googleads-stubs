"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.common.simulation_pb2
import google.ads.google_ads.v5.proto.enums.simulation_modification_method_pb2
import google.ads.google_ads.v5.proto.enums.simulation_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AdGroupSimulation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_GROUP_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MODIFICATION_METHOD_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    CPC_BID_POINT_LIST_FIELD_NUMBER: builtins.int
    CPV_BID_POINT_LIST_FIELD_NUMBER: builtins.int
    TARGET_CPA_POINT_LIST_FIELD_NUMBER: builtins.int
    TARGET_ROAS_POINT_LIST_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    ad_group_id: builtins.int = ...
    type: google.ads.google_ads.v5.proto.enums.simulation_type_pb2.SimulationTypeEnum.SimulationType.V = (
        ...
    )
    modification_method: google.ads.google_ads.v5.proto.enums.simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod.V = (
        ...
    )
    start_date: typing.Text = ...
    end_date: typing.Text = ...
    @property
    def cpc_bid_point_list(
        self,
    ) -> google.ads.google_ads.v5.proto.common.simulation_pb2.CpcBidSimulationPointList: ...
    @property
    def cpv_bid_point_list(
        self,
    ) -> google.ads.google_ads.v5.proto.common.simulation_pb2.CpvBidSimulationPointList: ...
    @property
    def target_cpa_point_list(
        self,
    ) -> google.ads.google_ads.v5.proto.common.simulation_pb2.TargetCpaSimulationPointList: ...
    @property
    def target_roas_point_list(
        self,
    ) -> google.ads.google_ads.v5.proto.common.simulation_pb2.TargetRoasSimulationPointList: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        ad_group_id: builtins.int = ...,
        type: google.ads.google_ads.v5.proto.enums.simulation_type_pb2.SimulationTypeEnum.SimulationType.V = ...,
        modification_method: google.ads.google_ads.v5.proto.enums.simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod.V = ...,
        start_date: typing.Text = ...,
        end_date: typing.Text = ...,
        cpc_bid_point_list: typing.Optional[
            google.ads.google_ads.v5.proto.common.simulation_pb2.CpcBidSimulationPointList
        ] = ...,
        cpv_bid_point_list: typing.Optional[
            google.ads.google_ads.v5.proto.common.simulation_pb2.CpvBidSimulationPointList
        ] = ...,
        target_cpa_point_list: typing.Optional[
            google.ads.google_ads.v5.proto.common.simulation_pb2.TargetCpaSimulationPointList
        ] = ...,
        target_roas_point_list: typing.Optional[
            google.ads.google_ads.v5.proto.common.simulation_pb2.TargetRoasSimulationPointList
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_ad_group_id",
            b"_ad_group_id",
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "cpv_bid_point_list",
            b"cpv_bid_point_list",
            "end_date",
            b"end_date",
            "point_list",
            b"point_list",
            "start_date",
            b"start_date",
            "target_cpa_point_list",
            b"target_cpa_point_list",
            "target_roas_point_list",
            b"target_roas_point_list",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_ad_group_id",
            b"_ad_group_id",
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "cpv_bid_point_list",
            b"cpv_bid_point_list",
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
            "target_cpa_point_list",
            b"target_cpa_point_list",
            "target_roas_point_list",
            b"target_roas_point_list",
            "type",
            b"type",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_ad_group_id", b"_ad_group_id"]
    ) -> typing_extensions.Literal["ad_group_id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_end_date", b"_end_date"]
    ) -> typing_extensions.Literal["end_date"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_start_date", b"_start_date"]
    ) -> typing_extensions.Literal["start_date"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["point_list", b"point_list"]
    ) -> typing_extensions.Literal[
        "cpc_bid_point_list",
        "cpv_bid_point_list",
        "target_cpa_point_list",
        "target_roas_point_list",
    ]: ...

global___AdGroupSimulation = AdGroupSimulation
