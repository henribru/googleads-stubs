from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.customer_feed import CustomerFeed

_M = TypeVar("_M")

class CustomerFeedOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerFeed
    update: CustomerFeed
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomerFeed = ...,
        update: CustomerFeed = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerFeedResult(proto.Message):
    resource_name: str
    customer_feed: CustomerFeed
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_feed: CustomerFeed = ...
    ) -> None: ...

class MutateCustomerFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerFeedOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CustomerFeedOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerFeedsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCustomerFeedResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCustomerFeedResult] = ...
    ) -> None: ...
