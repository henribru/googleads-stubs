from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import campaign_service

from .transports.base import CampaignServiceTransport

class CampaignServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CampaignServiceTransport]: ...

class CampaignServiceClient(metaclass=CampaignServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> CampaignServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def accessible_bidding_strategy_path(
        customer_id: str, bidding_strategy_id: str
    ) -> str: ...
    @staticmethod
    def parse_accessible_bidding_strategy_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def bidding_strategy_path(customer_id: str, bidding_strategy_id: str) -> str: ...
    @staticmethod
    def parse_bidding_strategy_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_budget_path(customer_id: str, campaign_budget_id: str) -> str: ...
    @staticmethod
    def parse_campaign_budget_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_group_path(customer_id: str, campaign_group_id: str) -> str: ...
    @staticmethod
    def parse_campaign_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_label_path(
        customer_id: str, campaign_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_feed_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, CampaignServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_campaigns(
        self,
        request: Union[campaign_service.MutateCampaignsRequest, dict] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[campaign_service.CampaignOperation] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_service.MutateCampaignsResponse: ...
