"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.merchant_center_link_pb2
import grpc

from .merchant_center_link_service_pb2 import *

class MerchantCenterLinkServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def ListMerchantCenterLinks(
        self,
        request: global___ListMerchantCenterLinksRequest,
    ) -> global___ListMerchantCenterLinksResponse: ...
    def GetMerchantCenterLink(
        self,
        request: global___GetMerchantCenterLinkRequest,
    ) -> google.ads.google_ads.v4.proto.resources.merchant_center_link_pb2.MerchantCenterLink: ...
    def MutateMerchantCenterLink(
        self,
        request: global___MutateMerchantCenterLinkRequest,
    ) -> global___MutateMerchantCenterLinkResponse: ...

class MerchantCenterLinkServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ListMerchantCenterLinks(
        self,
        request: global___ListMerchantCenterLinksRequest,
        context: grpc.ServicerContext,
    ) -> global___ListMerchantCenterLinksResponse: ...
    @abc.abstractmethod
    def GetMerchantCenterLink(
        self,
        request: global___GetMerchantCenterLinkRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.merchant_center_link_pb2.MerchantCenterLink: ...
    @abc.abstractmethod
    def MutateMerchantCenterLink(
        self,
        request: global___MutateMerchantCenterLinkRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateMerchantCenterLinkResponse: ...

def add_MerchantCenterLinkServiceServicer_to_server(
    servicer: MerchantCenterLinkServiceServicer, server: grpc.Server
) -> None: ...
