# Stubs for google.ads.google_ads.v2.proto.services.campaign_extension_setting_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CampaignExtensionSettingServiceStub:
    GetCampaignExtensionSetting: Any = ...
    MutateCampaignExtensionSettings: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignExtensionSettingServiceServicer:
    def GetCampaignExtensionSetting(self, request: Any, context: Any) -> None: ...
    def MutateCampaignExtensionSettings(self, request: Any, context: Any) -> None: ...

def add_CampaignExtensionSettingServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
