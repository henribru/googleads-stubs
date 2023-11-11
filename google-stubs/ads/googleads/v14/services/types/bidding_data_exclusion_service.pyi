from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.bidding_data_exclusion import (
    BiddingDataExclusion,
)

_M = TypeVar("_M")

class BiddingDataExclusionOperation(proto.Message):
    update_mask: FieldMask
    create: BiddingDataExclusion
    update: BiddingDataExclusion
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: BiddingDataExclusion = ...,
        update: BiddingDataExclusion = ...,
        remove: str = ...
    ) -> None: ...

class MutateBiddingDataExclusionsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[BiddingDataExclusionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[BiddingDataExclusionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateBiddingDataExclusionsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateBiddingDataExclusionsResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateBiddingDataExclusionsResult] = ...
    ) -> None: ...

class MutateBiddingDataExclusionsResult(proto.Message):
    resource_name: str
    bidding_data_exclusion: BiddingDataExclusion
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        bidding_data_exclusion: BiddingDataExclusion = ...
    ) -> None: ...
