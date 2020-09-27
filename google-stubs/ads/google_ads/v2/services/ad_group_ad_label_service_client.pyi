from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v2.proto.resources import (
    account_budget_pb2 as account_budget_pb2,
    account_budget_proposal_pb2 as account_budget_proposal_pb2,
    ad_group_ad_asset_view_pb2 as ad_group_ad_asset_view_pb2,
    ad_group_ad_label_pb2 as ad_group_ad_label_pb2,
)
from google.ads.google_ads.v2.proto.services import (
    account_budget_proposal_service_pb2 as account_budget_proposal_service_pb2,
    account_budget_proposal_service_pb2_grpc as account_budget_proposal_service_pb2_grpc,
    account_budget_service_pb2 as account_budget_service_pb2,
    account_budget_service_pb2_grpc as account_budget_service_pb2_grpc,
    ad_group_ad_asset_view_service_pb2 as ad_group_ad_asset_view_service_pb2,
    ad_group_ad_asset_view_service_pb2_grpc as ad_group_ad_asset_view_service_pb2_grpc,
    ad_group_ad_label_service_pb2 as ad_group_ad_label_service_pb2,
    ad_group_ad_label_service_pb2_grpc as ad_group_ad_label_service_pb2_grpc,
)
from google.ads.google_ads.v2.services import (
    ad_group_ad_label_service_client_config as ad_group_ad_label_service_client_config,
    enums as enums,
)
from google.ads.google_ads.v2.services.transports import (
    ad_group_ad_label_service_grpc_transport as ad_group_ad_label_service_grpc_transport,
)
from google.ads.google_ads.v2.types import AdGroupAdLabel

class AdGroupAdLabelServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupAdLabelServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupAdLabelServiceClient: ...
    @classmethod
    def ad_group_ad_label_path(cls, customer: Any, ad_group_ad_label: Any) -> str: ...
    transport: Union[
        ad_group_ad_label_service_grpc_transport.AdGroupAdLabelServiceGrpcTransport,
        Callable[
            [Credentials, type],
            ad_group_ad_label_service_grpc_transport.AdGroupAdLabelServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ad_group_ad_label_service_grpc_transport.AdGroupAdLabelServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    ad_group_ad_label_service_grpc_transport.AdGroupAdLabelServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_ad_label(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupAdLabel: ...
    def mutate_ad_group_ad_labels(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], ad_group_ad_label_service_pb2.AdGroupAdLabelOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ad_group_ad_label_service_pb2.MutateAdGroupAdLabelsResponse: ...
