# Stubs for google.ads.google_ads.v2.proto.services.campaign_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CampaignServiceStub:
    GetCampaign: Any = ...
    MutateCampaigns: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignServiceServicer:
    def GetCampaign(self, request: Any, context: Any) -> None: ...
    def MutateCampaigns(self, request: Any, context: Any) -> None: ...

def add_CampaignServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
