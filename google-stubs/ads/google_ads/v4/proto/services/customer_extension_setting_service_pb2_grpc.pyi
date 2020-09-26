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
