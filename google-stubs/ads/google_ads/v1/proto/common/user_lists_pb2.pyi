# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.customer_match_upload_key_type_pb2 import (
    CustomerMatchUploadKeyTypeEnum as google___ads___googleads___v1___enums___customer_match_upload_key_type_pb2___CustomerMatchUploadKeyTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_combined_rule_operator_pb2 import (
    UserListCombinedRuleOperatorEnum as google___ads___googleads___v1___enums___user_list_combined_rule_operator_pb2___UserListCombinedRuleOperatorEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_crm_data_source_type_pb2 import (
    UserListCrmDataSourceTypeEnum as google___ads___googleads___v1___enums___user_list_crm_data_source_type_pb2___UserListCrmDataSourceTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_date_rule_item_operator_pb2 import (
    UserListDateRuleItemOperatorEnum as google___ads___googleads___v1___enums___user_list_date_rule_item_operator_pb2___UserListDateRuleItemOperatorEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_logical_rule_operator_pb2 import (
    UserListLogicalRuleOperatorEnum as google___ads___googleads___v1___enums___user_list_logical_rule_operator_pb2___UserListLogicalRuleOperatorEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_number_rule_item_operator_pb2 import (
    UserListNumberRuleItemOperatorEnum as google___ads___googleads___v1___enums___user_list_number_rule_item_operator_pb2___UserListNumberRuleItemOperatorEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_prepopulation_status_pb2 import (
    UserListPrepopulationStatusEnum as google___ads___googleads___v1___enums___user_list_prepopulation_status_pb2___UserListPrepopulationStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_rule_type_pb2 import (
    UserListRuleTypeEnum as google___ads___googleads___v1___enums___user_list_rule_type_pb2___UserListRuleTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_string_rule_item_operator_pb2 import (
    UserListStringRuleItemOperatorEnum as google___ads___googleads___v1___enums___user_list_string_rule_item_operator_pb2___UserListStringRuleItemOperatorEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class SimilarUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def seed_user_list(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        seed_user_list : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SimilarUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SimilarUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"seed_user_list",b"seed_user_list"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"seed_user_list",b"seed_user_list"]) -> None: ...
global___SimilarUserListInfo = SimilarUserListInfo

class CrmBasedUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    upload_key_type = ... # type: google___ads___googleads___v1___enums___customer_match_upload_key_type_pb2___CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    data_source_type = ... # type: google___ads___googleads___v1___enums___user_list_crm_data_source_type_pb2___UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType

    @property
    def app_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        app_id : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        upload_key_type : typing___Optional[google___ads___googleads___v1___enums___customer_match_upload_key_type_pb2___CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType] = None,
        data_source_type : typing___Optional[google___ads___googleads___v1___enums___user_list_crm_data_source_type_pb2___UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CrmBasedUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CrmBasedUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"data_source_type",b"data_source_type",u"upload_key_type",b"upload_key_type"]) -> None: ...
global___CrmBasedUserListInfo = CrmBasedUserListInfo

class UserListRuleInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    rule_type = ... # type: google___ads___googleads___v1___enums___user_list_rule_type_pb2___UserListRuleTypeEnum.UserListRuleType

    @property
    def rule_item_groups(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___UserListRuleItemGroupInfo]: ...

    def __init__(self,
        *,
        rule_type : typing___Optional[google___ads___googleads___v1___enums___user_list_rule_type_pb2___UserListRuleTypeEnum.UserListRuleType] = None,
        rule_item_groups : typing___Optional[typing___Iterable[global___UserListRuleItemGroupInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListRuleInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListRuleInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"rule_item_groups",b"rule_item_groups",u"rule_type",b"rule_type"]) -> None: ...
global___UserListRuleInfo = UserListRuleInfo

class UserListRuleItemGroupInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rule_items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___UserListRuleItemInfo]: ...

    def __init__(self,
        *,
        rule_items : typing___Optional[typing___Iterable[global___UserListRuleItemInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListRuleItemGroupInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListRuleItemGroupInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"rule_items",b"rule_items"]) -> None: ...
global___UserListRuleItemGroupInfo = UserListRuleItemGroupInfo

class UserListRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def number_rule_item(self) -> global___UserListNumberRuleItemInfo: ...

    @property
    def string_rule_item(self) -> global___UserListStringRuleItemInfo: ...

    @property
    def date_rule_item(self) -> global___UserListDateRuleItemInfo: ...

    def __init__(self,
        *,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        number_rule_item : typing___Optional[global___UserListNumberRuleItemInfo] = None,
        string_rule_item : typing___Optional[global___UserListStringRuleItemInfo] = None,
        date_rule_item : typing___Optional[global___UserListDateRuleItemInfo] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListRuleItemInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListRuleItemInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"date_rule_item",b"date_rule_item",u"name",b"name",u"number_rule_item",b"number_rule_item",u"rule_item",b"rule_item",u"string_rule_item",b"string_rule_item"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"date_rule_item",b"date_rule_item",u"name",b"name",u"number_rule_item",b"number_rule_item",u"rule_item",b"rule_item",u"string_rule_item",b"string_rule_item"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"rule_item",b"rule_item"]) -> typing_extensions___Literal["number_rule_item","string_rule_item","date_rule_item"]: ...
global___UserListRuleItemInfo = UserListRuleItemInfo

class UserListDateRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator = ... # type: google___ads___googleads___v1___enums___user_list_date_rule_item_operator_pb2___UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator

    @property
    def value(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def offset_in_days(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        operator : typing___Optional[google___ads___googleads___v1___enums___user_list_date_rule_item_operator_pb2___UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator] = None,
        value : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        offset_in_days : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListDateRuleItemInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListDateRuleItemInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"offset_in_days",b"offset_in_days",u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"offset_in_days",b"offset_in_days",u"operator",b"operator",u"value",b"value"]) -> None: ...
global___UserListDateRuleItemInfo = UserListDateRuleItemInfo

class UserListNumberRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator = ... # type: google___ads___googleads___v1___enums___user_list_number_rule_item_operator_pb2___UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator

    @property
    def value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    def __init__(self,
        *,
        operator : typing___Optional[google___ads___googleads___v1___enums___user_list_number_rule_item_operator_pb2___UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator] = None,
        value : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListNumberRuleItemInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListNumberRuleItemInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"operator",b"operator",u"value",b"value"]) -> None: ...
global___UserListNumberRuleItemInfo = UserListNumberRuleItemInfo

class UserListStringRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator = ... # type: google___ads___googleads___v1___enums___user_list_string_rule_item_operator_pb2___UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator

    @property
    def value(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        operator : typing___Optional[google___ads___googleads___v1___enums___user_list_string_rule_item_operator_pb2___UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator] = None,
        value : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListStringRuleItemInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListStringRuleItemInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"operator",b"operator",u"value",b"value"]) -> None: ...
global___UserListStringRuleItemInfo = UserListStringRuleItemInfo

class CombinedRuleUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    rule_operator = ... # type: google___ads___googleads___v1___enums___user_list_combined_rule_operator_pb2___UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperator

    @property
    def left_operand(self) -> global___UserListRuleInfo: ...

    @property
    def right_operand(self) -> global___UserListRuleInfo: ...

    def __init__(self,
        *,
        left_operand : typing___Optional[global___UserListRuleInfo] = None,
        right_operand : typing___Optional[global___UserListRuleInfo] = None,
        rule_operator : typing___Optional[google___ads___googleads___v1___enums___user_list_combined_rule_operator_pb2___UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperator] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CombinedRuleUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CombinedRuleUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"left_operand",b"left_operand",u"right_operand",b"right_operand"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"left_operand",b"left_operand",u"right_operand",b"right_operand",u"rule_operator",b"rule_operator"]) -> None: ...
global___CombinedRuleUserListInfo = CombinedRuleUserListInfo

class DateSpecificRuleUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rule(self) -> global___UserListRuleInfo: ...

    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        rule : typing___Optional[global___UserListRuleInfo] = None,
        start_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        end_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DateSpecificRuleUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DateSpecificRuleUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"end_date",b"end_date",u"rule",b"rule",u"start_date",b"start_date"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"end_date",b"end_date",u"rule",b"rule",u"start_date",b"start_date"]) -> None: ...
global___DateSpecificRuleUserListInfo = DateSpecificRuleUserListInfo

class ExpressionRuleUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rule(self) -> global___UserListRuleInfo: ...

    def __init__(self,
        *,
        rule : typing___Optional[global___UserListRuleInfo] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExpressionRuleUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExpressionRuleUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"rule",b"rule"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"rule",b"rule"]) -> None: ...
