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

class AuthenticationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AuthenticationError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "AuthenticationErrorEnum.AuthenticationError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["AuthenticationErrorEnum.AuthenticationError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "AuthenticationErrorEnum.AuthenticationError"]
        ]: ...
        UNSPECIFIED = typing___cast("AuthenticationErrorEnum.AuthenticationError", 0)
        UNKNOWN = typing___cast("AuthenticationErrorEnum.AuthenticationError", 1)
        AUTHENTICATION_ERROR = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 2
        )
        CLIENT_CUSTOMER_ID_INVALID = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 5
        )
        CUSTOMER_NOT_FOUND = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 8
        )
        GOOGLE_ACCOUNT_DELETED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 9
        )
        GOOGLE_ACCOUNT_COOKIE_INVALID = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 10
        )
        GOOGLE_ACCOUNT_AUTHENTICATION_FAILED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 25
        )
        GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 12
        )
        LOGIN_COOKIE_REQUIRED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 13
        )
        NOT_ADS_USER = typing___cast("AuthenticationErrorEnum.AuthenticationError", 14)
        OAUTH_TOKEN_INVALID = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 15
        )
        OAUTH_TOKEN_EXPIRED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 16
        )
        OAUTH_TOKEN_DISABLED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 17
        )
        OAUTH_TOKEN_REVOKED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 18
        )
        OAUTH_TOKEN_HEADER_INVALID = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 19
        )
        LOGIN_COOKIE_INVALID = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 20
        )
        USER_ID_INVALID = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 22
        )
        TWO_STEP_VERIFICATION_NOT_ENROLLED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 23
        )
        ADVANCED_PROTECTION_NOT_ENROLLED = typing___cast(
            "AuthenticationErrorEnum.AuthenticationError", 24
        )
    UNSPECIFIED = typing___cast("AuthenticationErrorEnum.AuthenticationError", 0)
    UNKNOWN = typing___cast("AuthenticationErrorEnum.AuthenticationError", 1)
    AUTHENTICATION_ERROR = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 2
    )
    CLIENT_CUSTOMER_ID_INVALID = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 5
    )
    CUSTOMER_NOT_FOUND = typing___cast("AuthenticationErrorEnum.AuthenticationError", 8)
    GOOGLE_ACCOUNT_DELETED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 9
    )
    GOOGLE_ACCOUNT_COOKIE_INVALID = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 10
    )
    GOOGLE_ACCOUNT_AUTHENTICATION_FAILED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 25
    )
    GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 12
    )
    LOGIN_COOKIE_REQUIRED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 13
    )
    NOT_ADS_USER = typing___cast("AuthenticationErrorEnum.AuthenticationError", 14)
    OAUTH_TOKEN_INVALID = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 15
    )
    OAUTH_TOKEN_EXPIRED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 16
    )
    OAUTH_TOKEN_DISABLED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 17
    )
    OAUTH_TOKEN_REVOKED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 18
    )
    OAUTH_TOKEN_HEADER_INVALID = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 19
    )
    LOGIN_COOKIE_INVALID = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 20
    )
    USER_ID_INVALID = typing___cast("AuthenticationErrorEnum.AuthenticationError", 22)
    TWO_STEP_VERIFICATION_NOT_ENROLLED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 23
    )
    ADVANCED_PROTECTION_NOT_ENROLLED = typing___cast(
        "AuthenticationErrorEnum.AuthenticationError", 24
    )
    global___AuthenticationError = AuthenticationError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AuthenticationErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AuthenticationErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___AuthenticationErrorEnum = AuthenticationErrorEnum