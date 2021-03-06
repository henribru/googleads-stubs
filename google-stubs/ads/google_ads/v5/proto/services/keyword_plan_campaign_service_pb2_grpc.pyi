"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.keyword_plan_campaign_pb2
import grpc

from .keyword_plan_campaign_service_pb2 import *

class KeywordPlanCampaignServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetKeywordPlanCampaign(
        self,
        request: global___GetKeywordPlanCampaignRequest,
    ) -> google.ads.google_ads.v5.proto.resources.keyword_plan_campaign_pb2.KeywordPlanCampaign: ...
    def MutateKeywordPlanCampaigns(
        self,
        request: global___MutateKeywordPlanCampaignsRequest,
    ) -> global___MutateKeywordPlanCampaignsResponse: ...

class KeywordPlanCampaignServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetKeywordPlanCampaign(
        self,
        request: global___GetKeywordPlanCampaignRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.keyword_plan_campaign_pb2.KeywordPlanCampaign: ...
    @abc.abstractmethod
    def MutateKeywordPlanCampaigns(
        self,
        request: global___MutateKeywordPlanCampaignsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateKeywordPlanCampaignsResponse: ...

def add_KeywordPlanCampaignServiceServicer_to_server(
    servicer: KeywordPlanCampaignServiceServicer, server: grpc.Server
) -> None: ...
