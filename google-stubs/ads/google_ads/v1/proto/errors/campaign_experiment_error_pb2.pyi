# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)


builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class CampaignExperimentErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CampaignExperimentError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'CampaignExperimentErrorEnum.CampaignExperimentError': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['CampaignExperimentErrorEnum.CampaignExperimentError']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'CampaignExperimentErrorEnum.CampaignExperimentError']]: ...
        UNSPECIFIED = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 0)
        UNKNOWN = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 1)
        DUPLICATE_NAME = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 2)
        INVALID_TRANSITION = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 3)
        CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 4)
        CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 5)
        CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 6)
        CUSTOMER_CANNOT_CREATE_EXPERIMENT = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 7)
        CAMPAIGN_CANNOT_CREATE_EXPERIMENT = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 8)
        EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 9)
        EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 10)
        CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 11)
    UNSPECIFIED = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 0)
    UNKNOWN = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 1)
    DUPLICATE_NAME = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 2)
    INVALID_TRANSITION = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 3)
    CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 4)
    CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 5)
    CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 6)
    CUSTOMER_CANNOT_CREATE_EXPERIMENT = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 7)
    CAMPAIGN_CANNOT_CREATE_EXPERIMENT = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 8)
    EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 9)
    EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 10)
    CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS = typing___cast('CampaignExperimentErrorEnum.CampaignExperimentError', 11)
    global___CampaignExperimentError = CampaignExperimentError


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CampaignExperimentErrorEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CampaignExperimentErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___CampaignExperimentErrorEnum = CampaignExperimentErrorEnum
