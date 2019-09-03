# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class MediaBundleErrorEnum(google___protobuf___message___Message):
    class MediaBundleError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['BAD_REQUEST'],typing_extensions___Literal['DOUBLECLICK_BUNDLE_NOT_ALLOWED'],typing_extensions___Literal['EXTERNAL_URL_NOT_ALLOWED'],typing_extensions___Literal['FILE_TOO_LARGE'],typing_extensions___Literal['GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED'],typing_extensions___Literal['INVALID_INPUT'],typing_extensions___Literal['INVALID_MEDIA_BUNDLE'],typing_extensions___Literal['INVALID_MEDIA_BUNDLE_ENTRY'],typing_extensions___Literal['INVALID_MIME_TYPE'],typing_extensions___Literal['INVALID_PATH'],typing_extensions___Literal['INVALID_URL_REFERENCE'],typing_extensions___Literal['MEDIA_DATA_TOO_LARGE'],typing_extensions___Literal['MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY'],typing_extensions___Literal['SERVER_ERROR'],typing_extensions___Literal['STORAGE_ERROR'],typing_extensions___Literal['SWIFFY_BUNDLE_NOT_ALLOWED'],typing_extensions___Literal['TOO_MANY_FILES'],typing_extensions___Literal['UNEXPECTED_SIZE'],typing_extensions___Literal['UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT'],typing_extensions___Literal['UNSUPPORTED_HTML5_FEATURE'],typing_extensions___Literal['URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT'],typing_extensions___Literal['CUSTOM_EXIT_NOT_ALLOWED']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[12],typing_extensions___Literal[13],typing_extensions___Literal[14],typing_extensions___Literal[15],typing_extensions___Literal[16],typing_extensions___Literal[17],typing_extensions___Literal[18],typing_extensions___Literal[19],typing_extensions___Literal[20],typing_extensions___Literal[21],typing_extensions___Literal[22],typing_extensions___Literal[23],typing_extensions___Literal[24]]
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: ClosedValueType) -> str: ...
        @classmethod
        def Value(cls, name: ClosedKeyType) -> ClosedValueType: ...
        @classmethod
        def keys(cls) -> typing___List[ClosedKeyType]: ...
        @classmethod
        def values(cls) -> typing___List[ClosedValueType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[ClosedKeyType, ClosedValueType]]: ...
        UNSPECIFIED: typing_extensions___Literal[0]
        UNKNOWN: typing_extensions___Literal[1]
        BAD_REQUEST: typing_extensions___Literal[3]
        DOUBLECLICK_BUNDLE_NOT_ALLOWED: typing_extensions___Literal[4]
        EXTERNAL_URL_NOT_ALLOWED: typing_extensions___Literal[5]
        FILE_TOO_LARGE: typing_extensions___Literal[6]
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: typing_extensions___Literal[7]
        INVALID_INPUT: typing_extensions___Literal[8]
        INVALID_MEDIA_BUNDLE: typing_extensions___Literal[9]
        INVALID_MEDIA_BUNDLE_ENTRY: typing_extensions___Literal[10]
        INVALID_MIME_TYPE: typing_extensions___Literal[11]
        INVALID_PATH: typing_extensions___Literal[12]
        INVALID_URL_REFERENCE: typing_extensions___Literal[13]
        MEDIA_DATA_TOO_LARGE: typing_extensions___Literal[14]
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: typing_extensions___Literal[15]
        SERVER_ERROR: typing_extensions___Literal[16]
        STORAGE_ERROR: typing_extensions___Literal[17]
        SWIFFY_BUNDLE_NOT_ALLOWED: typing_extensions___Literal[18]
        TOO_MANY_FILES: typing_extensions___Literal[19]
        UNEXPECTED_SIZE: typing_extensions___Literal[20]
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: typing_extensions___Literal[21]
        UNSUPPORTED_HTML5_FEATURE: typing_extensions___Literal[22]
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: typing_extensions___Literal[23]
        CUSTOM_EXIT_NOT_ALLOWED: typing_extensions___Literal[24]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    BAD_REQUEST: typing_extensions___Literal[3]
    DOUBLECLICK_BUNDLE_NOT_ALLOWED: typing_extensions___Literal[4]
    EXTERNAL_URL_NOT_ALLOWED: typing_extensions___Literal[5]
    FILE_TOO_LARGE: typing_extensions___Literal[6]
    GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: typing_extensions___Literal[7]
    INVALID_INPUT: typing_extensions___Literal[8]
    INVALID_MEDIA_BUNDLE: typing_extensions___Literal[9]
    INVALID_MEDIA_BUNDLE_ENTRY: typing_extensions___Literal[10]
    INVALID_MIME_TYPE: typing_extensions___Literal[11]
    INVALID_PATH: typing_extensions___Literal[12]
    INVALID_URL_REFERENCE: typing_extensions___Literal[13]
    MEDIA_DATA_TOO_LARGE: typing_extensions___Literal[14]
    MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: typing_extensions___Literal[15]
    SERVER_ERROR: typing_extensions___Literal[16]
    STORAGE_ERROR: typing_extensions___Literal[17]
    SWIFFY_BUNDLE_NOT_ALLOWED: typing_extensions___Literal[18]
    TOO_MANY_FILES: typing_extensions___Literal[19]
    UNEXPECTED_SIZE: typing_extensions___Literal[20]
    UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: typing_extensions___Literal[21]
    UNSUPPORTED_HTML5_FEATURE: typing_extensions___Literal[22]
    URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: typing_extensions___Literal[23]
    CUSTOM_EXIT_NOT_ALLOWED: typing_extensions___Literal[24]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MediaBundleErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
