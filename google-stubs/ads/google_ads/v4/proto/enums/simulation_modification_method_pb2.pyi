# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SimulationModificationMethodEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SimulationModificationMethodValue = typing___NewType(
        "SimulationModificationMethodValue", builtin___int
    )
    type___SimulationModificationMethodValue = SimulationModificationMethodValue
    SimulationModificationMethod: _SimulationModificationMethod
    class _SimulationModificationMethod(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SimulationModificationMethodEnum.SimulationModificationMethodValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            SimulationModificationMethodEnum.SimulationModificationMethodValue, 0
        )
        UNKNOWN = typing___cast(
            SimulationModificationMethodEnum.SimulationModificationMethodValue, 1
        )
        UNIFORM = typing___cast(
            SimulationModificationMethodEnum.SimulationModificationMethodValue, 2
        )
        DEFAULT = typing___cast(
            SimulationModificationMethodEnum.SimulationModificationMethodValue, 3
        )
    UNSPECIFIED = typing___cast(
        SimulationModificationMethodEnum.SimulationModificationMethodValue, 0
    )
    UNKNOWN = typing___cast(
        SimulationModificationMethodEnum.SimulationModificationMethodValue, 1
    )
    UNIFORM = typing___cast(
        SimulationModificationMethodEnum.SimulationModificationMethodValue, 2
    )
    DEFAULT = typing___cast(
        SimulationModificationMethodEnum.SimulationModificationMethodValue, 3
    )
    type___SimulationModificationMethod = SimulationModificationMethod
    def __init__(self,) -> None: ...

type___SimulationModificationMethodEnum = SimulationModificationMethodEnum