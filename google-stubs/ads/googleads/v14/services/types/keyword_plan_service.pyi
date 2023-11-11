from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.resources.types.keyword_plan import KeywordPlan

_M = TypeVar("_M")

class KeywordPlanOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlan
    update: KeywordPlan
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: KeywordPlan = ...,
        update: KeywordPlan = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlansRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[KeywordPlanOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlansResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlansResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateKeywordPlansResult] = ...
    ) -> None: ...

class MutateKeywordPlansResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
