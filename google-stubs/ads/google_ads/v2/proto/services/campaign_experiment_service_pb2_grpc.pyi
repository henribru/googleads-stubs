# Stubs for google.ads.google_ads.v2.proto.services.campaign_experiment_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CampaignExperimentServiceStub:
    GetCampaignExperiment: Any = ...
    CreateCampaignExperiment: Any = ...
    MutateCampaignExperiments: Any = ...
    GraduateCampaignExperiment: Any = ...
    PromoteCampaignExperiment: Any = ...
    EndCampaignExperiment: Any = ...
    ListCampaignExperimentAsyncErrors: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignExperimentServiceServicer:
    def GetCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def CreateCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def MutateCampaignExperiments(self, request: Any, context: Any) -> None: ...
    def GraduateCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def PromoteCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def EndCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def ListCampaignExperimentAsyncErrors(self, request: Any, context: Any) -> None: ...

def add_CampaignExperimentServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
