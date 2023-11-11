from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class BatchJobErrorEnum(proto.Message):
    class BatchJobError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING = 2
        EMPTY_OPERATIONS = 3
        INVALID_SEQUENCE_TOKEN = 4
        RESULTS_NOT_READY = 5
        INVALID_PAGE_SIZE = 6
        CAN_ONLY_REMOVE_PENDING_JOB = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
