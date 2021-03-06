"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.third_party_app_analytics_link_pb2
import grpc

from .third_party_app_analytics_link_service_pb2 import *

class ThirdPartyAppAnalyticsLinkServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetThirdPartyAppAnalyticsLink(
        self,
        request: global___GetThirdPartyAppAnalyticsLinkRequest,
    ) -> google.ads.google_ads.v5.proto.resources.third_party_app_analytics_link_pb2.ThirdPartyAppAnalyticsLink: ...
    def RegenerateShareableLinkId(
        self,
        request: global___RegenerateShareableLinkIdRequest,
    ) -> global___RegenerateShareableLinkIdResponse: ...

class ThirdPartyAppAnalyticsLinkServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetThirdPartyAppAnalyticsLink(
        self,
        request: global___GetThirdPartyAppAnalyticsLinkRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.third_party_app_analytics_link_pb2.ThirdPartyAppAnalyticsLink: ...
    @abc.abstractmethod
    def RegenerateShareableLinkId(
        self,
        request: global___RegenerateShareableLinkIdRequest,
        context: grpc.ServicerContext,
    ) -> global___RegenerateShareableLinkIdResponse: ...

def add_ThirdPartyAppAnalyticsLinkServiceServicer_to_server(
    servicer: ThirdPartyAppAnalyticsLinkServiceServicer, server: grpc.Server
) -> None: ...
