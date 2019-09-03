import grpc
from google.ads.google_ads.v1.services.transports.operating_system_version_constant_service_grpc_transport import OperatingSystemVersionConstantServiceGrpcTransport
from google.auth.credentials import Credentials
from google.api_core.gapic_v1.client_info import ClientInfo
from google.api_core.retry import Retry
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.operating_system_version_constant_pb2 import OperatingSystemVersionConstant

class OperatingSystemVersionConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args: Any, **kwargs: Any) -> OperatingSystemVersionConstantServiceClient: ...
    @classmethod
    def from_service_account_json(cls, filename: str, *args: Any, **kwargs: Any) -> OperatingSystemVersionConstantServiceClient: ...
    @classmethod
    def operating_system_version_constant_path(cls, operating_system_version_constant: Any): ...
    transport: Union[OperatingSystemVersionConstantServiceGrpcTransport, Callable[[Credentials, type], OperatingSystemVersionConstantServiceGrpcTransport]] = ...
    def __init__(self, transport: Optional[Union[OperatingSystemVersionConstantServiceGrpcTransport, Callable[[Credentials, type], OperatingSystemVersionConstantServiceGrpcTransport]]] = ..., channel: Optional[grpc.Channel] = ..., credentials: Optional[Credentials] = ..., client_config: Optional[Dict[Any, Any]] = ..., client_info: Optional[ClientInfo] = ...) -> None: ...
    def get_operating_system_version_constant(self, resource_name: str, retry: Optional[Retry] = ..., timeout: Optional[float] = ..., metadata: Optional[Sequence[Tuple[str, str]]] = ...) -> OperatingSystemVersionConstant: ...
