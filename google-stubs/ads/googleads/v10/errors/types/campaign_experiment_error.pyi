import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignExperimentErrorEnum(proto.Message):
    class CampaignExperimentError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_NAME: int
        INVALID_TRANSITION: int
        CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET: int
        CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN: int
        CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT: int
        CUSTOMER_CANNOT_CREATE_EXPERIMENT: int
        CAMPAIGN_CANNOT_CREATE_EXPERIMENT: int
        EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP: int
        EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION: int
        CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS: int
