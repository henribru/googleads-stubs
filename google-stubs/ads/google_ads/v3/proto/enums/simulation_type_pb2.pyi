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

class SimulationTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SimulationTypeValue = typing___NewType("SimulationTypeValue", builtin___int)
    type___SimulationTypeValue = SimulationTypeValue
    SimulationType: _SimulationType
    class _SimulationType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SimulationTypeEnum.SimulationTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(SimulationTypeEnum.SimulationTypeValue, 0)
        UNKNOWN = typing___cast(SimulationTypeEnum.SimulationTypeValue, 1)
        CPC_BID = typing___cast(SimulationTypeEnum.SimulationTypeValue, 2)
        CPV_BID = typing___cast(SimulationTypeEnum.SimulationTypeValue, 3)
        TARGET_CPA = typing___cast(SimulationTypeEnum.SimulationTypeValue, 4)
        BID_MODIFIER = typing___cast(SimulationTypeEnum.SimulationTypeValue, 5)
    UNSPECIFIED = typing___cast(SimulationTypeEnum.SimulationTypeValue, 0)
    UNKNOWN = typing___cast(SimulationTypeEnum.SimulationTypeValue, 1)
    CPC_BID = typing___cast(SimulationTypeEnum.SimulationTypeValue, 2)
    CPV_BID = typing___cast(SimulationTypeEnum.SimulationTypeValue, 3)
    TARGET_CPA = typing___cast(SimulationTypeEnum.SimulationTypeValue, 4)
    BID_MODIFIER = typing___cast(SimulationTypeEnum.SimulationTypeValue, 5)
    type___SimulationType = SimulationType
    def __init__(self,) -> None: ...

type___SimulationTypeEnum = SimulationTypeEnum
