# Stubs for google.ads.google_ads.v1.proto.services.label_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class LabelServiceStub:
    GetLabel: Any = ...
    MutateLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class LabelServiceServicer:
    def GetLabel(self, request: Any, context: Any) -> None: ...
    def MutateLabels(self, request: Any, context: Any) -> None: ...

def add_LabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
