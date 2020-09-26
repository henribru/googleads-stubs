# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CampaignExperimentErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CampaignExperimentErrorValue = typing___NewType(
        "CampaignExperimentErrorValue", builtin___int
    )
    type___CampaignExperimentErrorValue = CampaignExperimentErrorValue
    CampaignExperimentError: _CampaignExperimentError
    class _CampaignExperimentError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 0
        )
        UNKNOWN = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 1
        )
        DUPLICATE_NAME = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 2
        )
        INVALID_TRANSITION = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 3
        )
        CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 4
        )
        CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 5
        )
        CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 6
        )
        CUSTOMER_CANNOT_CREATE_EXPERIMENT = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 7
        )
        CAMPAIGN_CANNOT_CREATE_EXPERIMENT = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 8
        )
        EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 9
        )
        EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 10
        )
        CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS = typing___cast(
            CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 11
        )
    UNSPECIFIED = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 0
    )
    UNKNOWN = typing___cast(CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 1)
    DUPLICATE_NAME = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 2
    )
    INVALID_TRANSITION = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 3
    )
    CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 4
    )
    CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 5
    )
    CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 6
    )
    CUSTOMER_CANNOT_CREATE_EXPERIMENT = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 7
    )
    CAMPAIGN_CANNOT_CREATE_EXPERIMENT = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 8
    )
    EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 9
    )
    EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 10
    )
    CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS = typing___cast(
        CampaignExperimentErrorEnum.CampaignExperimentErrorValue, 11
    )
    type___CampaignExperimentError = CampaignExperimentError
    def __init__(self,) -> None: ...

type___CampaignExperimentErrorEnum = CampaignExperimentErrorEnum
