import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SimulationTypeEnum(proto.Message):
    class SimulationType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CPC_BID: int
        CPV_BID: int
        TARGET_CPA: int
        BID_MODIFIER: int
        TARGET_ROAS: int
        PERCENT_CPC_BID: int
        TARGET_IMPRESSION_SHARE: int
        BUDGET: int