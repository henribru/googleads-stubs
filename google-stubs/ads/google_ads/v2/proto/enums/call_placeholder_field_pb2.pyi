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

class CallPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CallPlaceholderFieldValue = typing___NewType(
        "CallPlaceholderFieldValue", builtin___int
    )
    type___CallPlaceholderFieldValue = CallPlaceholderFieldValue
    CallPlaceholderField: _CallPlaceholderField
    class _CallPlaceholderField(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CallPlaceholderFieldEnum.CallPlaceholderFieldValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 0
        )
        UNKNOWN = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 1)
        PHONE_NUMBER = typing___cast(
            CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 2
        )
        COUNTRY_CODE = typing___cast(
            CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 3
        )
        TRACKED = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 4)
        CONVERSION_TYPE_ID = typing___cast(
            CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 5
        )
        CONVERSION_REPORTING_STATE = typing___cast(
            CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 6
        )
    UNSPECIFIED = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 0)
    UNKNOWN = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 1)
    PHONE_NUMBER = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 2)
    COUNTRY_CODE = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 3)
    TRACKED = typing___cast(CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 4)
    CONVERSION_TYPE_ID = typing___cast(
        CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 5
    )
    CONVERSION_REPORTING_STATE = typing___cast(
        CallPlaceholderFieldEnum.CallPlaceholderFieldValue, 6
    )
    type___CallPlaceholderField = CallPlaceholderField
    def __init__(self,) -> None: ...

type___CallPlaceholderFieldEnum = CallPlaceholderFieldEnum
