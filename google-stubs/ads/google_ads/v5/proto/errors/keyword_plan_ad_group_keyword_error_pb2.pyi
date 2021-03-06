"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class KeywordPlanAdGroupKeywordErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _KeywordPlanAdGroupKeywordError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            KeywordPlanAdGroupKeywordError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(0)
        )
        UNKNOWN = KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(1)
        INVALID_KEYWORD_MATCH_TYPE = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(2)
        )
        DUPLICATE_KEYWORD = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(3)
        )
        KEYWORD_TEXT_TOO_LONG = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(4)
        )
        KEYWORD_HAS_INVALID_CHARS = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(5)
        )
        KEYWORD_HAS_TOO_MANY_WORDS = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(6)
        )
        INVALID_KEYWORD_TEXT = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(7)
        )
        NEGATIVE_KEYWORD_HAS_CPC_BID = (
            KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(8)
        )
    class KeywordPlanAdGroupKeywordError(metaclass=_KeywordPlanAdGroupKeywordError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(0)
    UNKNOWN = KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(1)
    INVALID_KEYWORD_MATCH_TYPE = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(2)
    )
    DUPLICATE_KEYWORD = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(3)
    )
    KEYWORD_TEXT_TOO_LONG = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(4)
    )
    KEYWORD_HAS_INVALID_CHARS = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(5)
    )
    KEYWORD_HAS_TOO_MANY_WORDS = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(6)
    )
    INVALID_KEYWORD_TEXT = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(7)
    )
    NEGATIVE_KEYWORD_HAS_CPC_BID = (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.V(8)
    )
    def __init__(
        self,
    ) -> None: ...

global___KeywordPlanAdGroupKeywordErrorEnum = KeywordPlanAdGroupKeywordErrorEnum
