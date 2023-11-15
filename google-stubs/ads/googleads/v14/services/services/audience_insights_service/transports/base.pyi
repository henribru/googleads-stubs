import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import audience_insights_service

class AudienceInsightsServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def generate_insights_finder_report(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateInsightsFinderReportRequest],
        Union[
            audience_insights_service.GenerateInsightsFinderReportResponse,
            Awaitable[audience_insights_service.GenerateInsightsFinderReportResponse],
        ],
    ]: ...
    @property
    def list_audience_insights_attributes(
        self,
    ) -> Callable[
        [audience_insights_service.ListAudienceInsightsAttributesRequest],
        Union[
            audience_insights_service.ListAudienceInsightsAttributesResponse,
            Awaitable[audience_insights_service.ListAudienceInsightsAttributesResponse],
        ],
    ]: ...
    @property
    def list_insights_eligible_dates(
        self,
    ) -> Callable[
        [audience_insights_service.ListInsightsEligibleDatesRequest],
        Union[
            audience_insights_service.ListInsightsEligibleDatesResponse,
            Awaitable[audience_insights_service.ListInsightsEligibleDatesResponse],
        ],
    ]: ...
    @property
    def generate_audience_composition_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateAudienceCompositionInsightsRequest],
        Union[
            audience_insights_service.GenerateAudienceCompositionInsightsResponse,
            Awaitable[
                audience_insights_service.GenerateAudienceCompositionInsightsResponse
            ],
        ],
    ]: ...
