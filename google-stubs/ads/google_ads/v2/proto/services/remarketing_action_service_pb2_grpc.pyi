# Stubs for google.ads.google_ads.v2.proto.services.remarketing_action_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class RemarketingActionServiceStub:
    GetRemarketingAction: Any = ...
    MutateRemarketingActions: Any = ...
    def __init__(self, channel: Any) -> None: ...

class RemarketingActionServiceServicer:
    def GetRemarketingAction(self, request: Any, context: Any) -> None: ...
    def MutateRemarketingActions(self, request: Any, context: Any) -> None: ...

def add_RemarketingActionServiceServicer_to_server(servicer: Any, server: Any) -> None: ...