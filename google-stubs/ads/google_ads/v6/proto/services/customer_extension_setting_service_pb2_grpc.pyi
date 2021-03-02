# Stubs for google.ads.google_ads.v6.proto.services.customer_extension_setting_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class CustomerExtensionSettingServiceStub:
    GetCustomerExtensionSetting: Any = ...
    MutateCustomerExtensionSettings: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerExtensionSettingServiceServicer:
    def GetCustomerExtensionSetting(self, request: Any, context: Any) -> None: ...
    def MutateCustomerExtensionSettings(self, request: Any, context: Any) -> None: ...

def add_CustomerExtensionSettingServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CustomerExtensionSettingService:
    @staticmethod
    def GetCustomerExtensionSetting(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
    @staticmethod
    def MutateCustomerExtensionSettings(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...