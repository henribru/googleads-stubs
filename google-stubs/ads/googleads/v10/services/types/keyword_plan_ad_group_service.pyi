import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.resources.types import (
    keyword_plan_ad_group as keyword_plan_ad_group,
)

__protobuf__: Incomplete

class MutateKeywordPlanAdGroupsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class KeywordPlanAdGroupOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateKeywordPlanAdGroupsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateKeywordPlanAdGroupResult(proto.Message):
    resource_name: Incomplete