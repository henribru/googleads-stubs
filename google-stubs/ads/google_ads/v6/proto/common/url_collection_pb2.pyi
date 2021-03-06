"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UrlCollection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    URL_COLLECTION_ID_FIELD_NUMBER: builtins.int
    FINAL_URLS_FIELD_NUMBER: builtins.int
    FINAL_MOBILE_URLS_FIELD_NUMBER: builtins.int
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: builtins.int
    url_collection_id: typing.Text = ...
    final_urls: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    final_mobile_urls: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    tracking_url_template: typing.Text = ...
    def __init__(
        self,
        *,
        url_collection_id: typing.Text = ...,
        final_urls: typing.Optional[typing.Iterable[typing.Text]] = ...,
        final_mobile_urls: typing.Optional[typing.Iterable[typing.Text]] = ...,
        tracking_url_template: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_tracking_url_template",
            b"_tracking_url_template",
            "_url_collection_id",
            b"_url_collection_id",
            "tracking_url_template",
            b"tracking_url_template",
            "url_collection_id",
            b"url_collection_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_tracking_url_template",
            b"_tracking_url_template",
            "_url_collection_id",
            b"_url_collection_id",
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_urls",
            b"final_urls",
            "tracking_url_template",
            b"tracking_url_template",
            "url_collection_id",
            b"url_collection_id",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_tracking_url_template", b"_tracking_url_template"
        ],
    ) -> typing_extensions.Literal["tracking_url_template"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_url_collection_id", b"_url_collection_id"
        ],
    ) -> typing_extensions.Literal["url_collection_id"]: ...

global___UrlCollection = UrlCollection
