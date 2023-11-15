from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import ad_group_ad_label_service

from .transports.base import AdGroupAdLabelServiceTransport

class AdGroupAdLabelServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = None
    ) -> Type[AdGroupAdLabelServiceTransport]: ...

class AdGroupAdLabelServiceClient(metaclass=AdGroupAdLabelServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AdGroupAdLabelServiceTransport: ...
    def __enter__(self) -> AdGroupAdLabelServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def ad_group_ad_path(customer_id: str, ad_group_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_ad_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_ad_label_path(
        customer_id: str, ad_group_id: str, ad_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_ad_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def label_path(customer_id: str, label_id: str) -> str: ...
    @staticmethod
    def parse_label_path(path: str) -> Dict[str, str]: ...
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
        transport: Optional[Union[str, AdGroupAdLabelServiceTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_ad_group_ad_labels(
        self,
        request: Optional[
            Union[ad_group_ad_label_service.MutateAdGroupAdLabelsRequest, dict]
        ] = None,
        *,
        customer_id: Optional[str] = None,
        operations: Optional[
            MutableSequence[ad_group_ad_label_service.AdGroupAdLabelOperation]
        ] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> ad_group_ad_label_service.MutateAdGroupAdLabelsResponse: ...
