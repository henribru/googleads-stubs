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


class LegacyAppInstallAdAppStoreEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class LegacyAppInstallAdAppStore(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore']]: ...
        UNSPECIFIED = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 0)
        UNKNOWN = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 1)
        APPLE_APP_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 2)
        GOOGLE_PLAY = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 3)
        WINDOWS_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 4)
        WINDOWS_PHONE_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 5)
        CN_APP_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 6)
    UNSPECIFIED = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 0)
    UNKNOWN = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 1)
    APPLE_APP_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 2)
    GOOGLE_PLAY = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 3)
    WINDOWS_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 4)
    WINDOWS_PHONE_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 5)
    CN_APP_STORE = typing___cast('LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore', 6)
    global___LegacyAppInstallAdAppStore = LegacyAppInstallAdAppStore


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LegacyAppInstallAdAppStoreEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LegacyAppInstallAdAppStoreEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___LegacyAppInstallAdAppStoreEnum = LegacyAppInstallAdAppStoreEnum
