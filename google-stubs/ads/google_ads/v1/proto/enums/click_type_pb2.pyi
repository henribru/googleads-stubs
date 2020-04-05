# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)


builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ClickTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ClickType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'ClickTypeEnum.ClickType': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['ClickTypeEnum.ClickType']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ClickTypeEnum.ClickType']]: ...
        UNSPECIFIED = typing___cast('ClickTypeEnum.ClickType', 0)
        UNKNOWN = typing___cast('ClickTypeEnum.ClickType', 1)
        APP_DEEPLINK = typing___cast('ClickTypeEnum.ClickType', 2)
        BREADCRUMBS = typing___cast('ClickTypeEnum.ClickType', 3)
        BROADBAND_PLAN = typing___cast('ClickTypeEnum.ClickType', 4)
        CALL_TRACKING = typing___cast('ClickTypeEnum.ClickType', 5)
        CALLS = typing___cast('ClickTypeEnum.ClickType', 6)
        CLICK_ON_ENGAGEMENT_AD = typing___cast('ClickTypeEnum.ClickType', 7)
        GET_DIRECTIONS = typing___cast('ClickTypeEnum.ClickType', 8)
        LOCATION_EXPANSION = typing___cast('ClickTypeEnum.ClickType', 9)
        LOCATION_FORMAT_CALL = typing___cast('ClickTypeEnum.ClickType', 10)
        LOCATION_FORMAT_DIRECTIONS = typing___cast('ClickTypeEnum.ClickType', 11)
        LOCATION_FORMAT_IMAGE = typing___cast('ClickTypeEnum.ClickType', 12)
        LOCATION_FORMAT_LANDING_PAGE = typing___cast('ClickTypeEnum.ClickType', 13)
        LOCATION_FORMAT_MAP = typing___cast('ClickTypeEnum.ClickType', 14)
        LOCATION_FORMAT_STORE_INFO = typing___cast('ClickTypeEnum.ClickType', 15)
        LOCATION_FORMAT_TEXT = typing___cast('ClickTypeEnum.ClickType', 16)
        MOBILE_CALL_TRACKING = typing___cast('ClickTypeEnum.ClickType', 17)
        OFFER_PRINTS = typing___cast('ClickTypeEnum.ClickType', 18)
        OTHER = typing___cast('ClickTypeEnum.ClickType', 19)
        PRODUCT_EXTENSION_CLICKS = typing___cast('ClickTypeEnum.ClickType', 20)
        PRODUCT_LISTING_AD_CLICKS = typing___cast('ClickTypeEnum.ClickType', 21)
        SITELINKS = typing___cast('ClickTypeEnum.ClickType', 22)
        STORE_LOCATOR = typing___cast('ClickTypeEnum.ClickType', 23)
        URL_CLICKS = typing___cast('ClickTypeEnum.ClickType', 25)
        VIDEO_APP_STORE_CLICKS = typing___cast('ClickTypeEnum.ClickType', 26)
        VIDEO_CALL_TO_ACTION_CLICKS = typing___cast('ClickTypeEnum.ClickType', 27)
        VIDEO_CARD_ACTION_HEADLINE_CLICKS = typing___cast('ClickTypeEnum.ClickType', 28)
        VIDEO_END_CAP_CLICKS = typing___cast('ClickTypeEnum.ClickType', 29)
        VIDEO_WEBSITE_CLICKS = typing___cast('ClickTypeEnum.ClickType', 30)
        VISUAL_SITELINKS = typing___cast('ClickTypeEnum.ClickType', 31)
        WIRELESS_PLAN = typing___cast('ClickTypeEnum.ClickType', 32)
        PRODUCT_LISTING_AD_LOCAL = typing___cast('ClickTypeEnum.ClickType', 33)
        PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL = typing___cast('ClickTypeEnum.ClickType', 34)
        PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE = typing___cast('ClickTypeEnum.ClickType', 35)
        PRODUCT_LISTING_ADS_COUPON = typing___cast('ClickTypeEnum.ClickType', 36)
        PRODUCT_LISTING_AD_TRANSACTABLE = typing___cast('ClickTypeEnum.ClickType', 37)
        PRODUCT_AD_APP_DEEPLINK = typing___cast('ClickTypeEnum.ClickType', 38)
        SHOWCASE_AD_CATEGORY_LINK = typing___cast('ClickTypeEnum.ClickType', 39)
        SHOWCASE_AD_LOCAL_STOREFRONT_LINK = typing___cast('ClickTypeEnum.ClickType', 40)
        SHOWCASE_AD_ONLINE_PRODUCT_LINK = typing___cast('ClickTypeEnum.ClickType', 42)
        SHOWCASE_AD_LOCAL_PRODUCT_LINK = typing___cast('ClickTypeEnum.ClickType', 43)
        PROMOTION_EXTENSION = typing___cast('ClickTypeEnum.ClickType', 44)
        SWIPEABLE_GALLERY_AD_HEADLINE = typing___cast('ClickTypeEnum.ClickType', 45)
        SWIPEABLE_GALLERY_AD_SWIPES = typing___cast('ClickTypeEnum.ClickType', 46)
        SWIPEABLE_GALLERY_AD_SEE_MORE = typing___cast('ClickTypeEnum.ClickType', 47)
        SWIPEABLE_GALLERY_AD_SITELINK_ONE = typing___cast('ClickTypeEnum.ClickType', 48)
        SWIPEABLE_GALLERY_AD_SITELINK_TWO = typing___cast('ClickTypeEnum.ClickType', 49)
        SWIPEABLE_GALLERY_AD_SITELINK_THREE = typing___cast('ClickTypeEnum.ClickType', 50)
        SWIPEABLE_GALLERY_AD_SITELINK_FOUR = typing___cast('ClickTypeEnum.ClickType', 51)
        SWIPEABLE_GALLERY_AD_SITELINK_FIVE = typing___cast('ClickTypeEnum.ClickType', 52)
        HOTEL_PRICE = typing___cast('ClickTypeEnum.ClickType', 53)
        PRICE_EXTENSION = typing___cast('ClickTypeEnum.ClickType', 54)
        HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION = typing___cast('ClickTypeEnum.ClickType', 55)
        SHOPPING_COMPARISON_LISTING = typing___cast('ClickTypeEnum.ClickType', 56)
    UNSPECIFIED = typing___cast('ClickTypeEnum.ClickType', 0)
    UNKNOWN = typing___cast('ClickTypeEnum.ClickType', 1)
    APP_DEEPLINK = typing___cast('ClickTypeEnum.ClickType', 2)
    BREADCRUMBS = typing___cast('ClickTypeEnum.ClickType', 3)
    BROADBAND_PLAN = typing___cast('ClickTypeEnum.ClickType', 4)
    CALL_TRACKING = typing___cast('ClickTypeEnum.ClickType', 5)
    CALLS = typing___cast('ClickTypeEnum.ClickType', 6)
    CLICK_ON_ENGAGEMENT_AD = typing___cast('ClickTypeEnum.ClickType', 7)
    GET_DIRECTIONS = typing___cast('ClickTypeEnum.ClickType', 8)
    LOCATION_EXPANSION = typing___cast('ClickTypeEnum.ClickType', 9)
    LOCATION_FORMAT_CALL = typing___cast('ClickTypeEnum.ClickType', 10)
    LOCATION_FORMAT_DIRECTIONS = typing___cast('ClickTypeEnum.ClickType', 11)
    LOCATION_FORMAT_IMAGE = typing___cast('ClickTypeEnum.ClickType', 12)
    LOCATION_FORMAT_LANDING_PAGE = typing___cast('ClickTypeEnum.ClickType', 13)
    LOCATION_FORMAT_MAP = typing___cast('ClickTypeEnum.ClickType', 14)
    LOCATION_FORMAT_STORE_INFO = typing___cast('ClickTypeEnum.ClickType', 15)
    LOCATION_FORMAT_TEXT = typing___cast('ClickTypeEnum.ClickType', 16)
    MOBILE_CALL_TRACKING = typing___cast('ClickTypeEnum.ClickType', 17)
    OFFER_PRINTS = typing___cast('ClickTypeEnum.ClickType', 18)
    OTHER = typing___cast('ClickTypeEnum.ClickType', 19)
    PRODUCT_EXTENSION_CLICKS = typing___cast('ClickTypeEnum.ClickType', 20)
    PRODUCT_LISTING_AD_CLICKS = typing___cast('ClickTypeEnum.ClickType', 21)
    SITELINKS = typing___cast('ClickTypeEnum.ClickType', 22)
    STORE_LOCATOR = typing___cast('ClickTypeEnum.ClickType', 23)
    URL_CLICKS = typing___cast('ClickTypeEnum.ClickType', 25)
    VIDEO_APP_STORE_CLICKS = typing___cast('ClickTypeEnum.ClickType', 26)
    VIDEO_CALL_TO_ACTION_CLICKS = typing___cast('ClickTypeEnum.ClickType', 27)
    VIDEO_CARD_ACTION_HEADLINE_CLICKS = typing___cast('ClickTypeEnum.ClickType', 28)
    VIDEO_END_CAP_CLICKS = typing___cast('ClickTypeEnum.ClickType', 29)
    VIDEO_WEBSITE_CLICKS = typing___cast('ClickTypeEnum.ClickType', 30)
    VISUAL_SITELINKS = typing___cast('ClickTypeEnum.ClickType', 31)
    WIRELESS_PLAN = typing___cast('ClickTypeEnum.ClickType', 32)
    PRODUCT_LISTING_AD_LOCAL = typing___cast('ClickTypeEnum.ClickType', 33)
    PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL = typing___cast('ClickTypeEnum.ClickType', 34)
    PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE = typing___cast('ClickTypeEnum.ClickType', 35)
    PRODUCT_LISTING_ADS_COUPON = typing___cast('ClickTypeEnum.ClickType', 36)
    PRODUCT_LISTING_AD_TRANSACTABLE = typing___cast('ClickTypeEnum.ClickType', 37)
    PRODUCT_AD_APP_DEEPLINK = typing___cast('ClickTypeEnum.ClickType', 38)
    SHOWCASE_AD_CATEGORY_LINK = typing___cast('ClickTypeEnum.ClickType', 39)
    SHOWCASE_AD_LOCAL_STOREFRONT_LINK = typing___cast('ClickTypeEnum.ClickType', 40)
    SHOWCASE_AD_ONLINE_PRODUCT_LINK = typing___cast('ClickTypeEnum.ClickType', 42)
    SHOWCASE_AD_LOCAL_PRODUCT_LINK = typing___cast('ClickTypeEnum.ClickType', 43)
    PROMOTION_EXTENSION = typing___cast('ClickTypeEnum.ClickType', 44)
    SWIPEABLE_GALLERY_AD_HEADLINE = typing___cast('ClickTypeEnum.ClickType', 45)
    SWIPEABLE_GALLERY_AD_SWIPES = typing___cast('ClickTypeEnum.ClickType', 46)
    SWIPEABLE_GALLERY_AD_SEE_MORE = typing___cast('ClickTypeEnum.ClickType', 47)
    SWIPEABLE_GALLERY_AD_SITELINK_ONE = typing___cast('ClickTypeEnum.ClickType', 48)
    SWIPEABLE_GALLERY_AD_SITELINK_TWO = typing___cast('ClickTypeEnum.ClickType', 49)
    SWIPEABLE_GALLERY_AD_SITELINK_THREE = typing___cast('ClickTypeEnum.ClickType', 50)
    SWIPEABLE_GALLERY_AD_SITELINK_FOUR = typing___cast('ClickTypeEnum.ClickType', 51)
    SWIPEABLE_GALLERY_AD_SITELINK_FIVE = typing___cast('ClickTypeEnum.ClickType', 52)
    HOTEL_PRICE = typing___cast('ClickTypeEnum.ClickType', 53)
    PRICE_EXTENSION = typing___cast('ClickTypeEnum.ClickType', 54)
    HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION = typing___cast('ClickTypeEnum.ClickType', 55)
    SHOPPING_COMPARISON_LISTING = typing___cast('ClickTypeEnum.ClickType', 56)
    global___ClickType = ClickType


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ClickTypeEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ClickTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___ClickTypeEnum = ClickTypeEnum
