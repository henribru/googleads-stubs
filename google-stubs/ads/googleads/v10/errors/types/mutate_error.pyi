import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class MutateErrorEnum(proto.Message):
    class MutateError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        RESOURCE_NOT_FOUND: int
        ID_EXISTS_IN_MULTIPLE_MUTATES: int
        INCONSISTENT_FIELD_VALUES: int
        MUTATE_NOT_ALLOWED: int
        RESOURCE_NOT_IN_GOOGLE_ADS: int
        RESOURCE_ALREADY_EXISTS: int
        RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY: int
        OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE: int
        RESOURCE_READ_ONLY: int