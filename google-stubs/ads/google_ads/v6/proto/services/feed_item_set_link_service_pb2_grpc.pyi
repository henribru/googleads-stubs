"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.feed_item_set_link_pb2
import grpc

from .feed_item_set_link_service_pb2 import *

class FeedItemSetLinkServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetFeedItemSetLink(
        self,
        request: global___GetFeedItemSetLinkRequest,
    ) -> google.ads.google_ads.v6.proto.resources.feed_item_set_link_pb2.FeedItemSetLink: ...
    def MutateFeedItemSetLinks(
        self,
        request: global___MutateFeedItemSetLinksRequest,
    ) -> global___MutateFeedItemSetLinksResponse: ...

class FeedItemSetLinkServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetFeedItemSetLink(
        self,
        request: global___GetFeedItemSetLinkRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.feed_item_set_link_pb2.FeedItemSetLink: ...
    @abc.abstractmethod
    def MutateFeedItemSetLinks(
        self,
        request: global___MutateFeedItemSetLinksRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateFeedItemSetLinksResponse: ...

def add_FeedItemSetLinkServiceServicer_to_server(
    servicer: FeedItemSetLinkServiceServicer, server: grpc.Server
) -> None: ...
