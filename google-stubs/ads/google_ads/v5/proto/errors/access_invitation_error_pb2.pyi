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

class AccessInvitationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AccessInvitationErrorValue = typing___NewType(
        "AccessInvitationErrorValue", builtin___int
    )
    type___AccessInvitationErrorValue = AccessInvitationErrorValue
    AccessInvitationError: _AccessInvitationError
    class _AccessInvitationError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AccessInvitationErrorEnum.AccessInvitationErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            AccessInvitationErrorEnum.AccessInvitationErrorValue, 0
        )
        UNKNOWN = typing___cast(AccessInvitationErrorEnum.AccessInvitationErrorValue, 1)
        INVALID_EMAIL_ADDRESS = typing___cast(
            AccessInvitationErrorEnum.AccessInvitationErrorValue, 2
        )
        EMAIL_ADDRESS_ALREADY_HAS_ACCESS = typing___cast(
            AccessInvitationErrorEnum.AccessInvitationErrorValue, 3
        )
    UNSPECIFIED = typing___cast(AccessInvitationErrorEnum.AccessInvitationErrorValue, 0)
    UNKNOWN = typing___cast(AccessInvitationErrorEnum.AccessInvitationErrorValue, 1)
    INVALID_EMAIL_ADDRESS = typing___cast(
        AccessInvitationErrorEnum.AccessInvitationErrorValue, 2
    )
    EMAIL_ADDRESS_ALREADY_HAS_ACCESS = typing___cast(
        AccessInvitationErrorEnum.AccessInvitationErrorValue, 3
    )
    type___AccessInvitationError = AccessInvitationError
    def __init__(self,) -> None: ...

type___AccessInvitationErrorEnum = AccessInvitationErrorEnum
