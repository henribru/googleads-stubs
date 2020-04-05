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

class MediaBundleErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MediaBundleError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "MediaBundleErrorEnum.MediaBundleError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["MediaBundleErrorEnum.MediaBundleError"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "MediaBundleErrorEnum.MediaBundleError"]
        ]: ...
        UNSPECIFIED = typing___cast("MediaBundleErrorEnum.MediaBundleError", 0)
        UNKNOWN = typing___cast("MediaBundleErrorEnum.MediaBundleError", 1)
        BAD_REQUEST = typing___cast("MediaBundleErrorEnum.MediaBundleError", 3)
        DOUBLECLICK_BUNDLE_NOT_ALLOWED = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 4
        )
        EXTERNAL_URL_NOT_ALLOWED = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 5
        )
        FILE_TOO_LARGE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 6)
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 7
        )
        INVALID_INPUT = typing___cast("MediaBundleErrorEnum.MediaBundleError", 8)
        INVALID_MEDIA_BUNDLE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 9)
        INVALID_MEDIA_BUNDLE_ENTRY = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 10
        )
        INVALID_MIME_TYPE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 11)
        INVALID_PATH = typing___cast("MediaBundleErrorEnum.MediaBundleError", 12)
        INVALID_URL_REFERENCE = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 13
        )
        MEDIA_DATA_TOO_LARGE = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 14
        )
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 15
        )
        SERVER_ERROR = typing___cast("MediaBundleErrorEnum.MediaBundleError", 16)
        STORAGE_ERROR = typing___cast("MediaBundleErrorEnum.MediaBundleError", 17)
        SWIFFY_BUNDLE_NOT_ALLOWED = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 18
        )
        TOO_MANY_FILES = typing___cast("MediaBundleErrorEnum.MediaBundleError", 19)
        UNEXPECTED_SIZE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 20)
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 21
        )
        UNSUPPORTED_HTML5_FEATURE = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 22
        )
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 23
        )
        CUSTOM_EXIT_NOT_ALLOWED = typing___cast(
            "MediaBundleErrorEnum.MediaBundleError", 24
        )
    UNSPECIFIED = typing___cast("MediaBundleErrorEnum.MediaBundleError", 0)
    UNKNOWN = typing___cast("MediaBundleErrorEnum.MediaBundleError", 1)
    BAD_REQUEST = typing___cast("MediaBundleErrorEnum.MediaBundleError", 3)
    DOUBLECLICK_BUNDLE_NOT_ALLOWED = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 4
    )
    EXTERNAL_URL_NOT_ALLOWED = typing___cast("MediaBundleErrorEnum.MediaBundleError", 5)
    FILE_TOO_LARGE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 6)
    GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 7
    )
    INVALID_INPUT = typing___cast("MediaBundleErrorEnum.MediaBundleError", 8)
    INVALID_MEDIA_BUNDLE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 9)
    INVALID_MEDIA_BUNDLE_ENTRY = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 10
    )
    INVALID_MIME_TYPE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 11)
    INVALID_PATH = typing___cast("MediaBundleErrorEnum.MediaBundleError", 12)
    INVALID_URL_REFERENCE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 13)
    MEDIA_DATA_TOO_LARGE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 14)
    MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 15
    )
    SERVER_ERROR = typing___cast("MediaBundleErrorEnum.MediaBundleError", 16)
    STORAGE_ERROR = typing___cast("MediaBundleErrorEnum.MediaBundleError", 17)
    SWIFFY_BUNDLE_NOT_ALLOWED = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 18
    )
    TOO_MANY_FILES = typing___cast("MediaBundleErrorEnum.MediaBundleError", 19)
    UNEXPECTED_SIZE = typing___cast("MediaBundleErrorEnum.MediaBundleError", 20)
    UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 21
    )
    UNSUPPORTED_HTML5_FEATURE = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 22
    )
    URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT = typing___cast(
        "MediaBundleErrorEnum.MediaBundleError", 23
    )
    CUSTOM_EXIT_NOT_ALLOWED = typing___cast("MediaBundleErrorEnum.MediaBundleError", 24)
    global___MediaBundleError = MediaBundleError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MediaBundleErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MediaBundleErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___MediaBundleErrorEnum = MediaBundleErrorEnum
