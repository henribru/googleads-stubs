from typing import Any

import proto

class ValueRuleSetAttachmentTypeEnum(proto.Message):
    class ValueRuleSetAttachmentType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER = 2
        CAMPAIGN = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
