# Stubs for google.ads.google_ads.v2.proto.services.ad_group_audience_view_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class AdGroupAudienceViewServiceStub:
    GetAdGroupAudienceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupAudienceViewServiceServicer:
    def GetAdGroupAudienceView(self, request: Any, context: Any) -> None: ...

def add_AdGroupAudienceViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
