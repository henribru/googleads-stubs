# Stubs for google.ads.google_ads.v2.proto.services.mobile_app_category_constant_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class MobileAppCategoryConstantServiceStub:
    GetMobileAppCategoryConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class MobileAppCategoryConstantServiceServicer:
    def GetMobileAppCategoryConstant(self, request: Any, context: Any) -> None: ...

def add_MobileAppCategoryConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
