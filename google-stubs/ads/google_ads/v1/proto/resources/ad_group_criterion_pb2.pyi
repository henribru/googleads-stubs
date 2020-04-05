# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.criteria_pb2 import (
    AgeRangeInfo as google___ads___googleads___v1___common___criteria_pb2___AgeRangeInfo,
    AppPaymentModelInfo as google___ads___googleads___v1___common___criteria_pb2___AppPaymentModelInfo,
    CustomAffinityInfo as google___ads___googleads___v1___common___criteria_pb2___CustomAffinityInfo,
    CustomIntentInfo as google___ads___googleads___v1___common___criteria_pb2___CustomIntentInfo,
    GenderInfo as google___ads___googleads___v1___common___criteria_pb2___GenderInfo,
    IncomeRangeInfo as google___ads___googleads___v1___common___criteria_pb2___IncomeRangeInfo,
    KeywordInfo as google___ads___googleads___v1___common___criteria_pb2___KeywordInfo,
    ListingGroupInfo as google___ads___googleads___v1___common___criteria_pb2___ListingGroupInfo,
    MobileAppCategoryInfo as google___ads___googleads___v1___common___criteria_pb2___MobileAppCategoryInfo,
    MobileApplicationInfo as google___ads___googleads___v1___common___criteria_pb2___MobileApplicationInfo,
    ParentalStatusInfo as google___ads___googleads___v1___common___criteria_pb2___ParentalStatusInfo,
    PlacementInfo as google___ads___googleads___v1___common___criteria_pb2___PlacementInfo,
    TopicInfo as google___ads___googleads___v1___common___criteria_pb2___TopicInfo,
    UserInterestInfo as google___ads___googleads___v1___common___criteria_pb2___UserInterestInfo,
    UserListInfo as google___ads___googleads___v1___common___criteria_pb2___UserListInfo,
    WebpageInfo as google___ads___googleads___v1___common___criteria_pb2___WebpageInfo,
    YouTubeChannelInfo as google___ads___googleads___v1___common___criteria_pb2___YouTubeChannelInfo,
    YouTubeVideoInfo as google___ads___googleads___v1___common___criteria_pb2___YouTubeVideoInfo,
)

from google.ads.google_ads.v1.proto.common.custom_parameter_pb2 import (
    CustomParameter as google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter,
)

