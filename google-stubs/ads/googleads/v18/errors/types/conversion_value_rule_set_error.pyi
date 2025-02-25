from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ConversionValueRuleSetErrorEnum(proto.Message):
    class ConversionValueRuleSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONFLICTING_VALUE_RULE_CONDITIONS = 2
        INVALID_VALUE_RULE = 3
        DIMENSIONS_UPDATE_ONLY_ALLOW_APPEND = 4
        CONDITION_TYPE_NOT_ALLOWED = 5
        DUPLICATE_DIMENSIONS = 6
        INVALID_CAMPAIGN_ID = 7
        CANNOT_PAUSE_UNLESS_ALL_VALUE_RULES_ARE_PAUSED = 8
        SHOULD_PAUSE_WHEN_ALL_VALUE_RULES_ARE_PAUSED = 9
        VALUE_RULES_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE = 10
        INELIGIBLE_CONVERSION_ACTION_CATEGORIES = 11
        DIMENSION_NO_CONDITION_USED_WITH_OTHER_DIMENSIONS = 12
        DIMENSION_NO_CONDITION_NOT_ALLOWED = 13
        UNSUPPORTED_CONVERSION_ACTION_CATEGORIES = 14
        DIMENSION_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE = 15

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
