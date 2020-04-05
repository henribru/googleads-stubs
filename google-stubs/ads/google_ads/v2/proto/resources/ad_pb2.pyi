# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.ad_type_infos_pb2 import (
    AppAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___AppAdInfo,
    AppEngagementAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___AppEngagementAdInfo,
    CallOnlyAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___CallOnlyAdInfo,
    DisplayUploadAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___DisplayUploadAdInfo,
    ExpandedDynamicSearchAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ExpandedDynamicSearchAdInfo,
    ExpandedTextAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ExpandedTextAdInfo,
    GmailAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___GmailAdInfo,
    HotelAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___HotelAdInfo,
    ImageAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ImageAdInfo,
    LegacyAppInstallAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___LegacyAppInstallAdInfo,
    LegacyResponsiveDisplayAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___LegacyResponsiveDisplayAdInfo,
    ResponsiveDisplayAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ResponsiveDisplayAdInfo,
    ResponsiveSearchAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ResponsiveSearchAdInfo,
    ShoppingComparisonListingAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingComparisonListingAdInfo,
    ShoppingProductAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingProductAdInfo,
    ShoppingSmartAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingSmartAdInfo,
    TextAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___TextAdInfo,
    VideoAdInfo as google___ads___googleads___v2___common___ad_type_infos_pb2___VideoAdInfo,
)

from google.ads.google_ads.v2.proto.common.custom_parameter_pb2 import (
    CustomParameter as google___ads___googleads___v2___common___custom_parameter_pb2___CustomParameter,
)

from google.ads.google_ads.v2.proto.common.final_app_url_pb2 import (
    FinalAppUrl as google___ads___googleads___v2___common___final_app_url_pb2___FinalAppUrl,
)

from google.ads.google_ads.v2.proto.common.url_collection_pb2 import (
    UrlCollection as google___ads___googleads___v2___common___url_collection_pb2___UrlCollection,
)

from google.ads.google_ads.v2.proto.enums.ad_type_pb2 import (
    AdTypeEnum as google___ads___googleads___v2___enums___ad_type_pb2___AdTypeEnum,
)

from google.ads.google_ads.v2.proto.enums.device_pb2 import (
    DeviceEnum as google___ads___googleads___v2___enums___device_pb2___DeviceEnum,
)

