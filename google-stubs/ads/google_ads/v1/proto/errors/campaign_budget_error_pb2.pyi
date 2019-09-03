# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CampaignBudgetErrorEnum(google___protobuf___message___Message):
    class CampaignBudgetError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['CAMPAIGN_BUDGET_CANNOT_BE_SHARED'],typing_extensions___Literal['CAMPAIGN_BUDGET_REMOVED'],typing_extensions___Literal['CAMPAIGN_BUDGET_IN_USE'],typing_extensions___Literal['CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE'],typing_extensions___Literal['CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET'],typing_extensions___Literal['CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED'],typing_extensions___Literal['CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME'],typing_extensions___Literal['CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED'],typing_extensions___Literal['CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS'],typing_extensions___Literal['DUPLICATE_NAME'],typing_extensions___Literal['MONEY_AMOUNT_IN_WRONG_CURRENCY'],typing_extensions___Literal['MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC'],typing_extensions___Literal['MONEY_AMOUNT_TOO_LARGE'],typing_extensions___Literal['NEGATIVE_MONEY_AMOUNT'],typing_extensions___Literal['NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[17],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[12],typing_extensions___Literal[13],typing_extensions___Literal[14],typing_extensions___Literal[15],typing_extensions___Literal[16]]
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: ClosedValueType) -> str: ...
        @classmethod
        def Value(cls, name: ClosedKeyType) -> ClosedValueType: ...
        @classmethod
        def keys(cls) -> typing___List[ClosedKeyType]: ...
        @classmethod
        def values(cls) -> typing___List[ClosedValueType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[ClosedKeyType, ClosedValueType]]: ...
        UNSPECIFIED: typing_extensions___Literal[0]
        UNKNOWN: typing_extensions___Literal[1]
        CAMPAIGN_BUDGET_CANNOT_BE_SHARED: typing_extensions___Literal[17]
        CAMPAIGN_BUDGET_REMOVED: typing_extensions___Literal[2]
        CAMPAIGN_BUDGET_IN_USE: typing_extensions___Literal[3]
        CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE: typing_extensions___Literal[4]
        CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET: typing_extensions___Literal[6]
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED: typing_extensions___Literal[7]
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME: typing_extensions___Literal[8]
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED: typing_extensions___Literal[9]
        CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS: typing_extensions___Literal[10]
        DUPLICATE_NAME: typing_extensions___Literal[11]
        MONEY_AMOUNT_IN_WRONG_CURRENCY: typing_extensions___Literal[12]
        MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC: typing_extensions___Literal[13]
        MONEY_AMOUNT_TOO_LARGE: typing_extensions___Literal[14]
        NEGATIVE_MONEY_AMOUNT: typing_extensions___Literal[15]
        NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT: typing_extensions___Literal[16]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    CAMPAIGN_BUDGET_CANNOT_BE_SHARED: typing_extensions___Literal[17]
    CAMPAIGN_BUDGET_REMOVED: typing_extensions___Literal[2]
    CAMPAIGN_BUDGET_IN_USE: typing_extensions___Literal[3]
    CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE: typing_extensions___Literal[4]
    CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET: typing_extensions___Literal[6]
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED: typing_extensions___Literal[7]
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME: typing_extensions___Literal[8]
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED: typing_extensions___Literal[9]
    CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS: typing_extensions___Literal[10]
    DUPLICATE_NAME: typing_extensions___Literal[11]
    MONEY_AMOUNT_IN_WRONG_CURRENCY: typing_extensions___Literal[12]
    MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC: typing_extensions___Literal[13]
    MONEY_AMOUNT_TOO_LARGE: typing_extensions___Literal[14]
    NEGATIVE_MONEY_AMOUNT: typing_extensions___Literal[15]
    NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT: typing_extensions___Literal[16]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CampaignBudgetErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
