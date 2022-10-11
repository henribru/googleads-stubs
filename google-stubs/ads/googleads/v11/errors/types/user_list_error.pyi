import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListErrorEnum(proto.Message):
    class UserListError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXTERNAL_REMARKETING_USER_LIST_MUTATE_NOT_SUPPORTED: int
        CONCRETE_TYPE_REQUIRED: int
        CONVERSION_TYPE_ID_REQUIRED: int
        DUPLICATE_CONVERSION_TYPES: int
        INVALID_CONVERSION_TYPE: int
        INVALID_DESCRIPTION: int
        INVALID_NAME: int
        INVALID_TYPE: int
        CAN_NOT_ADD_LOGICAL_LIST_AS_LOGICAL_LIST_OPERAND: int
        INVALID_USER_LIST_LOGICAL_RULE_OPERAND: int
        NAME_ALREADY_USED: int
        NEW_CONVERSION_TYPE_NAME_REQUIRED: int
        CONVERSION_TYPE_NAME_ALREADY_USED: int
        OWNERSHIP_REQUIRED_FOR_SET: int
        USER_LIST_MUTATE_NOT_SUPPORTED: int
        INVALID_RULE: int
        INVALID_DATE_RANGE: int
        CAN_NOT_MUTATE_SENSITIVE_USERLIST: int
        MAX_NUM_RULEBASED_USERLISTS: int
        CANNOT_MODIFY_BILLABLE_RECORD_COUNT: int
        APP_ID_NOT_SET: int
        USERLIST_NAME_IS_RESERVED_FOR_SYSTEM_LIST: int
        ADVERTISER_NOT_ON_ALLOWLIST_FOR_USING_UPLOADED_DATA: int
        RULE_TYPE_IS_NOT_SUPPORTED: int
        CAN_NOT_ADD_A_SIMILAR_USERLIST_AS_LOGICAL_LIST_OPERAND: int
        CAN_NOT_MIX_CRM_BASED_IN_LOGICAL_LIST_WITH_OTHER_LISTS: int