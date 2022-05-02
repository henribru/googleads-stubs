import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignErrorEnum(proto.Message):
    class CampaignError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_TARGET_CONTENT_NETWORK: int
        CANNOT_TARGET_SEARCH_NETWORK: int
        CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH: int
        CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN: int
        CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK: int
        CANNOT_TARGET_PARTNER_SEARCH_NETWORK: int
        CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY: int
        CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS: int
        CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN: int
        DUPLICATE_CAMPAIGN_NAME: int
        INCOMPATIBLE_CAMPAIGN_FIELD: int
        INVALID_CAMPAIGN_NAME: int
        INVALID_AD_SERVING_OPTIMIZATION_STATUS: int
        INVALID_TRACKING_URL: int
        CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING: int
        MAX_IMPRESSIONS_NOT_IN_RANGE: int
        TIME_UNIT_NOT_SUPPORTED: int
        INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED: int
        BUDGET_CANNOT_BE_SHARED: int
        CAMPAIGN_CANNOT_USE_SHARED_BUDGET: int
        CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS: int
        CAMPAIGN_LABEL_DOES_NOT_EXIST: int
        CAMPAIGN_LABEL_ALREADY_EXISTS: int
        MISSING_SHOPPING_SETTING: int
        INVALID_SHOPPING_SALES_COUNTRY: int
        ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE: int
        INVALID_ADVERTISING_CHANNEL_SUB_TYPE: int
        AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED: int
        CANNOT_SET_AD_ROTATION_MODE: int
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED: int
        CANNOT_SET_DATE_TO_PAST: int
        MISSING_HOTEL_CUSTOMER_LINK: int
        INVALID_HOTEL_CUSTOMER_LINK: int
        MISSING_HOTEL_SETTING: int
        CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP: int
        APP_NOT_FOUND: int
        SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE: int
        MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS: int
        INSUFFICIENT_APP_INSTALLS_COUNT: int
        SENSITIVE_CATEGORY_APP: int
        HEC_AGREEMENT_REQUIRED: int
        NOT_COMPATIBLE_WITH_VIEW_THROUGH_CONVERSION_OPTIMIZATION: int
        INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE: int
        CANNOT_CREATE_APP_PRE_REGISTRATION_FOR_NON_ANDROID_APP: int
        APP_NOT_AVAILABLE_TO_CREATE_APP_PRE_REGISTRATION_CAMPAIGN: int
        INCOMPATIBLE_BUDGET_TYPE: int
