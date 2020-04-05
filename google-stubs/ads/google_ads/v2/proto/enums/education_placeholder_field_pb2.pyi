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

class EducationPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class EducationPlaceholderField(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "EducationPlaceholderFieldEnum.EducationPlaceholderField": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List[
            "EducationPlaceholderFieldEnum.EducationPlaceholderField"
        ]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "EducationPlaceholderFieldEnum.EducationPlaceholderField"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 0
        )
        UNKNOWN = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 1
        )
        PROGRAM_ID = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 2
        )
        LOCATION_ID = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 3
        )
        PROGRAM_NAME = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 4
        )
        AREA_OF_STUDY = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 5
        )
        PROGRAM_DESCRIPTION = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 6
        )
        SCHOOL_NAME = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 7
        )
        ADDRESS = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 8
        )
        THUMBNAIL_IMAGE_URL = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 9
        )
        ALTERNATIVE_THUMBNAIL_IMAGE_URL = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 10
        )
        FINAL_URLS = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 11
        )
        FINAL_MOBILE_URLS = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 12
        )
        TRACKING_URL = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 13
        )
        CONTEXTUAL_KEYWORDS = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 14
        )
        ANDROID_APP_LINK = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 15
        )
        SIMILAR_PROGRAM_IDS = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 16
        )
        IOS_APP_LINK = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 17
        )
        IOS_APP_STORE_ID = typing___cast(
            "EducationPlaceholderFieldEnum.EducationPlaceholderField", 18
        )
    UNSPECIFIED = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 0
    )
    UNKNOWN = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 1
    )
    PROGRAM_ID = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 2
    )
    LOCATION_ID = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 3
    )
    PROGRAM_NAME = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 4
    )
    AREA_OF_STUDY = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 5
    )
    PROGRAM_DESCRIPTION = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 6
    )
    SCHOOL_NAME = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 7
    )
    ADDRESS = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 8
    )
    THUMBNAIL_IMAGE_URL = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 9
    )
    ALTERNATIVE_THUMBNAIL_IMAGE_URL = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 10
    )
    FINAL_URLS = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 11
    )
    FINAL_MOBILE_URLS = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 12
    )
    TRACKING_URL = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 13
    )
    CONTEXTUAL_KEYWORDS = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 14
    )
    ANDROID_APP_LINK = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 15
    )
    SIMILAR_PROGRAM_IDS = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 16
    )
    IOS_APP_LINK = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 17
    )
    IOS_APP_STORE_ID = typing___cast(
        "EducationPlaceholderFieldEnum.EducationPlaceholderField", 18
    )
    global___EducationPlaceholderField = EducationPlaceholderField
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> EducationPlaceholderFieldEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> EducationPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___EducationPlaceholderFieldEnum = EducationPlaceholderFieldEnum
