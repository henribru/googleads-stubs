# Stubs for google.ads.google_ads.v2.proto.services.distance_view_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class DistanceViewServiceStub:
    GetDistanceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DistanceViewServiceServicer:
    def GetDistanceView(self, request: Any, context: Any) -> None: ...

def add_DistanceViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...