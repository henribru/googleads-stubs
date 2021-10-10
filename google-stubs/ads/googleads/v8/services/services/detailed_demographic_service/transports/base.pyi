import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import detailed_demographic
from google.ads.googleads.v8.services.types import detailed_demographic_service

class DetailedDemographicServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_detailed_demographic(
        self,
    ) -> typing.Callable[
        [detailed_demographic_service.GetDetailedDemographicRequest],
        detailed_demographic.DetailedDemographic,
    ]: ...
