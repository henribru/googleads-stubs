# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.criteria_pb2 import (
    AdScheduleInfo as google___ads___googleads___v2___common___criteria_pb2___AdScheduleInfo,
    AgeRangeInfo as google___ads___googleads___v2___common___criteria_pb2___AgeRangeInfo,
    CarrierInfo as google___ads___googleads___v2___common___criteria_pb2___CarrierInfo,
    ContentLabelInfo as google___ads___googleads___v2___common___criteria_pb2___ContentLabelInfo,
    CustomAffinityInfo as google___ads___googleads___v2___common___criteria_pb2___CustomAffinityInfo,
    DeviceInfo as google___ads___googleads___v2___common___criteria_pb2___DeviceInfo,
    GenderInfo as google___ads___googleads___v2___common___criteria_pb2___GenderInfo,
    IncomeRangeInfo as google___ads___googleads___v2___common___criteria_pb2___IncomeRangeInfo,
    IpBlockInfo as google___ads___googleads___v2___common___criteria_pb2___IpBlockInfo,
    KeywordInfo as google___ads___googleads___v2___common___criteria_pb2___KeywordInfo,
    LanguageInfo as google___ads___googleads___v2___common___criteria_pb2___LanguageInfo,
    ListingScopeInfo as google___ads___googleads___v2___common___criteria_pb2___ListingScopeInfo,
    LocationGroupInfo as google___ads___googleads___v2___common___criteria_pb2___LocationGroupInfo,
    LocationInfo as google___ads___googleads___v2___common___criteria_pb2___LocationInfo,
    MobileAppCategoryInfo as google___ads___googleads___v2___common___criteria_pb2___MobileAppCategoryInfo,
    MobileApplicationInfo as google___ads___googleads___v2___common___criteria_pb2___MobileApplicationInfo,
    MobileDeviceInfo as google___ads___googleads___v2___common___criteria_pb2___MobileDeviceInfo,
    OperatingSystemVersionInfo as google___ads___googleads___v2___common___criteria_pb2___OperatingSystemVersionInfo,
    ParentalStatusInfo as google___ads___googleads___v2___common___criteria_pb2___ParentalStatusInfo,
    PlacementInfo as google___ads___googleads___v2___common___criteria_pb2___PlacementInfo,
    ProximityInfo as google___ads___googleads___v2___common___criteria_pb2___ProximityInfo,
    TopicInfo as google___ads___googleads___v2___common___criteria_pb2___TopicInfo,
    UserInterestInfo as google___ads___googleads___v2___common___criteria_pb2___UserInterestInfo,
    UserListInfo as google___ads___googleads___v2___common___criteria_pb2___UserListInfo,
    WebpageInfo as google___ads___googleads___v2___common___criteria_pb2___WebpageInfo,
    YouTubeChannelInfo as google___ads___googleads___v2___common___criteria_pb2___YouTubeChannelInfo,
    YouTubeVideoInfo as google___ads___googleads___v2___common___criteria_pb2___YouTubeVideoInfo,
)

