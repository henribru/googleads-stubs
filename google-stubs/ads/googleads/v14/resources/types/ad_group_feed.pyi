from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.matching_function import MatchingFunction
from google.ads.googleads.v14.enums.types.feed_link_status import FeedLinkStatusEnum
from google.ads.googleads.v14.enums.types.placeholder_type import PlaceholderTypeEnum

_M = TypeVar("_M")

class AdGroupFeed(proto.Message):
    resource_name: str
    feed: str
    ad_group: str
    placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType]
    matching_function: MatchingFunction
    status: FeedLinkStatusEnum.FeedLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed: str = ...,
        ad_group: str = ...,
        placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType] = ...,
        matching_function: MatchingFunction = ...,
        status: FeedLinkStatusEnum.FeedLinkStatus = ...
    ) -> None: ...
