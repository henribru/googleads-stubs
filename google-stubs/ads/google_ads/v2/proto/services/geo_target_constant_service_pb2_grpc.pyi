# Stubs for google.ads.google_ads.v2.proto.services.geo_target_constant_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class GeoTargetConstantServiceStub:
    GetGeoTargetConstant: Any = ...
    SuggestGeoTargetConstants: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GeoTargetConstantServiceServicer:
    def GetGeoTargetConstant(self, request: Any, context: Any) -> None: ...
    def SuggestGeoTargetConstants(self, request: Any, context: Any) -> None: ...

def add_GeoTargetConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
