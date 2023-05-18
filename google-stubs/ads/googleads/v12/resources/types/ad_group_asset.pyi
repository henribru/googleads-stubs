from typing import Any

import proto

from google.ads.googleads.v12.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v12.enums.types.asset_link_status import AssetLinkStatusEnum
from google.ads.googleads.v12.enums.types.asset_source import AssetSourceEnum

class AdGroupAsset(proto.Message):
    resource_name: str
    ad_group: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    source: AssetSourceEnum.AssetSource
    status: AssetLinkStatusEnum.AssetLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        source: AssetSourceEnum.AssetSource = ...,
        status: AssetLinkStatusEnum.AssetLinkStatus = ...
    ) -> None: ...