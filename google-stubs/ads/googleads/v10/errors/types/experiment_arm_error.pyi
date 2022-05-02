import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExperimentArmErrorEnum(proto.Message):
    class ExperimentArmError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXPERIMENT_ARM_COUNT_LIMIT_EXCEEDED: int
        INVALID_CAMPAIGN_STATUS: int
        DUPLICATE_EXPERIMENT_ARM_NAME: int
        CANNOT_SET_TREATMENT_ARM_CAMPAIGN: int
        CANNOT_MODIFY_CAMPAIGN_IDS: int
        CANNOT_MODIFY_CAMPAIGN_WITHOUT_SUFFIX_SET: int
        CANNOT_MUTATE_TRAFFIC_SPLIT_AFTER_START: int
        CANNOT_ADD_CAMPAIGN_WITH_SHARED_BUDGET: int
        CANNOT_ADD_CAMPAIGN_WITH_CUSTOM_BUDGET: int
        CANNOT_ADD_CAMPAIGNS_WITH_DYNAMIC_ASSETS_ENABLED: int
        UNSUPPORTED_CAMPAIGN_ADVERTISING_CHANNEL_SUB_TYPE: int
        CANNOT_ADD_BASE_CAMPAIGN_WITH_DATE_RANGE: int
        BIDDING_STRATEGY_NOT_SUPPORTED_IN_EXPERIMENTS: int
        TRAFFIC_SPLIT_NOT_SUPPORTED_FOR_CHANNEL_TYPE: int
