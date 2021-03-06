"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.campaign_criterion_simulation_pb2
import grpc

from .campaign_criterion_simulation_service_pb2 import *

class CampaignCriterionSimulationServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetCampaignCriterionSimulation(
        self,
        request: global___GetCampaignCriterionSimulationRequest,
    ) -> google.ads.google_ads.v4.proto.resources.campaign_criterion_simulation_pb2.CampaignCriterionSimulation: ...

class CampaignCriterionSimulationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetCampaignCriterionSimulation(
        self,
        request: global___GetCampaignCriterionSimulationRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.campaign_criterion_simulation_pb2.CampaignCriterionSimulation: ...

def add_CampaignCriterionSimulationServiceServicer_to_server(
    servicer: CampaignCriterionSimulationServiceServicer, server: grpc.Server
) -> None: ...
