# Stubs for google.ads.google_ads.v1.proto.services.group_placement_view_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class GroupPlacementViewServiceStub:
    GetGroupPlacementView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GroupPlacementViewServiceServicer:
    def GetGroupPlacementView(self, request: Any, context: Any) -> None: ...

def add_GroupPlacementViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
