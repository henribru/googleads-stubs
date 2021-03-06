"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.topic_constant_pb2
import grpc

from .topic_constant_service_pb2 import *

class TopicConstantServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetTopicConstant(
        self,
        request: global___GetTopicConstantRequest,
    ) -> google.ads.google_ads.v5.proto.resources.topic_constant_pb2.TopicConstant: ...

class TopicConstantServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetTopicConstant(
        self,
        request: global___GetTopicConstantRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.topic_constant_pb2.TopicConstant: ...

def add_TopicConstantServiceServicer_to_server(
    servicer: TopicConstantServiceServicer, server: grpc.Server
) -> None: ...
