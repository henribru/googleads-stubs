# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.customer_match_upload_key_type_pb2 import (
    CustomerMatchUploadKeyTypeEnum as google___ads___googleads___v5___enums___customer_match_upload_key_type_pb2___CustomerMatchUploadKeyTypeEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_combined_rule_operator_pb2 import (
    UserListCombinedRuleOperatorEnum as google___ads___googleads___v5___enums___user_list_combined_rule_operator_pb2___UserListCombinedRuleOperatorEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_crm_data_source_type_pb2 import (
    UserListCrmDataSourceTypeEnum as google___ads___googleads___v5___enums___user_list_crm_data_source_type_pb2___UserListCrmDataSourceTypeEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_date_rule_item_operator_pb2 import (
    UserListDateRuleItemOperatorEnum as google___ads___googleads___v5___enums___user_list_date_rule_item_operator_pb2___UserListDateRuleItemOperatorEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_logical_rule_operator_pb2 import (
    UserListLogicalRuleOperatorEnum as google___ads___googleads___v5___enums___user_list_logical_rule_operator_pb2___UserListLogicalRuleOperatorEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_number_rule_item_operator_pb2 import (
    UserListNumberRuleItemOperatorEnum as google___ads___googleads___v5___enums___user_list_number_rule_item_operator_pb2___UserListNumberRuleItemOperatorEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_prepopulation_status_pb2 import (
    UserListPrepopulationStatusEnum as google___ads___googleads___v5___enums___user_list_prepopulation_status_pb2___UserListPrepopulationStatusEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_rule_type_pb2 import (
    UserListRuleTypeEnum as google___ads___googleads___v5___enums___user_list_rule_type_pb2___UserListRuleTypeEnum,
)

from google.ads.google_ads.v5.proto.enums.user_list_string_rule_item_operator_pb2 import (
    UserListStringRuleItemOperatorEnum as google___ads___googleads___v5___enums___user_list_string_rule_item_operator_pb2___UserListStringRuleItemOperatorEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SimilarUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def seed_user_list(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        seed_user_list: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["seed_user_list", b"seed_user_list"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["seed_user_list", b"seed_user_list"],
    ) -> None: ...

type___SimilarUserListInfo = SimilarUserListInfo

class CrmBasedUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    upload_key_type: google___ads___googleads___v5___enums___customer_match_upload_key_type_pb2___CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyTypeValue = ...
    data_source_type: google___ads___googleads___v5___enums___user_list_crm_data_source_type_pb2___UserListCrmDataSourceTypeEnum.UserListCrmDataSourceTypeValue = ...
    @property
    def app_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        app_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        upload_key_type: typing___Optional[
            google___ads___googleads___v5___enums___customer_match_upload_key_type_pb2___CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyTypeValue
        ] = None,
        data_source_type: typing___Optional[
            google___ads___googleads___v5___enums___user_list_crm_data_source_type_pb2___UserListCrmDataSourceTypeEnum.UserListCrmDataSourceTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["app_id", b"app_id"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "app_id",
            b"app_id",
            "data_source_type",
            b"data_source_type",
            "upload_key_type",
            b"upload_key_type",
        ],
    ) -> None: ...

type___CrmBasedUserListInfo = CrmBasedUserListInfo

class UserListRuleInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    rule_type: google___ads___googleads___v5___enums___user_list_rule_type_pb2___UserListRuleTypeEnum.UserListRuleTypeValue = ...
    @property
    def rule_item_groups(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___UserListRuleItemGroupInfo
    ]: ...
    def __init__(
        self,
        *,
        rule_type: typing___Optional[
            google___ads___googleads___v5___enums___user_list_rule_type_pb2___UserListRuleTypeEnum.UserListRuleTypeValue
        ] = None,
        rule_item_groups: typing___Optional[
            typing___Iterable[type___UserListRuleItemGroupInfo]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "rule_item_groups", b"rule_item_groups", "rule_type", b"rule_type"
        ],
    ) -> None: ...

type___UserListRuleInfo = UserListRuleInfo

class UserListRuleItemGroupInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def rule_items(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___UserListRuleItemInfo
    ]: ...
    def __init__(
        self,
        *,
        rule_items: typing___Optional[
            typing___Iterable[type___UserListRuleItemInfo]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["rule_items", b"rule_items"]
    ) -> None: ...

type___UserListRuleItemGroupInfo = UserListRuleItemGroupInfo

class UserListRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def number_rule_item(self) -> type___UserListNumberRuleItemInfo: ...
    @property
    def string_rule_item(self) -> type___UserListStringRuleItemInfo: ...
    @property
    def date_rule_item(self) -> type___UserListDateRuleItemInfo: ...
    def __init__(
        self,
        *,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        number_rule_item: typing___Optional[type___UserListNumberRuleItemInfo] = None,
        string_rule_item: typing___Optional[type___UserListStringRuleItemInfo] = None,
        date_rule_item: typing___Optional[type___UserListDateRuleItemInfo] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "date_rule_item",
            b"date_rule_item",
            "name",
            b"name",
            "number_rule_item",
            b"number_rule_item",
            "rule_item",
            b"rule_item",
            "string_rule_item",
            b"string_rule_item",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "date_rule_item",
            b"date_rule_item",
            "name",
            b"name",
            "number_rule_item",
            b"number_rule_item",
            "rule_item",
            b"rule_item",
            "string_rule_item",
            b"string_rule_item",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["rule_item", b"rule_item"]
    ) -> typing_extensions___Literal[
        "number_rule_item", "string_rule_item", "date_rule_item"
    ]: ...

type___UserListRuleItemInfo = UserListRuleItemInfo

class UserListDateRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator: google___ads___googleads___v5___enums___user_list_date_rule_item_operator_pb2___UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperatorValue = ...
    @property
    def value(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def offset_in_days(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        operator: typing___Optional[
            google___ads___googleads___v5___enums___user_list_date_rule_item_operator_pb2___UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperatorValue
        ] = None,
        value: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        offset_in_days: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "offset_in_days", b"offset_in_days", "value", b"value"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "offset_in_days",
            b"offset_in_days",
            "operator",
            b"operator",
            "value",
            b"value",
        ],
    ) -> None: ...

type___UserListDateRuleItemInfo = UserListDateRuleItemInfo

class UserListNumberRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator: google___ads___googleads___v5___enums___user_list_number_rule_item_operator_pb2___UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue = ...
    @property
    def value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    def __init__(
        self,
        *,
        operator: typing___Optional[
            google___ads___googleads___v5___enums___user_list_number_rule_item_operator_pb2___UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue
        ] = None,
        value: typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["value", b"value"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operator", b"operator", "value", b"value"
        ],
    ) -> None: ...

type___UserListNumberRuleItemInfo = UserListNumberRuleItemInfo

class UserListStringRuleItemInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator: google___ads___googleads___v5___enums___user_list_string_rule_item_operator_pb2___UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperatorValue = ...
    @property
    def value(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        operator: typing___Optional[
            google___ads___googleads___v5___enums___user_list_string_rule_item_operator_pb2___UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperatorValue
        ] = None,
        value: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["value", b"value"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operator", b"operator", "value", b"value"
        ],
    ) -> None: ...

type___UserListStringRuleItemInfo = UserListStringRuleItemInfo

class CombinedRuleUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    rule_operator: google___ads___googleads___v5___enums___user_list_combined_rule_operator_pb2___UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperatorValue = ...
    @property
    def left_operand(self) -> type___UserListRuleInfo: ...
    @property
    def right_operand(self) -> type___UserListRuleInfo: ...
    def __init__(
        self,
        *,
        left_operand: typing___Optional[type___UserListRuleInfo] = None,
        right_operand: typing___Optional[type___UserListRuleInfo] = None,
        rule_operator: typing___Optional[
            google___ads___googleads___v5___enums___user_list_combined_rule_operator_pb2___UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperatorValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "left_operand", b"left_operand", "right_operand", b"right_operand"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "left_operand",
            b"left_operand",
            "right_operand",
            b"right_operand",
            "rule_operator",
            b"rule_operator",
        ],
    ) -> None: ...

type___CombinedRuleUserListInfo = CombinedRuleUserListInfo

class DateSpecificRuleUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def rule(self) -> type___UserListRuleInfo: ...
    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        rule: typing___Optional[type___UserListRuleInfo] = None,
        start_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        end_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "end_date", b"end_date", "rule", b"rule", "start_date", b"start_date"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "end_date", b"end_date", "rule", b"rule", "start_date", b"start_date"
        ],
    ) -> None: ...

type___DateSpecificRuleUserListInfo = DateSpecificRuleUserListInfo

class ExpressionRuleUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def rule(self) -> type___UserListRuleInfo: ...
    def __init__(
        self, *, rule: typing___Optional[type___UserListRuleInfo] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["rule", b"rule"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["rule", b"rule"]
    ) -> None: ...

type___ExpressionRuleUserListInfo = ExpressionRuleUserListInfo

class RuleBasedUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    prepopulation_status: google___ads___googleads___v5___enums___user_list_prepopulation_status_pb2___UserListPrepopulationStatusEnum.UserListPrepopulationStatusValue = ...
    @property
    def combined_rule_user_list(self) -> type___CombinedRuleUserListInfo: ...
    @property
    def date_specific_rule_user_list(self) -> type___DateSpecificRuleUserListInfo: ...
    @property
    def expression_rule_user_list(self) -> type___ExpressionRuleUserListInfo: ...
    def __init__(
        self,
        *,
        prepopulation_status: typing___Optional[
            google___ads___googleads___v5___enums___user_list_prepopulation_status_pb2___UserListPrepopulationStatusEnum.UserListPrepopulationStatusValue
        ] = None,
        combined_rule_user_list: typing___Optional[
            type___CombinedRuleUserListInfo
        ] = None,
        date_specific_rule_user_list: typing___Optional[
            type___DateSpecificRuleUserListInfo
        ] = None,
        expression_rule_user_list: typing___Optional[
            type___ExpressionRuleUserListInfo
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "combined_rule_user_list",
            b"combined_rule_user_list",
            "date_specific_rule_user_list",
            b"date_specific_rule_user_list",
            "expression_rule_user_list",
            b"expression_rule_user_list",
            "rule_based_user_list",
            b"rule_based_user_list",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "combined_rule_user_list",
            b"combined_rule_user_list",
            "date_specific_rule_user_list",
            b"date_specific_rule_user_list",
            "expression_rule_user_list",
            b"expression_rule_user_list",
            "prepopulation_status",
            b"prepopulation_status",
            "rule_based_user_list",
            b"rule_based_user_list",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "rule_based_user_list", b"rule_based_user_list"
        ],
    ) -> typing_extensions___Literal[
        "combined_rule_user_list",
        "date_specific_rule_user_list",
        "expression_rule_user_list",
    ]: ...

type___RuleBasedUserListInfo = RuleBasedUserListInfo

class LogicalUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def rules(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___UserListLogicalRuleInfo
    ]: ...
    def __init__(
        self,
        *,
        rules: typing___Optional[
            typing___Iterable[type___UserListLogicalRuleInfo]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["rules", b"rules"]
    ) -> None: ...

type___LogicalUserListInfo = LogicalUserListInfo

class UserListLogicalRuleInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator: google___ads___googleads___v5___enums___user_list_logical_rule_operator_pb2___UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperatorValue = ...
    @property
    def rule_operands(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___LogicalUserListOperandInfo
    ]: ...
    def __init__(
        self,
        *,
        operator: typing___Optional[
            google___ads___googleads___v5___enums___user_list_logical_rule_operator_pb2___UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperatorValue
        ] = None,
        rule_operands: typing___Optional[
            typing___Iterable[type___LogicalUserListOperandInfo]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operator", b"operator", "rule_operands", b"rule_operands"
        ],
    ) -> None: ...

type___UserListLogicalRuleInfo = UserListLogicalRuleInfo

class LogicalUserListOperandInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def user_list(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        user_list: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["user_list", b"user_list"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["user_list", b"user_list"]
    ) -> None: ...

type___LogicalUserListOperandInfo = LogicalUserListOperandInfo

class BasicUserListInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def actions(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___UserListActionInfo
    ]: ...
    def __init__(
        self,
        *,
        actions: typing___Optional[typing___Iterable[type___UserListActionInfo]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["actions", b"actions"]
    ) -> None: ...

type___BasicUserListInfo = BasicUserListInfo

class UserListActionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def remarketing_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        remarketing_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "remarketing_action",
            b"remarketing_action",
            "user_list_action",
            b"user_list_action",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "remarketing_action",
            b"remarketing_action",
            "user_list_action",
            b"user_list_action",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "user_list_action", b"user_list_action"
        ],
    ) -> typing_extensions___Literal["conversion_action", "remarketing_action"]: ...

type___UserListActionInfo = UserListActionInfo
