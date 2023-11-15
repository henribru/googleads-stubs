from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    operation,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.resources.types import offline_user_data_job
from google.ads.googleads.v13.services.types import offline_user_data_job_service

from .transports.base import OfflineUserDataJobServiceTransport

class OfflineUserDataJobServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = None
    ) -> Type[OfflineUserDataJobServiceTransport]: ...

class OfflineUserDataJobServiceClient(metaclass=OfflineUserDataJobServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> OfflineUserDataJobServiceTransport: ...
    def __enter__(self) -> OfflineUserDataJobServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def offline_user_data_job_path(
        customer_id: str, offline_user_data_update_id: str
    ) -> str: ...
    @staticmethod
    def parse_offline_user_data_job_path(path: str) -> Dict[str, str]: ...
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
        transport: Optional[Union[str, OfflineUserDataJobServiceTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def create_offline_user_data_job(
        self,
        request: Optional[
            Union[offline_user_data_job_service.CreateOfflineUserDataJobRequest, dict]
        ] = None,
        *,
        customer_id: Optional[str] = None,
        job: Optional[offline_user_data_job.OfflineUserDataJob] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> offline_user_data_job_service.CreateOfflineUserDataJobResponse: ...
    def add_offline_user_data_job_operations(
        self,
        request: Optional[
            Union[
                offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest,
                dict,
            ]
        ] = None,
        *,
        resource_name: Optional[str] = None,
        operations: Optional[
            MutableSequence[offline_user_data_job_service.OfflineUserDataJobOperation]
        ] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse: ...
    def run_offline_user_data_job(
        self,
        request: Optional[
            Union[offline_user_data_job_service.RunOfflineUserDataJobRequest, dict]
        ] = None,
        *,
        resource_name: Optional[str] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> operation.Operation: ...
