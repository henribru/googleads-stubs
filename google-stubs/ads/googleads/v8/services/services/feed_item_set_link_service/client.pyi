from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import feed_item_set_link
from google.ads.googleads.v8.services.types import feed_item_set_link_service

from .transports.base import FeedItemSetLinkServiceTransport

class FeedItemSetLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[FeedItemSetLinkServiceTransport]: ...

class FeedItemSetLinkServiceClient(metaclass=FeedItemSetLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> FeedItemSetLinkServiceTransport: ...
    @staticmethod
    def feed_item_path(customer_id: str, feed_id: str, feed_item_id: str) -> str: ...
    @staticmethod
    def parse_feed_item_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_item_set_path(
        customer_id: str, feed_id: str, feed_item_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_item_set_link_path(
        customer_id: str, feed_id: str, feed_item_set_id: str, feed_item_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_link_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, FeedItemSetLinkServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_feed_item_set_link(
        self,
        request: feed_item_set_link_service.GetFeedItemSetLinkRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> feed_item_set_link.FeedItemSetLink: ...
    def mutate_feed_item_set_links(
        self,
        request: feed_item_set_link_service.MutateFeedItemSetLinksRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[feed_item_set_link_service.FeedItemSetLinkOperation] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> feed_item_set_link_service.MutateFeedItemSetLinksResponse: ...
