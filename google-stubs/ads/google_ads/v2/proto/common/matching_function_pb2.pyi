# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.matching_function_context_type_pb2 import (
    MatchingFunctionContextTypeEnum as google___ads___googleads___v2___enums___matching_function_context_type_pb2___MatchingFunctionContextTypeEnum,
)

from google.ads.google_ads.v2.proto.enums.matching_function_operator_pb2 import (
    MatchingFunctionOperatorEnum as google___ads___googleads___v2___enums___matching_function_operator_pb2___MatchingFunctionOperatorEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class MatchingFunction(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operator = (
        ...
    )  # type: google___ads___googleads___v2___enums___matching_function_operator_pb2___MatchingFunctionOperatorEnum.MatchingFunctionOperator
    @property
    def function_string(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def left_operands(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___Operand
    ]: ...
    @property
    def right_operands(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___Operand
    ]: ...
    def __init__(
        self,
        *,
        function_string: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        operator: typing___Optional[
            google___ads___googleads___v2___enums___matching_function_operator_pb2___MatchingFunctionOperatorEnum.MatchingFunctionOperator
        ] = None,
        left_operands: typing___Optional[typing___Iterable[global___Operand]] = None,
        right_operands: typing___Optional[typing___Iterable[global___Operand]] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MatchingFunction: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MatchingFunction: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["function_string", b"function_string"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "function_string",
            b"function_string",
            "left_operands",
            b"left_operands",
            "operator",
            b"operator",
            "right_operands",
            b"right_operands",
        ],
    ) -> None: ...

global___MatchingFunction = MatchingFunction

class Operand(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ConstantOperand(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def string_value(self) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def long_value(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def boolean_value(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
        @property
        def double_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
        def __init__(
            self,
            *,
            string_value: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            long_value: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            boolean_value: typing___Optional[
                google___protobuf___wrappers_pb2___BoolValue
            ] = None,
            double_value: typing___Optional[
                google___protobuf___wrappers_pb2___DoubleValue
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Operand.ConstantOperand: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> Operand.ConstantOperand: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "boolean_value",
                b"boolean_value",
                "constant_operand_value",
                b"constant_operand_value",
                "double_value",
                b"double_value",
                "long_value",
                b"long_value",
                "string_value",
                b"string_value",
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "boolean_value",
                b"boolean_value",
                "constant_operand_value",
                b"constant_operand_value",
                "double_value",
                b"double_value",
                "long_value",
                b"long_value",
                "string_value",
                b"string_value",
            ],
        ) -> None: ...
        def WhichOneof(
            self,
            oneof_group: typing_extensions___Literal[
                "constant_operand_value", b"constant_operand_value"
            ],
        ) -> typing_extensions___Literal[
            "string_value", "long_value", "boolean_value", "double_value"
        ]: ...
    global___ConstantOperand = ConstantOperand
    class FeedAttributeOperand(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def feed_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def feed_attribute_id(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            feed_id: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            feed_attribute_id: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Operand.FeedAttributeOperand: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> Operand.FeedAttributeOperand: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "feed_attribute_id", b"feed_attribute_id", "feed_id", b"feed_id"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "feed_attribute_id", b"feed_attribute_id", "feed_id", b"feed_id"
            ],
        ) -> None: ...
    global___FeedAttributeOperand = FeedAttributeOperand
    class FunctionOperand(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def matching_function(self) -> global___MatchingFunction: ...
        def __init__(
            self,
            *,
            matching_function: typing___Optional[global___MatchingFunction] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Operand.FunctionOperand: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> Operand.FunctionOperand: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "matching_function", b"matching_function"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "matching_function", b"matching_function"
            ],
        ) -> None: ...
    global___FunctionOperand = FunctionOperand
    class RequestContextOperand(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        context_type = (
            ...
        )  # type: google___ads___googleads___v2___enums___matching_function_context_type_pb2___MatchingFunctionContextTypeEnum.MatchingFunctionContextType
        def __init__(
            self,
            *,
            context_type: typing___Optional[
                google___ads___googleads___v2___enums___matching_function_context_type_pb2___MatchingFunctionContextTypeEnum.MatchingFunctionContextType
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> Operand.RequestContextOperand: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> Operand.RequestContextOperand: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal["context_type", b"context_type"],
        ) -> None: ...
    global___RequestContextOperand = RequestContextOperand
    @property
    def constant_operand(self) -> global___Operand.ConstantOperand: ...
    @property
    def feed_attribute_operand(self) -> global___Operand.FeedAttributeOperand: ...
    @property
    def function_operand(self) -> global___Operand.FunctionOperand: ...
    @property
    def request_context_operand(self) -> global___Operand.RequestContextOperand: ...
    def __init__(
        self,
        *,
        constant_operand: typing___Optional[global___Operand.ConstantOperand] = None,
        feed_attribute_operand: typing___Optional[
            global___Operand.FeedAttributeOperand
        ] = None,
        function_operand: typing___Optional[global___Operand.FunctionOperand] = None,
        request_context_operand: typing___Optional[
            global___Operand.RequestContextOperand
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Operand: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Operand: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "constant_operand",
            b"constant_operand",
            "feed_attribute_operand",
            b"feed_attribute_operand",
            "function_argument_operand",
            b"function_argument_operand",
            "function_operand",
            b"function_operand",
            "request_context_operand",
            b"request_context_operand",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "constant_operand",
            b"constant_operand",
            "feed_attribute_operand",
            b"feed_attribute_operand",
            "function_argument_operand",
            b"function_argument_operand",
            "function_operand",
            b"function_operand",
            "request_context_operand",
            b"request_context_operand",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "function_argument_operand", b"function_argument_operand"
        ],
    ) -> typing_extensions___Literal[
        "constant_operand",
        "feed_attribute_operand",
        "function_operand",
        "request_context_operand",
    ]: ...

global___Operand = Operand
