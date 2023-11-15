from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v14.enums.types.conversion_origin import ConversionOriginEnum

_M = TypeVar("_M")

class CampaignConversionGoal(proto.Message):
    resource_name: str
    campaign: str
    category: ConversionActionCategoryEnum.ConversionActionCategory
    origin: ConversionOriginEnum.ConversionOrigin
    biddable: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        category: ConversionActionCategoryEnum.ConversionActionCategory = ...,
        origin: ConversionOriginEnum.ConversionOrigin = ...,
        biddable: bool = ...
    ) -> None: ...
