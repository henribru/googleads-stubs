"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.common.custom_parameter_pb2
import google.ads.google_ads.v5.proto.common.explorer_auto_optimizer_setting_pb2
import google.ads.google_ads.v5.proto.common.targeting_setting_pb2
import google.ads.google_ads.v5.proto.enums.ad_group_ad_rotation_mode_pb2
import google.ads.google_ads.v5.proto.enums.ad_group_status_pb2
import google.ads.google_ads.v5.proto.enums.ad_group_type_pb2
import google.ads.google_ads.v5.proto.enums.bidding_source_pb2
import google.ads.google_ads.v5.proto.enums.targeting_dimension_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AdGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    AD_ROTATION_MODE_FIELD_NUMBER: builtins.int
    BASE_AD_GROUP_FIELD_NUMBER: builtins.int
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: builtins.int
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    CPM_BID_MICROS_FIELD_NUMBER: builtins.int
    TARGET_CPA_MICROS_FIELD_NUMBER: builtins.int
    CPV_BID_MICROS_FIELD_NUMBER: builtins.int
    TARGET_CPM_MICROS_FIELD_NUMBER: builtins.int
    TARGET_ROAS_FIELD_NUMBER: builtins.int
    PERCENT_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EXPLORER_AUTO_OPTIMIZER_SETTING_FIELD_NUMBER: builtins.int
    DISPLAY_CUSTOM_BID_DIMENSION_FIELD_NUMBER: builtins.int
    FINAL_URL_SUFFIX_FIELD_NUMBER: builtins.int
    TARGETING_SETTING_FIELD_NUMBER: builtins.int
    EFFECTIVE_TARGET_CPA_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_TARGET_CPA_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_TARGET_ROAS_FIELD_NUMBER: builtins.int
    EFFECTIVE_TARGET_ROAS_SOURCE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    id: builtins.int = ...
    name: typing.Text = ...
    status: google.ads.google_ads.v5.proto.enums.ad_group_status_pb2.AdGroupStatusEnum.AdGroupStatus.V = (
        ...
    )
    type: google.ads.google_ads.v5.proto.enums.ad_group_type_pb2.AdGroupTypeEnum.AdGroupType.V = (
        ...
    )
    ad_rotation_mode: google.ads.google_ads.v5.proto.enums.ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum.AdGroupAdRotationMode.V = (
        ...
    )
    base_ad_group: typing.Text = ...
    tracking_url_template: typing.Text = ...
    campaign: typing.Text = ...
    cpc_bid_micros: builtins.int = ...
    cpm_bid_micros: builtins.int = ...
    target_cpa_micros: builtins.int = ...
    cpv_bid_micros: builtins.int = ...
    target_cpm_micros: builtins.int = ...
    target_roas: builtins.float = ...
    percent_cpc_bid_micros: builtins.int = ...
    display_custom_bid_dimension: google.ads.google_ads.v5.proto.enums.targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension.V = (
        ...
    )
    final_url_suffix: typing.Text = ...
    effective_target_cpa_micros: builtins.int = ...
    effective_target_cpa_source: google.ads.google_ads.v5.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = (
        ...
    )
    effective_target_roas: builtins.float = ...
    effective_target_roas_source: google.ads.google_ads.v5.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = (
        ...
    )
    labels: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    @property
    def url_custom_parameters(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.ads.google_ads.v5.proto.common.custom_parameter_pb2.CustomParameter
    ]: ...
    @property
    def explorer_auto_optimizer_setting(
        self,
    ) -> google.ads.google_ads.v5.proto.common.explorer_auto_optimizer_setting_pb2.ExplorerAutoOptimizerSetting: ...
    @property
    def targeting_setting(
        self,
    ) -> google.ads.google_ads.v5.proto.common.targeting_setting_pb2.TargetingSetting: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: builtins.int = ...,
        name: typing.Text = ...,
        status: google.ads.google_ads.v5.proto.enums.ad_group_status_pb2.AdGroupStatusEnum.AdGroupStatus.V = ...,
        type: google.ads.google_ads.v5.proto.enums.ad_group_type_pb2.AdGroupTypeEnum.AdGroupType.V = ...,
        ad_rotation_mode: google.ads.google_ads.v5.proto.enums.ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum.AdGroupAdRotationMode.V = ...,
        base_ad_group: typing.Text = ...,
        tracking_url_template: typing.Text = ...,
        url_custom_parameters: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v5.proto.common.custom_parameter_pb2.CustomParameter
            ]
        ] = ...,
        campaign: typing.Text = ...,
        cpc_bid_micros: builtins.int = ...,
        cpm_bid_micros: builtins.int = ...,
        target_cpa_micros: builtins.int = ...,
        cpv_bid_micros: builtins.int = ...,
        target_cpm_micros: builtins.int = ...,
        target_roas: builtins.float = ...,
        percent_cpc_bid_micros: builtins.int = ...,
        explorer_auto_optimizer_setting: typing.Optional[
            google.ads.google_ads.v5.proto.common.explorer_auto_optimizer_setting_pb2.ExplorerAutoOptimizerSetting
        ] = ...,
        display_custom_bid_dimension: google.ads.google_ads.v5.proto.enums.targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension.V = ...,
        final_url_suffix: typing.Text = ...,
        targeting_setting: typing.Optional[
            google.ads.google_ads.v5.proto.common.targeting_setting_pb2.TargetingSetting
        ] = ...,
        effective_target_cpa_micros: builtins.int = ...,
        effective_target_cpa_source: google.ads.google_ads.v5.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = ...,
        effective_target_roas: builtins.float = ...,
        effective_target_roas_source: google.ads.google_ads.v5.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = ...,
        labels: typing.Optional[typing.Iterable[typing.Text]] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_base_ad_group",
            b"_base_ad_group",
            "_campaign",
            b"_campaign",
            "_cpc_bid_micros",
            b"_cpc_bid_micros",
            "_cpm_bid_micros",
            b"_cpm_bid_micros",
            "_cpv_bid_micros",
            b"_cpv_bid_micros",
            "_effective_target_cpa_micros",
            b"_effective_target_cpa_micros",
            "_effective_target_roas",
            b"_effective_target_roas",
            "_final_url_suffix",
            b"_final_url_suffix",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_percent_cpc_bid_micros",
            b"_percent_cpc_bid_micros",
            "_target_cpa_micros",
            b"_target_cpa_micros",
            "_target_cpm_micros",
            b"_target_cpm_micros",
            "_target_roas",
            b"_target_roas",
            "_tracking_url_template",
            b"_tracking_url_template",
            "base_ad_group",
            b"base_ad_group",
            "campaign",
            b"campaign",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "cpm_bid_micros",
            b"cpm_bid_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "effective_target_cpa_micros",
            b"effective_target_cpa_micros",
            "effective_target_roas",
            b"effective_target_roas",
            "explorer_auto_optimizer_setting",
            b"explorer_auto_optimizer_setting",
            "final_url_suffix",
            b"final_url_suffix",
            "id",
            b"id",
            "name",
            b"name",
            "percent_cpc_bid_micros",
            b"percent_cpc_bid_micros",
            "target_cpa_micros",
            b"target_cpa_micros",
            "target_cpm_micros",
            b"target_cpm_micros",
            "target_roas",
            b"target_roas",
            "targeting_setting",
            b"targeting_setting",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_base_ad_group",
            b"_base_ad_group",
            "_campaign",
            b"_campaign",
            "_cpc_bid_micros",
            b"_cpc_bid_micros",
            "_cpm_bid_micros",
            b"_cpm_bid_micros",
            "_cpv_bid_micros",
            b"_cpv_bid_micros",
            "_effective_target_cpa_micros",
            b"_effective_target_cpa_micros",
            "_effective_target_roas",
            b"_effective_target_roas",
            "_final_url_suffix",
            b"_final_url_suffix",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_percent_cpc_bid_micros",
            b"_percent_cpc_bid_micros",
            "_target_cpa_micros",
            b"_target_cpa_micros",
            "_target_cpm_micros",
            b"_target_cpm_micros",
            "_target_roas",
            b"_target_roas",
            "_tracking_url_template",
            b"_tracking_url_template",
            "ad_rotation_mode",
            b"ad_rotation_mode",
            "base_ad_group",
            b"base_ad_group",
            "campaign",
            b"campaign",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "cpm_bid_micros",
            b"cpm_bid_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "display_custom_bid_dimension",
            b"display_custom_bid_dimension",
            "effective_target_cpa_micros",
            b"effective_target_cpa_micros",
            "effective_target_cpa_source",
            b"effective_target_cpa_source",
            "effective_target_roas",
            b"effective_target_roas",
            "effective_target_roas_source",
            b"effective_target_roas_source",
            "explorer_auto_optimizer_setting",
            b"explorer_auto_optimizer_setting",
            "final_url_suffix",
            b"final_url_suffix",
            "id",
            b"id",
            "labels",
            b"labels",
            "name",
            b"name",
            "percent_cpc_bid_micros",
            b"percent_cpc_bid_micros",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "target_cpa_micros",
            b"target_cpa_micros",
            "target_cpm_micros",
            b"target_cpm_micros",
            "target_roas",
            b"target_roas",
            "targeting_setting",
            b"targeting_setting",
            "tracking_url_template",
            b"tracking_url_template",
            "type",
            b"type",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_base_ad_group", b"_base_ad_group"],
    ) -> typing_extensions.Literal["base_ad_group"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_campaign", b"_campaign"]
    ) -> typing_extensions.Literal["campaign"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_cpc_bid_micros", b"_cpc_bid_micros"],
    ) -> typing_extensions.Literal["cpc_bid_micros"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_cpm_bid_micros", b"_cpm_bid_micros"],
    ) -> typing_extensions.Literal["cpm_bid_micros"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_cpv_bid_micros", b"_cpv_bid_micros"],
    ) -> typing_extensions.Literal["cpv_bid_micros"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_effective_target_cpa_micros", b"_effective_target_cpa_micros"
        ],
    ) -> typing_extensions.Literal["effective_target_cpa_micros"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_effective_target_roas", b"_effective_target_roas"
        ],
    ) -> typing_extensions.Literal["effective_target_roas"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_final_url_suffix", b"_final_url_suffix"
        ],
    ) -> typing_extensions.Literal["final_url_suffix"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_id", b"_id"]
    ) -> typing_extensions.Literal["id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_name", b"_name"]
    ) -> typing_extensions.Literal["name"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_percent_cpc_bid_micros", b"_percent_cpc_bid_micros"
        ],
    ) -> typing_extensions.Literal["percent_cpc_bid_micros"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_target_cpa_micros", b"_target_cpa_micros"
        ],
    ) -> typing_extensions.Literal["target_cpa_micros"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_target_cpm_micros", b"_target_cpm_micros"
        ],
    ) -> typing_extensions.Literal["target_cpm_micros"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_target_roas", b"_target_roas"]
    ) -> typing_extensions.Literal["target_roas"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_tracking_url_template", b"_tracking_url_template"
        ],
    ) -> typing_extensions.Literal["tracking_url_template"]: ...

global___AdGroup = AdGroup
