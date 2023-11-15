import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import customer_service

class CustomerServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_customer(
        self,
    ) -> Callable[
        [customer_service.MutateCustomerRequest],
        Union[
            customer_service.MutateCustomerResponse,
            Awaitable[customer_service.MutateCustomerResponse],
        ],
    ]: ...
    @property
    def list_accessible_customers(
        self,
    ) -> Callable[
        [customer_service.ListAccessibleCustomersRequest],
        Union[
            customer_service.ListAccessibleCustomersResponse,
            Awaitable[customer_service.ListAccessibleCustomersResponse],
        ],
    ]: ...
    @property
    def create_customer_client(
        self,
    ) -> Callable[
        [customer_service.CreateCustomerClientRequest],
        Union[
            customer_service.CreateCustomerClientResponse,
            Awaitable[customer_service.CreateCustomerClientResponse],
        ],
    ]: ...
