import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import detail_placement_view
from google.ads.googleads.v7.services.types import detail_placement_view_service

class DetailPlacementViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_detail_placement_view(
        self,
    ) -> typing.Callable[
        [detail_placement_view_service.GetDetailPlacementViewRequest],
        detail_placement_view.DetailPlacementView,
    ]: ...
