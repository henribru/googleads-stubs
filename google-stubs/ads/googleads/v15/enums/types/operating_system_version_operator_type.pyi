from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class OperatingSystemVersionOperatorTypeEnum(proto.Message):
    class OperatingSystemVersionOperatorType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EQUALS_TO = 2
        GREATER_THAN_EQUALS_TO = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
