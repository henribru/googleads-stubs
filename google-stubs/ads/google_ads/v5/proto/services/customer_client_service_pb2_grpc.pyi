"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.customer_client_pb2
import grpc

from .customer_client_service_pb2 import *

class CustomerClientServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetCustomerClient(
        self,
        request: global___GetCustomerClientRequest,
    ) -> google.ads.google_ads.v5.proto.resources.customer_client_pb2.CustomerClient: ...

class CustomerClientServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetCustomerClient(
        self,
        request: global___GetCustomerClientRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.customer_client_pb2.CustomerClient: ...

def add_CustomerClientServiceServicer_to_server(
    servicer: CustomerClientServiceServicer, server: grpc.Server
) -> None: ...
