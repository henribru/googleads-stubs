# Stubs for google.ads.google_ads.v1.proto.services.customer_extension_setting_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

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