global___ExpressionRuleUserListInfo = ExpressionRuleUserListInfo

class RuleBasedUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    prepopulation_status = ... # type: google___ads___googleads___v1___enums___user_list_prepopulation_status_pb2___UserListPrepopulationStatusEnum.UserListPrepopulationStatus

    @property
    def combined_rule_user_list(self) -> global___CombinedRuleUserListInfo: ...

    @property
    def date_specific_rule_user_list(self) -> global___DateSpecificRuleUserListInfo: ...

    @property
    def expression_rule_user_list(self) -> global___ExpressionRuleUserListInfo: ...

    def __init__(self,
        *,
        prepopulation_status : typing___Optional[google___ads___googleads___v1___enums___user_list_prepopulation_status_pb2___UserListPrepopulationStatusEnum.UserListPrepopulationStatus] = None,
        combined_rule_user_list : typing___Optional[global___CombinedRuleUserListInfo] = None,
        date_specific_rule_user_list : typing___Optional[global___DateSpecificRuleUserListInfo] = None,
        expression_rule_user_list : typing___Optional[global___ExpressionRuleUserListInfo] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RuleBasedUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RuleBasedUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"combined_rule_user_list",b"combined_rule_user_list",u"date_specific_rule_user_list",b"date_specific_rule_user_list",u"expression_rule_user_list",b"expression_rule_user_list",u"rule_based_user_list",b"rule_based_user_list"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"combined_rule_user_list",b"combined_rule_user_list",u"date_specific_rule_user_list",b"date_specific_rule_user_list",u"expression_rule_user_list",b"expression_rule_user_list",u"prepopulation_status",b"prepopulation_status",u"rule_based_user_list",b"rule_based_user_list"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"rule_based_user_list",b"rule_based_user_list"]) -> typing_extensions___Literal["combined_rule_user_list","date_specific_rule_user_list","expression_rule_user_list"]: ...
