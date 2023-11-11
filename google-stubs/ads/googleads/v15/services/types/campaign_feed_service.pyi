from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.campaign_feed import CampaignFeed

_M = TypeVar("_M")

class CampaignFeedOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignFeed
    update: CampaignFeed
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignFeed = ...,
        update: CampaignFeed = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignFeedResult(proto.Message):
    resource_name: str
    campaign_feed: CampaignFeed
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_feed: CampaignFeed = ...
    ) -> None: ...

class MutateCampaignFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignFeedOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignFeedOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignFeedsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignFeedResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignFeedResult] = ...
    ) -> None: ...
