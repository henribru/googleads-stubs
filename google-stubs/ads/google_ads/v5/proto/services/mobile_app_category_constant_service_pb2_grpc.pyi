"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.mobile_app_category_constant_pb2
import grpc

from .mobile_app_category_constant_service_pb2 import *

class MobileAppCategoryConstantServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetMobileAppCategoryConstant(
        self,
        request: global___GetMobileAppCategoryConstantRequest,
    ) -> google.ads.google_ads.v5.proto.resources.mobile_app_category_constant_pb2.MobileAppCategoryConstant: ...

class MobileAppCategoryConstantServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetMobileAppCategoryConstant(
        self,
        request: global___GetMobileAppCategoryConstantRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.mobile_app_category_constant_pb2.MobileAppCategoryConstant: ...

def add_MobileAppCategoryConstantServiceServicer_to_server(
    servicer: MobileAppCategoryConstantServiceServicer, server: grpc.Server
) -> None: ...