global___RuleBasedUserListInfo = RuleBasedUserListInfo

class LogicalUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rules(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___UserListLogicalRuleInfo]: ...

    def __init__(self,
        *,
        rules : typing___Optional[typing___Iterable[global___UserListLogicalRuleInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogicalUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogicalUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"rules",b"rules"]) -> None: ...
global___LogicalUserListInfo = LogicalUserListInfo

class UserListLogicalRuleInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator = ... # type: google___ads___googleads___v1___enums___user_list_logical_rule_operator_pb2___UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator

    @property
    def rule_operands(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___LogicalUserListOperandInfo]: ...

    def __init__(self,
        *,
        operator : typing___Optional[google___ads___googleads___v1___enums___user_list_logical_rule_operator_pb2___UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator] = None,
        rule_operands : typing___Optional[typing___Iterable[global___LogicalUserListOperandInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListLogicalRuleInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListLogicalRuleInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"operator",b"operator",u"rule_operands",b"rule_operands"]) -> None: ...
global___UserListLogicalRuleInfo = UserListLogicalRuleInfo

class LogicalUserListOperandInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def user_list(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        user_list : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogicalUserListOperandInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogicalUserListOperandInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"user_list",b"user_list"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"user_list",b"user_list"]) -> None: ...
global___LogicalUserListOperandInfo = LogicalUserListOperandInfo

class BasicUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def actions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___UserListActionInfo]: ...

    def __init__(self,
        *,
        actions : typing___Optional[typing___Iterable[global___UserListActionInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BasicUserListInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BasicUserListInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actions",b"actions"]) -> None: ...
global___BasicUserListInfo = BasicUserListInfo

class UserListActionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def remarketing_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        conversion_action : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        remarketing_action : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UserListActionInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UserListActionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"conversion_action",b"conversion_action",u"remarketing_action",b"remarketing_action",u"user_list_action",b"user_list_action"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"conversion_action",b"conversion_action",u"remarketing_action",b"remarketing_action",u"user_list_action",b"user_list_action"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"user_list_action",b"user_list_action"]) -> typing_extensions___Literal["conversion_action","remarketing_action"]: ...
global___UserListActionInfo = UserListActionInfo
