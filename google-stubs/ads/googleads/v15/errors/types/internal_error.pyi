from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class InternalErrorEnum(proto.Message):
    class InternalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INTERNAL_ERROR = 2
        ERROR_CODE_NOT_PUBLISHED = 3
        TRANSIENT_ERROR = 4
        DEADLINE_EXCEEDED = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(self, key: NoReturn) -> bool: ...  # type: ignore[override]
