"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v4.proto.common.criteria_pb2
import google.ads.google_ads.v4.proto.common.custom_parameter_pb2
import google.ads.google_ads.v4.proto.enums.ad_group_criterion_approval_status_pb2
import google.ads.google_ads.v4.proto.enums.ad_group_criterion_status_pb2
import google.ads.google_ads.v4.proto.enums.bidding_source_pb2
import google.ads.google_ads.v4.proto.enums.criterion_system_serving_status_pb2
import google.ads.google_ads.v4.proto.enums.criterion_type_pb2
import google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AdGroupCriterion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class QualityInfo(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        QUALITY_SCORE_FIELD_NUMBER: builtins.int
        CREATIVE_QUALITY_SCORE_FIELD_NUMBER: builtins.int
        POST_CLICK_QUALITY_SCORE_FIELD_NUMBER: builtins.int
        SEARCH_PREDICTED_CTR_FIELD_NUMBER: builtins.int
        creative_quality_score: google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.V = (
            ...
        )
        post_click_quality_score: google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.V = (
            ...
        )
        search_predicted_ctr: google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.V = (
            ...
        )
        @property
        def quality_score(self) -> google.protobuf.wrappers_pb2.Int32Value: ...
        def __init__(
            self,
            *,
            quality_score: typing.Optional[
                google.protobuf.wrappers_pb2.Int32Value
            ] = ...,
            creative_quality_score: google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.V = ...,
            post_click_quality_score: google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.V = ...,
            search_predicted_ctr: google.ads.google_ads.v4.proto.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.V = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal["quality_score", b"quality_score"],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "creative_quality_score",
                b"creative_quality_score",
                "post_click_quality_score",
                b"post_click_quality_score",
                "quality_score",
                b"quality_score",
                "search_predicted_ctr",
                b"search_predicted_ctr",
            ],
        ) -> None: ...
    class PositionEstimates(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        FIRST_PAGE_CPC_MICROS_FIELD_NUMBER: builtins.int
        FIRST_POSITION_CPC_MICROS_FIELD_NUMBER: builtins.int
        TOP_OF_PAGE_CPC_MICROS_FIELD_NUMBER: builtins.int
        ESTIMATED_ADD_CLICKS_AT_FIRST_POSITION_CPC_FIELD_NUMBER: builtins.int
        ESTIMATED_ADD_COST_AT_FIRST_POSITION_CPC_FIELD_NUMBER: builtins.int
        @property
        def first_page_cpc_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
        @property
        def first_position_cpc_micros(
            self,
        ) -> google.protobuf.wrappers_pb2.Int64Value: ...
        @property
        def top_of_page_cpc_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
        @property
        def estimated_add_clicks_at_first_position_cpc(
            self,
        ) -> google.protobuf.wrappers_pb2.Int64Value: ...
        @property
        def estimated_add_cost_at_first_position_cpc(
            self,
        ) -> google.protobuf.wrappers_pb2.Int64Value: ...
        def __init__(
            self,
            *,
            first_page_cpc_micros: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
            first_position_cpc_micros: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
            top_of_page_cpc_micros: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
            estimated_add_clicks_at_first_position_cpc: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
            estimated_add_cost_at_first_position_cpc: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "estimated_add_clicks_at_first_position_cpc",
                b"estimated_add_clicks_at_first_position_cpc",
                "estimated_add_cost_at_first_position_cpc",
                b"estimated_add_cost_at_first_position_cpc",
                "first_page_cpc_micros",
                b"first_page_cpc_micros",
                "first_position_cpc_micros",
                b"first_position_cpc_micros",
                "top_of_page_cpc_micros",
                b"top_of_page_cpc_micros",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "estimated_add_clicks_at_first_position_cpc",
                b"estimated_add_clicks_at_first_position_cpc",
                "estimated_add_cost_at_first_position_cpc",
                b"estimated_add_cost_at_first_position_cpc",
                "first_page_cpc_micros",
                b"first_page_cpc_micros",
                "first_position_cpc_micros",
                b"first_position_cpc_micros",
                "top_of_page_cpc_micros",
                b"top_of_page_cpc_micros",
            ],
        ) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CRITERION_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    QUALITY_INFO_FIELD_NUMBER: builtins.int
    AD_GROUP_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NEGATIVE_FIELD_NUMBER: builtins.int
    SYSTEM_SERVING_STATUS_FIELD_NUMBER: builtins.int
    APPROVAL_STATUS_FIELD_NUMBER: builtins.int
    DISAPPROVAL_REASONS_FIELD_NUMBER: builtins.int
    BID_MODIFIER_FIELD_NUMBER: builtins.int
    CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    CPM_BID_MICROS_FIELD_NUMBER: builtins.int
    CPV_BID_MICROS_FIELD_NUMBER: builtins.int
    PERCENT_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPM_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPV_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_PERCENT_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPC_BID_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPM_BID_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPV_BID_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_PERCENT_CPC_BID_SOURCE_FIELD_NUMBER: builtins.int
    POSITION_ESTIMATES_FIELD_NUMBER: builtins.int
    FINAL_URLS_FIELD_NUMBER: builtins.int
    FINAL_MOBILE_URLS_FIELD_NUMBER: builtins.int
    FINAL_URL_SUFFIX_FIELD_NUMBER: builtins.int
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: builtins.int
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    PLACEMENT_FIELD_NUMBER: builtins.int
    MOBILE_APP_CATEGORY_FIELD_NUMBER: builtins.int
    MOBILE_APPLICATION_FIELD_NUMBER: builtins.int
    LISTING_GROUP_FIELD_NUMBER: builtins.int
    AGE_RANGE_FIELD_NUMBER: builtins.int
    GENDER_FIELD_NUMBER: builtins.int
    INCOME_RANGE_FIELD_NUMBER: builtins.int
    PARENTAL_STATUS_FIELD_NUMBER: builtins.int
    USER_LIST_FIELD_NUMBER: builtins.int
    YOUTUBE_VIDEO_FIELD_NUMBER: builtins.int
    YOUTUBE_CHANNEL_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    USER_INTEREST_FIELD_NUMBER: builtins.int
    WEBPAGE_FIELD_NUMBER: builtins.int
    APP_PAYMENT_MODEL_FIELD_NUMBER: builtins.int
    CUSTOM_AFFINITY_FIELD_NUMBER: builtins.int
    CUSTOM_INTENT_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    status: google.ads.google_ads.v4.proto.enums.ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus.V = (
        ...
    )
    type: google.ads.google_ads.v4.proto.enums.criterion_type_pb2.CriterionTypeEnum.CriterionType.V = (
        ...
    )
    system_serving_status: google.ads.google_ads.v4.proto.enums.criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum.CriterionSystemServingStatus.V = (
        ...
    )
    approval_status: google.ads.google_ads.v4.proto.enums.ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus.V = (
        ...
    )
    effective_cpc_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = (
        ...
    )
    effective_cpm_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = (
        ...
    )
    effective_cpv_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = (
        ...
    )
    effective_percent_cpc_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = (
        ...
    )
    @property
    def criterion_id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def quality_info(self) -> global___AdGroupCriterion.QualityInfo: ...
    @property
    def ad_group(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def negative(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def disapproval_reasons(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.StringValue
    ]: ...
    @property
    def bid_modifier(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def cpc_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def cpm_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def cpv_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def percent_cpc_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def effective_cpc_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def effective_cpm_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def effective_cpv_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def effective_percent_cpc_bid_micros(
        self,
    ) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def position_estimates(self) -> global___AdGroupCriterion.PositionEstimates: ...
    @property
    def final_urls(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.StringValue
    ]: ...
    @property
    def final_mobile_urls(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.StringValue
    ]: ...
    @property
    def final_url_suffix(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def tracking_url_template(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.ads.google_ads.v4.proto.common.custom_parameter_pb2.CustomParameter
    ]: ...
    @property
    def keyword(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.KeywordInfo: ...
    @property
    def placement(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.PlacementInfo: ...
    @property
    def mobile_app_category(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.MobileAppCategoryInfo: ...
    @property
    def mobile_application(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.MobileApplicationInfo: ...
    @property
    def listing_group(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.ListingGroupInfo: ...
    @property
    def age_range(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.AgeRangeInfo: ...
    @property
    def gender(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.GenderInfo: ...
    @property
    def income_range(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.IncomeRangeInfo: ...
    @property
    def parental_status(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.ParentalStatusInfo: ...
    @property
    def user_list(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.UserListInfo: ...
    @property
    def youtube_video(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.YouTubeVideoInfo: ...
    @property
    def youtube_channel(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.YouTubeChannelInfo: ...
    @property
    def topic(self) -> google.ads.google_ads.v4.proto.common.criteria_pb2.TopicInfo: ...
    @property
    def user_interest(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.UserInterestInfo: ...
    @property
    def webpage(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.WebpageInfo: ...
    @property
    def app_payment_model(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.AppPaymentModelInfo: ...
    @property
    def custom_affinity(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.CustomAffinityInfo: ...
    @property
    def custom_intent(
        self,
    ) -> google.ads.google_ads.v4.proto.common.criteria_pb2.CustomIntentInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        criterion_id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        status: google.ads.google_ads.v4.proto.enums.ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus.V = ...,
        quality_info: typing.Optional[global___AdGroupCriterion.QualityInfo] = ...,
        ad_group: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        type: google.ads.google_ads.v4.proto.enums.criterion_type_pb2.CriterionTypeEnum.CriterionType.V = ...,
        negative: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        system_serving_status: google.ads.google_ads.v4.proto.enums.criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum.CriterionSystemServingStatus.V = ...,
        approval_status: google.ads.google_ads.v4.proto.enums.ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus.V = ...,
        disapproval_reasons: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.StringValue]
        ] = ...,
        bid_modifier: typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
        cpc_bid_micros: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        cpm_bid_micros: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        cpv_bid_micros: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        percent_cpc_bid_micros: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        effective_cpc_bid_micros: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        effective_cpm_bid_micros: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        effective_cpv_bid_micros: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        effective_percent_cpc_bid_micros: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        effective_cpc_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = ...,
        effective_cpm_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = ...,
        effective_cpv_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = ...,
        effective_percent_cpc_bid_source: google.ads.google_ads.v4.proto.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.V = ...,
        position_estimates: typing.Optional[
            global___AdGroupCriterion.PositionEstimates
        ] = ...,
        final_urls: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.StringValue]
        ] = ...,
        final_mobile_urls: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.StringValue]
        ] = ...,
        final_url_suffix: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        tracking_url_template: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        url_custom_parameters: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v4.proto.common.custom_parameter_pb2.CustomParameter
            ]
        ] = ...,
        keyword: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.KeywordInfo
        ] = ...,
        placement: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.PlacementInfo
        ] = ...,
        mobile_app_category: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.MobileAppCategoryInfo
        ] = ...,
        mobile_application: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.MobileApplicationInfo
        ] = ...,
        listing_group: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.ListingGroupInfo
        ] = ...,
        age_range: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.AgeRangeInfo
        ] = ...,
        gender: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.GenderInfo
        ] = ...,
        income_range: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.IncomeRangeInfo
        ] = ...,
        parental_status: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.ParentalStatusInfo
        ] = ...,
        user_list: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.UserListInfo
        ] = ...,
        youtube_video: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.YouTubeVideoInfo
        ] = ...,
        youtube_channel: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.YouTubeChannelInfo
        ] = ...,
        topic: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.TopicInfo
        ] = ...,
        user_interest: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.UserInterestInfo
        ] = ...,
        webpage: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.WebpageInfo
        ] = ...,
        app_payment_model: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.AppPaymentModelInfo
        ] = ...,
        custom_affinity: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.CustomAffinityInfo
        ] = ...,
        custom_intent: typing.Optional[
            google.ads.google_ads.v4.proto.common.criteria_pb2.CustomIntentInfo
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "ad_group",
            b"ad_group",
            "age_range",
            b"age_range",
            "app_payment_model",
            b"app_payment_model",
            "bid_modifier",
            b"bid_modifier",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "cpm_bid_micros",
            b"cpm_bid_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "custom_affinity",
            b"custom_affinity",
            "custom_intent",
            b"custom_intent",
            "effective_cpc_bid_micros",
            b"effective_cpc_bid_micros",
            "effective_cpm_bid_micros",
            b"effective_cpm_bid_micros",
            "effective_cpv_bid_micros",
            b"effective_cpv_bid_micros",
            "effective_percent_cpc_bid_micros",
            b"effective_percent_cpc_bid_micros",
            "final_url_suffix",
            b"final_url_suffix",
            "gender",
            b"gender",
            "income_range",
            b"income_range",
            "keyword",
            b"keyword",
            "listing_group",
            b"listing_group",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "negative",
            b"negative",
            "parental_status",
            b"parental_status",
            "percent_cpc_bid_micros",
            b"percent_cpc_bid_micros",
            "placement",
            b"placement",
            "position_estimates",
            b"position_estimates",
            "quality_info",
            b"quality_info",
            "topic",
            b"topic",
            "tracking_url_template",
            b"tracking_url_template",
            "user_interest",
            b"user_interest",
            "user_list",
            b"user_list",
            "webpage",
            b"webpage",
            "youtube_channel",
            b"youtube_channel",
            "youtube_video",
            b"youtube_video",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ad_group",
            b"ad_group",
            "age_range",
            b"age_range",
            "app_payment_model",
            b"app_payment_model",
            "approval_status",
            b"approval_status",
            "bid_modifier",
            b"bid_modifier",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "cpm_bid_micros",
            b"cpm_bid_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "custom_affinity",
            b"custom_affinity",
            "custom_intent",
            b"custom_intent",
            "disapproval_reasons",
            b"disapproval_reasons",
            "effective_cpc_bid_micros",
            b"effective_cpc_bid_micros",
            "effective_cpc_bid_source",
            b"effective_cpc_bid_source",
            "effective_cpm_bid_micros",
            b"effective_cpm_bid_micros",
            "effective_cpm_bid_source",
            b"effective_cpm_bid_source",
            "effective_cpv_bid_micros",
            b"effective_cpv_bid_micros",
            "effective_cpv_bid_source",
            b"effective_cpv_bid_source",
            "effective_percent_cpc_bid_micros",
            b"effective_percent_cpc_bid_micros",
            "effective_percent_cpc_bid_source",
            b"effective_percent_cpc_bid_source",
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_url_suffix",
            b"final_url_suffix",
            "final_urls",
            b"final_urls",
            "gender",
            b"gender",
            "income_range",
            b"income_range",
            "keyword",
            b"keyword",
            "listing_group",
            b"listing_group",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "negative",
            b"negative",
            "parental_status",
            b"parental_status",
            "percent_cpc_bid_micros",
            b"percent_cpc_bid_micros",
            "placement",
            b"placement",
            "position_estimates",
            b"position_estimates",
            "quality_info",
            b"quality_info",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "system_serving_status",
            b"system_serving_status",
            "topic",
            b"topic",
            "tracking_url_template",
            b"tracking_url_template",
            "type",
            b"type",
            "url_custom_parameters",
            b"url_custom_parameters",
            "user_interest",
            b"user_interest",
            "user_list",
            b"user_list",
            "webpage",
            b"webpage",
            "youtube_channel",
            b"youtube_channel",
            "youtube_video",
            b"youtube_video",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["criterion", b"criterion"]
    ) -> typing_extensions.Literal[
        "keyword",
        "placement",
        "mobile_app_category",
        "mobile_application",
        "listing_group",
        "age_range",
        "gender",
        "income_range",
        "parental_status",
        "user_list",
        "youtube_video",
        "youtube_channel",
        "topic",
        "user_interest",
        "webpage",
        "app_payment_model",
        "custom_affinity",
        "custom_intent",
    ]: ...

global___AdGroupCriterion = AdGroupCriterion