from google.ads.google_ads.v1.proto.enums.ad_group_criterion_approval_status_pb2 import (
    AdGroupCriterionApprovalStatusEnum as google___ads___googleads___v1___enums___ad_group_criterion_approval_status_pb2___AdGroupCriterionApprovalStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.ad_group_criterion_status_pb2 import (
    AdGroupCriterionStatusEnum as google___ads___googleads___v1___enums___ad_group_criterion_status_pb2___AdGroupCriterionStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.bidding_source_pb2 import (
    BiddingSourceEnum as google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum,
)

from google.ads.google_ads.v1.proto.enums.criterion_system_serving_status_pb2 import (
    CriterionSystemServingStatusEnum as google___ads___googleads___v1___enums___criterion_system_serving_status_pb2___CriterionSystemServingStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.criterion_type_pb2 import (
    CriterionTypeEnum as google___ads___googleads___v1___enums___criterion_type_pb2___CriterionTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.quality_score_bucket_pb2 import (
    QualityScoreBucketEnum as google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
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

class AdGroupCriterion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class QualityInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        creative_quality_score = (
            ...
        )  # type: google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum.QualityScoreBucket
        post_click_quality_score = (
            ...
        )  # type: google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum.QualityScoreBucket
        search_predicted_ctr = (
            ...
        )  # type: google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum.QualityScoreBucket
        @property
        def quality_score(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
        def __init__(
            self,
            *,
            quality_score: typing___Optional[
                google___protobuf___wrappers_pb2___Int32Value
            ] = None,
            creative_quality_score: typing___Optional[
                google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum.QualityScoreBucket
            ] = None,
            post_click_quality_score: typing___Optional[
                google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum.QualityScoreBucket
            ] = None,
            search_predicted_ctr: typing___Optional[
                google___ads___googleads___v1___enums___quality_score_bucket_pb2___QualityScoreBucketEnum.QualityScoreBucket
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AdGroupCriterion.QualityInfo: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> AdGroupCriterion.QualityInfo: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal["quality_score", b"quality_score"],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
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
    global___QualityInfo = QualityInfo
    class PositionEstimates(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def first_page_cpc_micros(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def first_position_cpc_micros(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def top_of_page_cpc_micros(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def estimated_add_clicks_at_first_position_cpc(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def estimated_add_cost_at_first_position_cpc(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            first_page_cpc_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            first_position_cpc_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            top_of_page_cpc_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            estimated_add_clicks_at_first_position_cpc: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            estimated_add_cost_at_first_position_cpc: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> AdGroupCriterion.PositionEstimates: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> AdGroupCriterion.PositionEstimates: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
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
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
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
    global___PositionEstimates = PositionEstimates

    resource_name = ...  # type: typing___Text
    status = (
        ...
    )  # type: google___ads___googleads___v1___enums___ad_group_criterion_status_pb2___AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    type = (
        ...
    )  # type: google___ads___googleads___v1___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType
    system_serving_status = (
        ...
    )  # type: google___ads___googleads___v1___enums___criterion_system_serving_status_pb2___CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    approval_status = (
        ...
    )  # type: google___ads___googleads___v1___enums___ad_group_criterion_approval_status_pb2___AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    effective_cpc_bid_source = (
        ...
    )  # type: google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
    effective_cpm_bid_source = (
        ...
    )  # type: google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
    effective_cpv_bid_source = (
        ...
    )  # type: google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
    effective_percent_cpc_bid_source = (
        ...
    )  # type: google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
    @property
    def criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def quality_info(self) -> global___AdGroupCriterion.QualityInfo: ...
    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def negative(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def bid_modifier(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def cpc_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpm_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpv_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def percent_cpc_bid_micros(
        self
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def effective_cpc_bid_micros(
        self
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def effective_cpm_bid_micros(
        self
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def effective_cpv_bid_micros(
        self
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def effective_percent_cpc_bid_micros(
        self
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def position_estimates(self) -> global___AdGroupCriterion.PositionEstimates: ...
    @property
    def final_urls(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_mobile_urls(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def tracking_url_template(
        self
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def url_custom_parameters(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def keyword(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___KeywordInfo: ...
    @property
    def placement(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___PlacementInfo: ...
    @property
    def mobile_app_category(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___MobileAppCategoryInfo: ...
    @property
    def mobile_application(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___MobileApplicationInfo: ...
    @property
    def listing_group(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___ListingGroupInfo: ...
    @property
    def age_range(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___AgeRangeInfo: ...
    @property
    def gender(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___GenderInfo: ...
    @property
    def income_range(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___IncomeRangeInfo: ...
    @property
    def parental_status(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___ParentalStatusInfo: ...
    @property
    def user_list(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___UserListInfo: ...
    @property
    def youtube_video(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___YouTubeVideoInfo: ...
    @property
    def youtube_channel(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___YouTubeChannelInfo: ...
    @property
    def topic(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___TopicInfo: ...
    @property
    def user_interest(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___UserInterestInfo: ...
    @property
    def webpage(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___WebpageInfo: ...
    @property
    def app_payment_model(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___AppPaymentModelInfo: ...
    @property
    def custom_affinity(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___CustomAffinityInfo: ...
    @property
    def custom_intent(
        self
    ) -> google___ads___googleads___v1___common___criteria_pb2___CustomIntentInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v1___enums___ad_group_criterion_status_pb2___AdGroupCriterionStatusEnum.AdGroupCriterionStatus
        ] = None,
        quality_info: typing___Optional[global___AdGroupCriterion.QualityInfo] = None,
        ad_group: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v1___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType
        ] = None,
        negative: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        system_serving_status: typing___Optional[
            google___ads___googleads___v1___enums___criterion_system_serving_status_pb2___CriterionSystemServingStatusEnum.CriterionSystemServingStatus
        ] = None,
        approval_status: typing___Optional[
            google___ads___googleads___v1___enums___ad_group_criterion_approval_status_pb2___AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
        ] = None,
        bid_modifier: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpm_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpv_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        percent_cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        effective_cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        effective_cpm_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        effective_cpv_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        effective_percent_cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        effective_cpc_bid_source: typing___Optional[
            google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
        ] = None,
        effective_cpm_bid_source: typing___Optional[
            google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
        ] = None,
        effective_cpv_bid_source: typing___Optional[
            google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
        ] = None,
        effective_percent_cpc_bid_source: typing___Optional[
            google___ads___googleads___v1___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSource
        ] = None,
        position_estimates: typing___Optional[
            global___AdGroupCriterion.PositionEstimates
        ] = None,
        final_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_mobile_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        keyword: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___KeywordInfo
        ] = None,
        placement: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___PlacementInfo
        ] = None,
        mobile_app_category: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___MobileAppCategoryInfo
        ] = None,
        mobile_application: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___MobileApplicationInfo
        ] = None,
        listing_group: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___ListingGroupInfo
        ] = None,
        age_range: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___AgeRangeInfo
        ] = None,
        gender: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___GenderInfo
        ] = None,
        income_range: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___IncomeRangeInfo
        ] = None,
        parental_status: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___ParentalStatusInfo
        ] = None,
        user_list: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___UserListInfo
        ] = None,
        youtube_video: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___YouTubeVideoInfo
        ] = None,
        youtube_channel: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___YouTubeChannelInfo
        ] = None,
        topic: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___TopicInfo
        ] = None,
        user_interest: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___UserInterestInfo
        ] = None,
        webpage: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___WebpageInfo
        ] = None,
        app_payment_model: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___AppPaymentModelInfo
        ] = None,
        custom_affinity: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___CustomAffinityInfo
        ] = None,
        custom_intent: typing___Optional[
            google___ads___googleads___v1___common___criteria_pb2___CustomIntentInfo
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AdGroupCriterion: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AdGroupCriterion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
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
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
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
        self, oneof_group: typing_extensions___Literal["criterion", b"criterion"]
    ) -> typing_extensions___Literal[
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
