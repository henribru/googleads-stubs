from typing import Any

class BillingSetupServiceStub:
    GetBillingSetup: Any = ...
    MutateBillingSetup: Any = ...
    def __init__(self, channel: Any) -> None: ...

class BillingSetupServiceServicer:
    def GetBillingSetup(self, request: Any, context: Any) -> None: ...
    def MutateBillingSetup(self, request: Any, context: Any) -> None: ...

def add_BillingSetupServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
