from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import billing_setup_service

from .transports.base import BillingSetupServiceTransport

class BillingSetupServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = None
    ) -> Type[BillingSetupServiceTransport]: ...

class BillingSetupServiceClient(metaclass=BillingSetupServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> BillingSetupServiceTransport: ...
    def __enter__(self) -> BillingSetupServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def billing_setup_path(customer_id: str, billing_setup_id: str) -> str: ...
    @staticmethod
    def parse_billing_setup_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def payments_account_path(customer_id: str, payments_account_id: str) -> str: ...
    @staticmethod
    def parse_payments_account_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[Union[str, BillingSetupServiceTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_billing_setup(
        self,
        request: Optional[
            Union[billing_setup_service.MutateBillingSetupRequest, dict]
        ] = None,
        *,
        customer_id: Optional[str] = None,
        operation: Optional[billing_setup_service.BillingSetupOperation] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> billing_setup_service.MutateBillingSetupResponse: ...
