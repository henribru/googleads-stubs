# Stubs for google.ads.google_ads.v1.proto.services.campaign_criterion_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CampaignCriterionServiceStub:
    GetCampaignCriterion: Any = ...
    MutateCampaignCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignCriterionServiceServicer:
    def GetCampaignCriterion(self, request: Any, context: Any) -> None: ...
    def MutateCampaignCriteria(self, request: Any, context: Any) -> None: ...

def add_CampaignCriterionServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
