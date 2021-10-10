import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import life_event
from google.ads.googleads.v7.services.types import life_event_service

class LifeEventServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_life_event(
        self,
    ) -> typing.Callable[
        [life_event_service.GetLifeEventRequest], life_event.LifeEvent
    ]: ...
