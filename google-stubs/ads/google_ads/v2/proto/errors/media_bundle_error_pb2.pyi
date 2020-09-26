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

class MediaBundleErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MediaBundleErrorValue = typing___NewType("MediaBundleErrorValue", builtin___int)
    type___MediaBundleErrorValue = MediaBundleErrorValue
    MediaBundleError: _MediaBundleError
    class _MediaBundleError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MediaBundleErrorEnum.MediaBundleErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 0)
        UNKNOWN = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 1)
        BAD_REQUEST = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 3)
        DOUBLECLICK_BUNDLE_NOT_ALLOWED = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 4
        )
        EXTERNAL_URL_NOT_ALLOWED = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 5
        )
        FILE_TOO_LARGE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 6)
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 7
        )
        INVALID_INPUT = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 8)
        INVALID_MEDIA_BUNDLE = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 9
        )
        INVALID_MEDIA_BUNDLE_ENTRY = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 10
        )
        INVALID_MIME_TYPE = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 11
        )
        INVALID_PATH = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 12)
        INVALID_URL_REFERENCE = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 13
        )
        MEDIA_DATA_TOO_LARGE = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 14
        )
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 15
        )
        SERVER_ERROR = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 16)
        STORAGE_ERROR = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 17)
        SWIFFY_BUNDLE_NOT_ALLOWED = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 18
        )
        TOO_MANY_FILES = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 19)
        UNEXPECTED_SIZE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 20)
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 21
        )
        UNSUPPORTED_HTML5_FEATURE = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 22
        )
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 23
        )
        CUSTOM_EXIT_NOT_ALLOWED = typing___cast(
            MediaBundleErrorEnum.MediaBundleErrorValue, 24
        )
    UNSPECIFIED = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 0)
    UNKNOWN = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 1)
    BAD_REQUEST = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 3)
    DOUBLECLICK_BUNDLE_NOT_ALLOWED = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 4
    )
    EXTERNAL_URL_NOT_ALLOWED = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 5
    )
    FILE_TOO_LARGE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 6)
    GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 7
    )
    INVALID_INPUT = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 8)
    INVALID_MEDIA_BUNDLE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 9)
    INVALID_MEDIA_BUNDLE_ENTRY = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 10
    )
    INVALID_MIME_TYPE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 11)
    INVALID_PATH = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 12)
    INVALID_URL_REFERENCE = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 13
    )
    MEDIA_DATA_TOO_LARGE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 14)
    MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 15
    )
    SERVER_ERROR = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 16)
    STORAGE_ERROR = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 17)
    SWIFFY_BUNDLE_NOT_ALLOWED = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 18
    )
    TOO_MANY_FILES = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 19)
    UNEXPECTED_SIZE = typing___cast(MediaBundleErrorEnum.MediaBundleErrorValue, 20)
    UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 21
    )
    UNSUPPORTED_HTML5_FEATURE = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 22
    )
    URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 23
    )
    CUSTOM_EXIT_NOT_ALLOWED = typing___cast(
        MediaBundleErrorEnum.MediaBundleErrorValue, 24
    )
    type___MediaBundleError = MediaBundleError
    def __init__(self,) -> None: ...

type___MediaBundleErrorEnum = MediaBundleErrorEnum
