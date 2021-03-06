"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ExpandedLandingPageView(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    EXPANDED_FINAL_URL_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    expanded_final_url: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        expanded_final_url: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_expanded_final_url",
            b"_expanded_final_url",
            "expanded_final_url",
            b"expanded_final_url",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_expanded_final_url",
            b"_expanded_final_url",
            "expanded_final_url",
            b"expanded_final_url",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_expanded_final_url", b"_expanded_final_url"
        ],
    ) -> typing_extensions.Literal["expanded_final_url"]: ...

global___ExpandedLandingPageView = ExpandedLandingPageView
