# Stubs for google.ads.google_ads.v1.proto.services.parental_status_view_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ParentalStatusViewServiceStub:
    GetParentalStatusView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ParentalStatusViewServiceServicer:
    def GetParentalStatusView(self, request: Any, context: Any) -> None: ...

def add_ParentalStatusViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
