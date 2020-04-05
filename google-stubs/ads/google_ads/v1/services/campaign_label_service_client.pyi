import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.campaign_label_service_grpc_transport import (
    CampaignLabelServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.campaign_label_pb2 import CampaignLabel
from google.ads.google_ads.v1.proto.services.campaign_label_service_pb2 import (
    CampaignLabelOperation,
    MutateCampaignLabelsResponse,
)

class CampaignLabelServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignLabelServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignLabelServiceClient: ...
    @classmethod
    def campaign_label_path(cls, customer: Any, campaign_label: Any) -> str: ...
    transport: Union[
        CampaignLabelServiceGrpcTransport,
        Callable[[Credentials, type], CampaignLabelServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignLabelServiceGrpcTransport,
                Callable[[Credentials, type], CampaignLabelServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_label(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignLabel: ...
    def mutate_campaign_labels(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignLabelOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignLabelsResponse: ...
