from typing import Any

import proto

from google.ads.googleads.v15.enums.types.linked_product_type import (
    LinkedProductTypeEnum,
)
from google.ads.googleads.v15.enums.types.product_link_invitation_status import (
    ProductLinkInvitationStatusEnum,
)

class HotelCenterLinkInvitationIdentifier(proto.Message):
    hotel_center_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        hotel_center_id: int = ...
    ) -> None: ...

class MerchantCenterLinkInvitationIdentifier(proto.Message):
    merchant_center_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        merchant_center_id: int = ...
    ) -> None: ...

class ProductLinkInvitation(proto.Message):
    resource_name: str
    product_link_invitation_id: int
    status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    type_: LinkedProductTypeEnum.LinkedProductType
    hotel_center: HotelCenterLinkInvitationIdentifier
    merchant_center: MerchantCenterLinkInvitationIdentifier
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        product_link_invitation_id: int = ...,
        status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus = ...,
        type_: LinkedProductTypeEnum.LinkedProductType = ...,
        hotel_center: HotelCenterLinkInvitationIdentifier = ...,
        merchant_center: MerchantCenterLinkInvitationIdentifier = ...
    ) -> None: ...