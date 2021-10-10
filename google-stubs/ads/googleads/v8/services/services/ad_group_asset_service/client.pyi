from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import ad_group_asset
from google.ads.googleads.v8.services.types import ad_group_asset_service

from .transports.base import AdGroupAssetServiceTransport

class AdGroupAssetServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[AdGroupAssetServiceTransport]: ...

class AdGroupAssetServiceClient(metaclass=AdGroupAssetServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> AdGroupAssetServiceTransport: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_asset_path(
        customer_id: str, ad_group_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_path(customer_id: str, asset_id: str) -> str: ...
    @staticmethod
    def parse_asset_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, AdGroupAssetServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_ad_group_asset(
        self,
        request: ad_group_asset_service.GetAdGroupAssetRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> ad_group_asset.AdGroupAsset: ...
    def mutate_ad_group_assets(
        self,
        request: ad_group_asset_service.MutateAdGroupAssetsRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[ad_group_asset_service.AdGroupAssetOperation] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> ad_group_asset_service.MutateAdGroupAssetsResponse: ...
