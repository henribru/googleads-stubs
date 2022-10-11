import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCustomerCustomizersRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CustomerCustomizerOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCustomerCustomizersResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateCustomerCustomizerResult(proto.Message):
    resource_name: Incomplete
    customer_customizer: Incomplete