from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.placeholder_type import PlaceholderTypeEnum

_M = TypeVar("_M")

class FeedPlaceholderView(proto.Message):
    resource_name: str
    placeholder_type: PlaceholderTypeEnum.PlaceholderType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        placeholder_type: PlaceholderTypeEnum.PlaceholderType = ...
    ) -> None: ...
