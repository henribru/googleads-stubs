# Stubs for google.ads.google_ads.v1.proto.services.customer_negative_criterion_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CustomerNegativeCriterionServiceStub:
    GetCustomerNegativeCriterion: Any = ...
    MutateCustomerNegativeCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerNegativeCriterionServiceServicer:
    def GetCustomerNegativeCriterion(self, request: Any, context: Any) -> None: ...
    def MutateCustomerNegativeCriteria(self, request: Any, context: Any) -> None: ...

def add_CustomerNegativeCriterionServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
