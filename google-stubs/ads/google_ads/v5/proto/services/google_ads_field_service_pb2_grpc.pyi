"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.google_ads_field_pb2
import grpc

from .google_ads_field_service_pb2 import *

class GoogleAdsFieldServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetGoogleAdsField(
        self,
        request: global___GetGoogleAdsFieldRequest,
    ) -> google.ads.google_ads.v5.proto.resources.google_ads_field_pb2.GoogleAdsField: ...
    def SearchGoogleAdsFields(
        self,
        request: global___SearchGoogleAdsFieldsRequest,
    ) -> global___SearchGoogleAdsFieldsResponse: ...

class GoogleAdsFieldServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetGoogleAdsField(
        self,
        request: global___GetGoogleAdsFieldRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.google_ads_field_pb2.GoogleAdsField: ...
    @abc.abstractmethod
    def SearchGoogleAdsFields(
        self,
        request: global___SearchGoogleAdsFieldsRequest,
        context: grpc.ServicerContext,
    ) -> global___SearchGoogleAdsFieldsResponse: ...

def add_GoogleAdsFieldServiceServicer_to_server(
    servicer: GoogleAdsFieldServiceServicer, server: grpc.Server
) -> None: ...
