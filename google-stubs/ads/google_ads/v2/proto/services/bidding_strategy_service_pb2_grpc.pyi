# Stubs for google.ads.google_ads.v2.proto.services.bidding_strategy_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BiddingStrategyServiceStub:
    GetBiddingStrategy: Any = ...
    MutateBiddingStrategies: Any = ...
    def __init__(self, channel: Any) -> None: ...

class BiddingStrategyServiceServicer:
    def GetBiddingStrategy(self, request: Any, context: Any) -> None: ...
    def MutateBiddingStrategies(self, request: Any, context: Any) -> None: ...

def add_BiddingStrategyServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
