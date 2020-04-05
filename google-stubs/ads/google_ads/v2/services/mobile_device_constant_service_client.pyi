import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.mobile_device_constant_service_grpc_transport import (
    MobileDeviceConstantServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.mobile_device_constant_pb2 import (
    MobileDeviceConstant,
)

class MobileDeviceConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MobileDeviceConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MobileDeviceConstantServiceClient: ...
    @classmethod
    def mobile_device_constant_path(cls, mobile_device_constant: Any): ...
    transport: Union[
        MobileDeviceConstantServiceGrpcTransport,
        Callable[[Credentials, type], MobileDeviceConstantServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                MobileDeviceConstantServiceGrpcTransport,
                Callable[[Credentials, type], MobileDeviceConstantServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_mobile_device_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MobileDeviceConstant: ...
