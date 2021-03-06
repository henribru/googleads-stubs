"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.offline_user_data_job_pb2
import google.longrunning.operations_pb2
import grpc

from .offline_user_data_job_service_pb2 import *

class OfflineUserDataJobServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def CreateOfflineUserDataJob(
        self,
        request: global___CreateOfflineUserDataJobRequest,
    ) -> global___CreateOfflineUserDataJobResponse: ...
    def GetOfflineUserDataJob(
        self,
        request: global___GetOfflineUserDataJobRequest,
    ) -> google.ads.google_ads.v5.proto.resources.offline_user_data_job_pb2.OfflineUserDataJob: ...
    def AddOfflineUserDataJobOperations(
        self,
        request: global___AddOfflineUserDataJobOperationsRequest,
    ) -> global___AddOfflineUserDataJobOperationsResponse: ...
    def RunOfflineUserDataJob(
        self,
        request: global___RunOfflineUserDataJobRequest,
    ) -> google.longrunning.operations_pb2.Operation: ...

class OfflineUserDataJobServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateOfflineUserDataJob(
        self,
        request: global___CreateOfflineUserDataJobRequest,
        context: grpc.ServicerContext,
    ) -> global___CreateOfflineUserDataJobResponse: ...
    @abc.abstractmethod
    def GetOfflineUserDataJob(
        self,
        request: global___GetOfflineUserDataJobRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.offline_user_data_job_pb2.OfflineUserDataJob: ...
    @abc.abstractmethod
    def AddOfflineUserDataJobOperations(
        self,
        request: global___AddOfflineUserDataJobOperationsRequest,
        context: grpc.ServicerContext,
    ) -> global___AddOfflineUserDataJobOperationsResponse: ...
    @abc.abstractmethod
    def RunOfflineUserDataJob(
        self,
        request: global___RunOfflineUserDataJobRequest,
        context: grpc.ServicerContext,
    ) -> google.longrunning.operations_pb2.Operation: ...

def add_OfflineUserDataJobServiceServicer_to_server(
    servicer: OfflineUserDataJobServiceServicer, server: grpc.Server
) -> None: ...
