"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.paid_organic_search_term_view_pb2
import grpc

from .paid_organic_search_term_view_service_pb2 import *

class PaidOrganicSearchTermViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetPaidOrganicSearchTermView(
        self,
        request: global___GetPaidOrganicSearchTermViewRequest,
    ) -> google.ads.google_ads.v5.proto.resources.paid_organic_search_term_view_pb2.PaidOrganicSearchTermView: ...

class PaidOrganicSearchTermViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetPaidOrganicSearchTermView(
        self,
        request: global___GetPaidOrganicSearchTermViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.paid_organic_search_term_view_pb2.PaidOrganicSearchTermView: ...

def add_PaidOrganicSearchTermViewServiceServicer_to_server(
    servicer: PaidOrganicSearchTermViewServiceServicer, server: grpc.Server
) -> None: ...
