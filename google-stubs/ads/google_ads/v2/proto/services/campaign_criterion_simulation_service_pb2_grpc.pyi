# Stubs for google.ads.google_ads.v2.proto.services.campaign_criterion_simulation_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CampaignCriterionSimulationServiceStub:
    GetCampaignCriterionSimulation: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignCriterionSimulationServiceServicer:
    def GetCampaignCriterionSimulation(self, request: Any, context: Any) -> None: ...

def add_CampaignCriterionSimulationServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
