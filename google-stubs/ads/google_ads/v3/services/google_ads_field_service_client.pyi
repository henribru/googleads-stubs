from google.ads.google_ads.v3.proto.services import (
    google_ads_field_service_pb2 as google_ads_field_service_pb2,
)
from google.ads.google_ads.v3.services import (
    google_ads_field_service_client_config as google_ads_field_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    google_ads_field_service_grpc_transport as google_ads_field_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.google_ads_field_service_grpc_transport import (
    GoogleAdsFieldServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import (
    Optional,
    Dict,
    Any,
    List,
    Sequence,
    Tuple,
    Union,
    Callable,
    ClassVar,
    Iterable,
)
from google.ads.google_ads.v3.proto.resources.google_ads_field_pb2 import GoogleAdsField
from google.ads.google_ads.v3.types import GoogleAdsField

class GoogleAdsFieldServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GoogleAdsFieldServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GoogleAdsFieldServiceClient: ...
    @classmethod
    def google_ads_field_path(cls, google_ads_field: Any): ...
    transport: Union[
        GoogleAdsFieldServiceGrpcTransport,
        Callable[[Credentials, type], GoogleAdsFieldServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                GoogleAdsFieldServiceGrpcTransport,
                Callable[[Credentials, type], GoogleAdsFieldServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_google_ads_field(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GoogleAdsField: ...
    def search_google_ads_fields(
        self,
        query: str,
        page_size: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[GoogleAdsField]: ...