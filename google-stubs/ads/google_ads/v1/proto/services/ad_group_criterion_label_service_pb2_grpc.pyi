# Stubs for google.ads.google_ads.v1.proto.services.ad_group_criterion_label_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class AdGroupCriterionLabelServiceStub:
    GetAdGroupCriterionLabel: Any = ...
    MutateAdGroupCriterionLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupCriterionLabelServiceServicer:
    def GetAdGroupCriterionLabel(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupCriterionLabels(self, request: Any, context: Any) -> None: ...

def add_AdGroupCriterionLabelServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
