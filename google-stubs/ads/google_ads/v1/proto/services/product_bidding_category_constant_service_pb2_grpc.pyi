# Stubs for google.ads.google_ads.v1.proto.services.product_bidding_category_constant_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ProductBiddingCategoryConstantServiceStub:
    GetProductBiddingCategoryConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ProductBiddingCategoryConstantServiceServicer:
    def GetProductBiddingCategoryConstant(self, request: Any, context: Any) -> None: ...

def add_ProductBiddingCategoryConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
