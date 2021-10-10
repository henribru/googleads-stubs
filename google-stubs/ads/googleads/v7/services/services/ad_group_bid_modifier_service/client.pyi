from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import ad_group_bid_modifier
from google.ads.googleads.v7.services.types import ad_group_bid_modifier_service

from .transports.base import AdGroupBidModifierServiceTransport

class AdGroupBidModifierServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[AdGroupBidModifierServiceTransport]: ...

class AdGroupBidModifierServiceClient(metaclass=AdGroupBidModifierServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> AdGroupBidModifierServiceTransport: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_bid_modifier_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_bid_modifier_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, AdGroupBidModifierServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_ad_group_bid_modifier(
        self,
        request: ad_group_bid_modifier_service.GetAdGroupBidModifierRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> ad_group_bid_modifier.AdGroupBidModifier: ...
    def mutate_ad_group_bid_modifiers(
        self,
        request: ad_group_bid_modifier_service.MutateAdGroupBidModifiersRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            ad_group_bid_modifier_service.AdGroupBidModifierOperation
        ] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> ad_group_bid_modifier_service.MutateAdGroupBidModifiersResponse: ...
