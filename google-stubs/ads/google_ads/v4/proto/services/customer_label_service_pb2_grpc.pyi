from typing import Any

class CustomerLabelServiceStub:
    GetCustomerLabel: Any = ...
    MutateCustomerLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerLabelServiceServicer:
    def GetCustomerLabel(self, request: Any, context: Any) -> None: ...
    def MutateCustomerLabels(self, request: Any, context: Any) -> None: ...

def add_CustomerLabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
