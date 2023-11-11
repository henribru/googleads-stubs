from typing import Any

import proto

class AdNetworkTypeEnum(proto.Message):
    class AdNetworkType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH = 2
        SEARCH_PARTNERS = 3
        CONTENT = 4
        MIXED = 7
        YOUTUBE = 8
        GOOGLE_TV = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
