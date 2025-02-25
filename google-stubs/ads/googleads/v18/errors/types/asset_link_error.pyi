from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetLinkErrorEnum(proto.Message):
    class AssetLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PINNING_UNSUPPORTED = 2
        UNSUPPORTED_FIELD_TYPE = 3
        FIELD_TYPE_INCOMPATIBLE_WITH_ASSET_TYPE = 4
        FIELD_TYPE_INCOMPATIBLE_WITH_CAMPAIGN_TYPE = 5
        INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE = 6
        IMAGE_NOT_WITHIN_SPECIFIED_DIMENSION_RANGE = 7
        INVALID_PINNED_FIELD = 8
        MEDIA_BUNDLE_ASSET_FILE_SIZE_TOO_LARGE = 9
        NOT_ENOUGH_AVAILABLE_ASSET_LINKS_FOR_VALID_COMBINATION = 10
        NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK = 11
        NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK_FOR_VALID_COMBINATION = 12
        YOUTUBE_VIDEO_REMOVED = 13
        YOUTUBE_VIDEO_TOO_LONG = 14
        YOUTUBE_VIDEO_TOO_SHORT = 15
        EXCLUDED_PARENT_FIELD_TYPE = 16
        INVALID_STATUS = 17
        YOUTUBE_VIDEO_DURATION_NOT_DEFINED = 18
        CANNOT_CREATE_AUTOMATICALLY_CREATED_LINKS = 19
        CANNOT_LINK_TO_AUTOMATICALLY_CREATED_ASSET = 20
        CANNOT_MODIFY_ASSET_LINK_SOURCE = 21
        CANNOT_LINK_LOCATION_LEAD_FORM_WITHOUT_LOCATION_ASSET = 22
        CUSTOMER_NOT_VERIFIED = 23
        UNSUPPORTED_CALL_TO_ACTION = 24
        BRAND_ASSETS_NOT_LINKED_AT_ASSET_GROUP_LEVEL = 25
        BRAND_ASSETS_NOT_LINKED_AT_CAMPAIGN_LEVEL = 26

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
