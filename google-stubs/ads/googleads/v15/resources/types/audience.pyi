from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.audiences import (
    AudienceDimension,
    AudienceExclusionDimension,
)
from google.ads.googleads.v15.enums.types.audience_scope import AudienceScopeEnum
from google.ads.googleads.v15.enums.types.audience_status import AudienceStatusEnum

_M = TypeVar("_M")

class Audience(proto.Message):
    resource_name: str
    id: int
    status: AudienceStatusEnum.AudienceStatus
    name: str
    description: str
    dimensions: MutableSequence[AudienceDimension]
    exclusion_dimension: AudienceExclusionDimension
    scope: AudienceScopeEnum.AudienceScope
    asset_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        status: AudienceStatusEnum.AudienceStatus = ...,
        name: str = ...,
        description: str = ...,
        dimensions: MutableSequence[AudienceDimension] = ...,
        exclusion_dimension: AudienceExclusionDimension = ...,
        scope: AudienceScopeEnum.AudienceScope = ...,
        asset_group: str = ...
    ) -> None: ...
