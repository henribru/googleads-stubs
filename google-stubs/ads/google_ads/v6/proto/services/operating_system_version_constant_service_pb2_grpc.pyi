"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.operating_system_version_constant_pb2
import grpc

from .operating_system_version_constant_service_pb2 import *

class OperatingSystemVersionConstantServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetOperatingSystemVersionConstant(
        self,
        request: global___GetOperatingSystemVersionConstantRequest,
    ) -> google.ads.google_ads.v6.proto.resources.operating_system_version_constant_pb2.OperatingSystemVersionConstant: ...

class OperatingSystemVersionConstantServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetOperatingSystemVersionConstant(
        self,
        request: global___GetOperatingSystemVersionConstantRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.operating_system_version_constant_pb2.OperatingSystemVersionConstant: ...

def add_OperatingSystemVersionConstantServiceServicer_to_server(
    servicer: OperatingSystemVersionConstantServiceServicer, server: grpc.Server
) -> None: ...
