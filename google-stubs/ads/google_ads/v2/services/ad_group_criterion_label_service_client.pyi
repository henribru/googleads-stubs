import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.ad_group_criterion_label_service_grpc_transport import (
    AdGroupCriterionLabelServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.ad_group_criterion_label_pb2 import (
    AdGroupCriterionLabel,
)
from google.ads.google_ads.v2.proto.services.ad_group_criterion_label_service_pb2 import (
    AdGroupCriterionLabelOperation,
    MutateAdGroupCriterionLabelsResponse,
)

class AdGroupCriterionLabelServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionLabelServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionLabelServiceClient: ...
    @classmethod
    def ad_group_criterion_label_path(
        cls, customer: Any, ad_group_criterion_label: Any
    ) -> str: ...
    transport: Union[
        AdGroupCriterionLabelServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupCriterionLabelServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupCriterionLabelServiceGrpcTransport,
                Callable[
                    [Credentials, type], AdGroupCriterionLabelServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_criterion_label(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupCriterionLabel: ...
    def mutate_ad_group_criterion_labels(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], AdGroupCriterionLabelOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAdGroupCriterionLabelsResponse: ...
