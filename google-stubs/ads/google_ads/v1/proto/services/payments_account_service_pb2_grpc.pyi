# Stubs for google.ads.google_ads.v1.proto.services.payments_account_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class PaymentsAccountServiceStub:
    ListPaymentsAccounts: Any = ...
    def __init__(self, channel: Any) -> None: ...

class PaymentsAccountServiceServicer:
    def ListPaymentsAccounts(self, request: Any, context: Any) -> None: ...

def add_PaymentsAccountServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
