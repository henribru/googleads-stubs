from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.ad_type_infos import (
    AppAdInfo,
    AppEngagementAdInfo,
    AppPreRegistrationAdInfo,
    CallAdInfo,
    DiscoveryCarouselAdInfo,
    DiscoveryMultiAssetAdInfo,
    DiscoveryVideoResponsiveAdInfo,
    DisplayUploadAdInfo,
    ExpandedDynamicSearchAdInfo,
    ExpandedTextAdInfo,
    HotelAdInfo,
    ImageAdInfo,
    LegacyAppInstallAdInfo,
    LegacyResponsiveDisplayAdInfo,
    LocalAdInfo,
    ResponsiveDisplayAdInfo,
    ResponsiveSearchAdInfo,
    ShoppingComparisonListingAdInfo,
    ShoppingProductAdInfo,
    ShoppingSmartAdInfo,
    SmartCampaignAdInfo,
    TextAdInfo,
    TravelAdInfo,
    VideoAdInfo,
    VideoResponsiveAdInfo,
)
from google.ads.googleads.v15.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v15.common.types.final_app_url import FinalAppUrl
from google.ads.googleads.v15.common.types.url_collection import UrlCollection
from google.ads.googleads.v15.enums.types.ad_type import AdTypeEnum
from google.ads.googleads.v15.enums.types.device import DeviceEnum
from google.ads.googleads.v15.enums.types.system_managed_entity_source import (
    SystemManagedResourceSourceEnum,
)

_M = TypeVar("_M")

class Ad(proto.Message):
    resource_name: str
    id: int
    final_urls: MutableSequence[str]
    final_app_urls: MutableSequence[FinalAppUrl]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    final_url_suffix: str
    url_custom_parameters: MutableSequence[CustomParameter]
    display_url: str
    type_: AdTypeEnum.AdType
    added_by_google_ads: bool
    device_preference: DeviceEnum.Device
    url_collections: MutableSequence[UrlCollection]
    name: str
    system_managed_resource_source: SystemManagedResourceSourceEnum.SystemManagedResourceSource
    text_ad: TextAdInfo
    expanded_text_ad: ExpandedTextAdInfo
    call_ad: CallAdInfo
    expanded_dynamic_search_ad: ExpandedDynamicSearchAdInfo
    hotel_ad: HotelAdInfo
    shopping_smart_ad: ShoppingSmartAdInfo
    shopping_product_ad: ShoppingProductAdInfo
    image_ad: ImageAdInfo
    video_ad: VideoAdInfo
    video_responsive_ad: VideoResponsiveAdInfo
    responsive_search_ad: ResponsiveSearchAdInfo
    legacy_responsive_display_ad: LegacyResponsiveDisplayAdInfo
    app_ad: AppAdInfo
    legacy_app_install_ad: LegacyAppInstallAdInfo
    responsive_display_ad: ResponsiveDisplayAdInfo
    local_ad: LocalAdInfo
    display_upload_ad: DisplayUploadAdInfo
    app_engagement_ad: AppEngagementAdInfo
    shopping_comparison_listing_ad: ShoppingComparisonListingAdInfo
    smart_campaign_ad: SmartCampaignAdInfo
    app_pre_registration_ad: AppPreRegistrationAdInfo
    discovery_multi_asset_ad: DiscoveryMultiAssetAdInfo
    discovery_carousel_ad: DiscoveryCarouselAdInfo
    discovery_video_responsive_ad: DiscoveryVideoResponsiveAdInfo
    travel_ad: TravelAdInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        final_urls: MutableSequence[str] = ...,
        final_app_urls: MutableSequence[FinalAppUrl] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        tracking_url_template: str = ...,
        final_url_suffix: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        display_url: str = ...,
        type_: AdTypeEnum.AdType = ...,
        added_by_google_ads: bool = ...,
        device_preference: DeviceEnum.Device = ...,
        url_collections: MutableSequence[UrlCollection] = ...,
        name: str = ...,
        system_managed_resource_source: SystemManagedResourceSourceEnum.SystemManagedResourceSource = ...,
        text_ad: TextAdInfo = ...,
        expanded_text_ad: ExpandedTextAdInfo = ...,
        call_ad: CallAdInfo = ...,
        expanded_dynamic_search_ad: ExpandedDynamicSearchAdInfo = ...,
        hotel_ad: HotelAdInfo = ...,
        shopping_smart_ad: ShoppingSmartAdInfo = ...,
        shopping_product_ad: ShoppingProductAdInfo = ...,
        image_ad: ImageAdInfo = ...,
        video_ad: VideoAdInfo = ...,
        video_responsive_ad: VideoResponsiveAdInfo = ...,
        responsive_search_ad: ResponsiveSearchAdInfo = ...,
        legacy_responsive_display_ad: LegacyResponsiveDisplayAdInfo = ...,
        app_ad: AppAdInfo = ...,
        legacy_app_install_ad: LegacyAppInstallAdInfo = ...,
        responsive_display_ad: ResponsiveDisplayAdInfo = ...,
        local_ad: LocalAdInfo = ...,
        display_upload_ad: DisplayUploadAdInfo = ...,
        app_engagement_ad: AppEngagementAdInfo = ...,
        shopping_comparison_listing_ad: ShoppingComparisonListingAdInfo = ...,
        smart_campaign_ad: SmartCampaignAdInfo = ...,
        app_pre_registration_ad: AppPreRegistrationAdInfo = ...,
        discovery_multi_asset_ad: DiscoveryMultiAssetAdInfo = ...,
        discovery_carousel_ad: DiscoveryCarouselAdInfo = ...,
        discovery_video_responsive_ad: DiscoveryVideoResponsiveAdInfo = ...,
        travel_ad: TravelAdInfo = ...
    ) -> None: ...
