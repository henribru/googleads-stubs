# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

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

class CustomerManagerLinkErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CustomerManagerLinkError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "CustomerManagerLinkErrorEnum.CustomerManagerLinkError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["CustomerManagerLinkErrorEnum.CustomerManagerLinkError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "CustomerManagerLinkErrorEnum.CustomerManagerLinkError"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 0
        )
        UNKNOWN = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 1
        )
        NO_PENDING_INVITE = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 2
        )
        SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 3
        )
        MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 4
        )
        CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 5
        )
        CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 6
        )
        CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 7
        )
        CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 8
        )
        DUPLICATE_CHILD_FOUND = typing___cast(
            "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 9
        )
    UNSPECIFIED = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 0
    )
    UNKNOWN = typing___cast("CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 1)
    NO_PENDING_INVITE = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 2
    )
    SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 3
    )
    MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 4
    )
    CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 5
    )
    CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 6
    )
    CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 7
    )
    CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 8
    )
    DUPLICATE_CHILD_FOUND = typing___cast(
        "CustomerManagerLinkErrorEnum.CustomerManagerLinkError", 9
    )
    global___CustomerManagerLinkError = CustomerManagerLinkError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CustomerManagerLinkErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CustomerManagerLinkErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___CustomerManagerLinkErrorEnum = CustomerManagerLinkErrorEnum