from google.ads.google_ads.v2.proto.enums.campaign_criterion_status_pb2 import (
    CampaignCriterionStatusEnum as google___ads___googleads___v2___enums___campaign_criterion_status_pb2___CampaignCriterionStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.criterion_type_pb2 import (
    CriterionTypeEnum as google___ads___googleads___v2___enums___criterion_type_pb2___CriterionTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    FloatValue as google___protobuf___wrappers_pb2___FloatValue,
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

class CampaignCriterion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    type = (
        ...
    )  # type: google___ads___googleads___v2___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType
    status = (
        ...
    )  # type: google___ads___googleads___v2___enums___campaign_criterion_status_pb2___CampaignCriterionStatusEnum.CampaignCriterionStatus
    @property
    def campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def bid_modifier(self) -> google___protobuf___wrappers_pb2___FloatValue: ...
    @property
    def negative(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def keyword(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___KeywordInfo: ...
    @property
    def placement(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___PlacementInfo: ...
    @property
    def mobile_app_category(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___MobileAppCategoryInfo: ...
    @property
    def mobile_application(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___MobileApplicationInfo: ...
    @property
    def location(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___LocationInfo: ...
    @property
    def device(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___DeviceInfo: ...
    @property
    def ad_schedule(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___AdScheduleInfo: ...
    @property
    def age_range(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___AgeRangeInfo: ...
    @property
    def gender(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___GenderInfo: ...
    @property
    def income_range(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___IncomeRangeInfo: ...
    @property
    def parental_status(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___ParentalStatusInfo: ...
    @property
    def user_list(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___UserListInfo: ...
    @property
    def youtube_video(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___YouTubeVideoInfo: ...
    @property
    def youtube_channel(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___YouTubeChannelInfo: ...
    @property
    def proximity(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___ProximityInfo: ...
    @property
    def topic(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___TopicInfo: ...
    @property
    def listing_scope(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___ListingScopeInfo: ...
    @property
    def language(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___LanguageInfo: ...
    @property
    def ip_block(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___IpBlockInfo: ...
    @property
    def content_label(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___ContentLabelInfo: ...
    @property
    def carrier(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___CarrierInfo: ...
    @property
    def user_interest(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___UserInterestInfo: ...
    @property
    def webpage(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___WebpageInfo: ...
    @property
    def operating_system_version(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___OperatingSystemVersionInfo: ...
    @property
    def mobile_device(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___MobileDeviceInfo: ...
    @property
    def location_group(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___LocationGroupInfo: ...
    @property
    def custom_affinity(
        self
    ) -> google___ads___googleads___v2___common___criteria_pb2___CustomAffinityInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        bid_modifier: typing___Optional[
            google___protobuf___wrappers_pb2___FloatValue
        ] = None,
        negative: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___campaign_criterion_status_pb2___CampaignCriterionStatusEnum.CampaignCriterionStatus
        ] = None,
        keyword: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___KeywordInfo
        ] = None,
        placement: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___PlacementInfo
        ] = None,
        mobile_app_category: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___MobileAppCategoryInfo
        ] = None,
        mobile_application: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___MobileApplicationInfo
        ] = None,
        location: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___LocationInfo
        ] = None,
        device: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___DeviceInfo
        ] = None,
        ad_schedule: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___AdScheduleInfo
        ] = None,
        age_range: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___AgeRangeInfo
        ] = None,
        gender: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___GenderInfo
        ] = None,
        income_range: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___IncomeRangeInfo
        ] = None,
        parental_status: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___ParentalStatusInfo
        ] = None,
        user_list: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___UserListInfo
        ] = None,
        youtube_video: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___YouTubeVideoInfo
        ] = None,
        youtube_channel: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___YouTubeChannelInfo
        ] = None,
        proximity: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___ProximityInfo
        ] = None,
        topic: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___TopicInfo
        ] = None,
        listing_scope: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___ListingScopeInfo
        ] = None,
        language: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___LanguageInfo
        ] = None,
        ip_block: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___IpBlockInfo
        ] = None,
        content_label: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___ContentLabelInfo
        ] = None,
        carrier: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___CarrierInfo
        ] = None,
        user_interest: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___UserInterestInfo
        ] = None,
        webpage: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___WebpageInfo
        ] = None,
        operating_system_version: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___OperatingSystemVersionInfo
        ] = None,
        mobile_device: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___MobileDeviceInfo
        ] = None,
        location_group: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___LocationGroupInfo
        ] = None,
        custom_affinity: typing___Optional[
            google___ads___googleads___v2___common___criteria_pb2___CustomAffinityInfo
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CampaignCriterion: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CampaignCriterion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_schedule",
            b"ad_schedule",
            "age_range",
            b"age_range",
            "bid_modifier",
            b"bid_modifier",
            "campaign",
            b"campaign",
            "carrier",
            b"carrier",
            "content_label",
            b"content_label",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "custom_affinity",
            b"custom_affinity",
            "device",
            b"device",
            "gender",
            b"gender",
            "income_range",
            b"income_range",
            "ip_block",
            b"ip_block",
            "keyword",
            b"keyword",
            "language",
            b"language",
            "listing_scope",
            b"listing_scope",
            "location",
            b"location",
            "location_group",
            b"location_group",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "mobile_device",
            b"mobile_device",
            "negative",
            b"negative",
            "operating_system_version",
            b"operating_system_version",
            "parental_status",
            b"parental_status",
            "placement",
            b"placement",
            "proximity",
            b"proximity",
            "topic",
            b"topic",
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
            "ad_schedule",
            b"ad_schedule",
            "age_range",
            b"age_range",
            "bid_modifier",
            b"bid_modifier",
            "campaign",
            b"campaign",
            "carrier",
            b"carrier",
            "content_label",
            b"content_label",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "custom_affinity",
            b"custom_affinity",
            "device",
            b"device",
            "gender",
            b"gender",
            "income_range",
            b"income_range",
            "ip_block",
            b"ip_block",
            "keyword",
            b"keyword",
            "language",
            b"language",
            "listing_scope",
            b"listing_scope",
            "location",
            b"location",
            "location_group",
            b"location_group",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "mobile_device",
            b"mobile_device",
            "negative",
            b"negative",
            "operating_system_version",
            b"operating_system_version",
            "parental_status",
            b"parental_status",
            "placement",
            b"placement",
            "proximity",
            b"proximity",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "topic",
            b"topic",
            "type",
            b"type",
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
        "location",
        "device",
        "ad_schedule",
        "age_range",
        "gender",
        "income_range",
        "parental_status",
        "user_list",
        "youtube_video",
        "youtube_channel",
        "proximity",
        "topic",
        "listing_scope",
        "language",
        "ip_block",
        "content_label",
        "carrier",
        "user_interest",
        "webpage",
        "operating_system_version",
        "mobile_device",
        "location_group",
        "custom_affinity",
    ]: ...

global___CampaignCriterion = CampaignCriterion