from google.ads.google_ads.v2.proto.enums.system_managed_entity_source_pb2 import (
    SystemManagedResourceSourceEnum as google___ads___googleads___v2___enums___system_managed_entity_source_pb2___SystemManagedResourceSourceEnum,
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

class Ad(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    type = (
        ...
    )  # type: google___ads___googleads___v2___enums___ad_type_pb2___AdTypeEnum.AdType
    device_preference = (
        ...
    )  # type: google___ads___googleads___v2___enums___device_pb2___DeviceEnum.Device
    system_managed_resource_source = (
        ...
    )  # type: google___ads___googleads___v2___enums___system_managed_entity_source_pb2___SystemManagedResourceSourceEnum.SystemManagedResourceSource
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def final_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_app_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v2___common___final_app_url_pb2___FinalAppUrl
    ]: ...
    @property
    def final_mobile_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def tracking_url_template(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v2___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def display_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def added_by_google_ads(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def url_collections(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v2___common___url_collection_pb2___UrlCollection
    ]: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def text_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___TextAdInfo: ...
    @property
    def expanded_text_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ExpandedTextAdInfo: ...
    @property
    def call_only_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___CallOnlyAdInfo: ...
    @property
    def expanded_dynamic_search_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ExpandedDynamicSearchAdInfo: ...
    @property
    def hotel_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___HotelAdInfo: ...
    @property
    def shopping_smart_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingSmartAdInfo: ...
    @property
    def shopping_product_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingProductAdInfo: ...
    @property
    def gmail_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___GmailAdInfo: ...
    @property
    def image_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ImageAdInfo: ...
    @property
    def video_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___VideoAdInfo: ...
    @property
    def responsive_search_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ResponsiveSearchAdInfo: ...
    @property
    def legacy_responsive_display_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___LegacyResponsiveDisplayAdInfo: ...
    @property
    def app_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___AppAdInfo: ...
    @property
    def legacy_app_install_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___LegacyAppInstallAdInfo: ...
    @property
    def responsive_display_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ResponsiveDisplayAdInfo: ...
    @property
    def display_upload_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___DisplayUploadAdInfo: ...
    @property
    def app_engagement_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___AppEngagementAdInfo: ...
    @property
    def shopping_comparison_listing_ad(
        self,
    ) -> google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingComparisonListingAdInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        final_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_app_urls: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v2___common___final_app_url_pb2___FinalAppUrl
            ]
        ] = None,
        final_mobile_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v2___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        display_url: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___ad_type_pb2___AdTypeEnum.AdType
        ] = None,
        added_by_google_ads: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        device_preference: typing___Optional[
            google___ads___googleads___v2___enums___device_pb2___DeviceEnum.Device
        ] = None,
        url_collections: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v2___common___url_collection_pb2___UrlCollection
            ]
        ] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        system_managed_resource_source: typing___Optional[
            google___ads___googleads___v2___enums___system_managed_entity_source_pb2___SystemManagedResourceSourceEnum.SystemManagedResourceSource
        ] = None,
        text_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___TextAdInfo
        ] = None,
        expanded_text_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ExpandedTextAdInfo
        ] = None,
        call_only_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___CallOnlyAdInfo
        ] = None,
        expanded_dynamic_search_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ExpandedDynamicSearchAdInfo
        ] = None,
        hotel_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___HotelAdInfo
        ] = None,
        shopping_smart_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingSmartAdInfo
        ] = None,
        shopping_product_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingProductAdInfo
        ] = None,
        gmail_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___GmailAdInfo
        ] = None,
        image_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ImageAdInfo
        ] = None,
        video_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___VideoAdInfo
        ] = None,
        responsive_search_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ResponsiveSearchAdInfo
        ] = None,
        legacy_responsive_display_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___LegacyResponsiveDisplayAdInfo
        ] = None,
        app_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___AppAdInfo
        ] = None,
        legacy_app_install_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___LegacyAppInstallAdInfo
        ] = None,
        responsive_display_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ResponsiveDisplayAdInfo
        ] = None,
        display_upload_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___DisplayUploadAdInfo
        ] = None,
        app_engagement_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___AppEngagementAdInfo
        ] = None,
        shopping_comparison_listing_ad: typing___Optional[
            google___ads___googleads___v2___common___ad_type_infos_pb2___ShoppingComparisonListingAdInfo
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Ad: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Ad: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_data",
            b"ad_data",
            "added_by_google_ads",
            b"added_by_google_ads",
            "app_ad",
            b"app_ad",
            "app_engagement_ad",
            b"app_engagement_ad",
            "call_only_ad",
            b"call_only_ad",
            "display_upload_ad",
            b"display_upload_ad",
            "display_url",
            b"display_url",
            "expanded_dynamic_search_ad",
            b"expanded_dynamic_search_ad",
            "expanded_text_ad",
            b"expanded_text_ad",
            "final_url_suffix",
            b"final_url_suffix",
            "gmail_ad",
            b"gmail_ad",
            "hotel_ad",
            b"hotel_ad",
            "id",
            b"id",
            "image_ad",
            b"image_ad",
            "legacy_app_install_ad",
            b"legacy_app_install_ad",
            "legacy_responsive_display_ad",
            b"legacy_responsive_display_ad",
            "name",
            b"name",
            "responsive_display_ad",
            b"responsive_display_ad",
            "responsive_search_ad",
            b"responsive_search_ad",
            "shopping_comparison_listing_ad",
            b"shopping_comparison_listing_ad",
            "shopping_product_ad",
            b"shopping_product_ad",
            "shopping_smart_ad",
            b"shopping_smart_ad",
            "text_ad",
            b"text_ad",
            "tracking_url_template",
            b"tracking_url_template",
            "video_ad",
            b"video_ad",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_data",
            b"ad_data",
            "added_by_google_ads",
            b"added_by_google_ads",
            "app_ad",
            b"app_ad",
            "app_engagement_ad",
            b"app_engagement_ad",
            "call_only_ad",
            b"call_only_ad",
            "device_preference",
            b"device_preference",
            "display_upload_ad",
            b"display_upload_ad",
            "display_url",
            b"display_url",
            "expanded_dynamic_search_ad",
            b"expanded_dynamic_search_ad",
            "expanded_text_ad",
            b"expanded_text_ad",
            "final_app_urls",
            b"final_app_urls",
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_url_suffix",
            b"final_url_suffix",
            "final_urls",
            b"final_urls",
            "gmail_ad",
            b"gmail_ad",
            "hotel_ad",
            b"hotel_ad",
            "id",
            b"id",
            "image_ad",
            b"image_ad",
            "legacy_app_install_ad",
            b"legacy_app_install_ad",
            "legacy_responsive_display_ad",
            b"legacy_responsive_display_ad",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "responsive_display_ad",
            b"responsive_display_ad",
            "responsive_search_ad",
            b"responsive_search_ad",
            "shopping_comparison_listing_ad",
            b"shopping_comparison_listing_ad",
            "shopping_product_ad",
            b"shopping_product_ad",
            "shopping_smart_ad",
            b"shopping_smart_ad",
            "system_managed_resource_source",
            b"system_managed_resource_source",
            "text_ad",
            b"text_ad",
            "tracking_url_template",
            b"tracking_url_template",
            "type",
            b"type",
            "url_collections",
            b"url_collections",
            "url_custom_parameters",
            b"url_custom_parameters",
            "video_ad",
            b"video_ad",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["ad_data", b"ad_data"]
    ) -> typing_extensions___Literal[
        "text_ad",
        "expanded_text_ad",
        "call_only_ad",
        "expanded_dynamic_search_ad",
        "hotel_ad",
        "shopping_smart_ad",
        "shopping_product_ad",
        "gmail_ad",
        "image_ad",
        "video_ad",
        "responsive_search_ad",
        "legacy_responsive_display_ad",
        "app_ad",
        "legacy_app_install_ad",
        "responsive_display_ad",
        "display_upload_ad",
        "app_engagement_ad",
        "shopping_comparison_listing_ad",
    ]: ...

global___Ad = Ad
