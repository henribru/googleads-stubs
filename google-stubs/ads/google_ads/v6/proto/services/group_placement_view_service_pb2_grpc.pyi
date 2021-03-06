"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.group_placement_view_pb2
import grpc

from .group_placement_view_service_pb2 import *

class GroupPlacementViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetGroupPlacementView(
        self,
        request: global___GetGroupPlacementViewRequest,
    ) -> google.ads.google_ads.v6.proto.resources.group_placement_view_pb2.GroupPlacementView: ...

class GroupPlacementViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetGroupPlacementView(
        self,
        request: global___GetGroupPlacementViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.group_placement_view_pb2.GroupPlacementView: ...

def add_GroupPlacementViewServiceServicer_to_server(
    servicer: GroupPlacementViewServiceServicer, server: grpc.Server
) -> None: ...
