"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.ad_group_criterion_label_pb2
import grpc

from .ad_group_criterion_label_service_pb2 import *

class AdGroupCriterionLabelServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupCriterionLabel(
        self,
        request: global___GetAdGroupCriterionLabelRequest,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_criterion_label_pb2.AdGroupCriterionLabel: ...
    def MutateAdGroupCriterionLabels(
        self,
        request: global___MutateAdGroupCriterionLabelsRequest,
    ) -> global___MutateAdGroupCriterionLabelsResponse: ...

class AdGroupCriterionLabelServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupCriterionLabel(
        self,
        request: global___GetAdGroupCriterionLabelRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_criterion_label_pb2.AdGroupCriterionLabel: ...
    @abc.abstractmethod
    def MutateAdGroupCriterionLabels(
        self,
        request: global___MutateAdGroupCriterionLabelsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateAdGroupCriterionLabelsResponse: ...

def add_AdGroupCriterionLabelServiceServicer_to_server(
    servicer: AdGroupCriterionLabelServiceServicer, server: grpc.Server
) -> None: ...
