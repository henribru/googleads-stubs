"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.extension_feed_item_pb2
import grpc

from .extension_feed_item_service_pb2 import *

class ExtensionFeedItemServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetExtensionFeedItem(
        self,
        request: global___GetExtensionFeedItemRequest,
    ) -> google.ads.google_ads.v4.proto.resources.extension_feed_item_pb2.ExtensionFeedItem: ...
    def MutateExtensionFeedItems(
        self,
        request: global___MutateExtensionFeedItemsRequest,
    ) -> global___MutateExtensionFeedItemsResponse: ...

class ExtensionFeedItemServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetExtensionFeedItem(
        self,
        request: global___GetExtensionFeedItemRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.extension_feed_item_pb2.ExtensionFeedItem: ...
    @abc.abstractmethod
    def MutateExtensionFeedItems(
        self,
        request: global___MutateExtensionFeedItemsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateExtensionFeedItemsResponse: ...

def add_ExtensionFeedItemServiceServicer_to_server(
    servicer: ExtensionFeedItemServiceServicer, server: grpc.Server
) -> None: ...
