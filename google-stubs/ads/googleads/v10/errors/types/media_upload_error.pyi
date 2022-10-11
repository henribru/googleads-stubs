import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class MediaUploadErrorEnum(proto.Message):
    class MediaUploadError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FILE_TOO_BIG: int
        UNPARSEABLE_IMAGE: int
        ANIMATED_IMAGE_NOT_ALLOWED: int
        FORMAT_NOT_ALLOWED: int
        EXTERNAL_URL_NOT_ALLOWED: int
        INVALID_URL_REFERENCE: int
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: int
        ANIMATED_VISUAL_EFFECT: int
        ANIMATION_TOO_LONG: int
        ASPECT_RATIO_NOT_ALLOWED: int
        AUDIO_NOT_ALLOWED_IN_MEDIA_BUNDLE: int
        CMYK_JPEG_NOT_ALLOWED: int
        FLASH_NOT_ALLOWED: int
        FRAME_RATE_TOO_HIGH: int
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: int
        IMAGE_CONSTRAINTS_VIOLATED: int
        INVALID_MEDIA_BUNDLE: int
        INVALID_MEDIA_BUNDLE_ENTRY: int
        INVALID_MIME_TYPE: int
        INVALID_PATH: int
        LAYOUT_PROBLEM: int
        MALFORMED_URL: int
        MEDIA_BUNDLE_NOT_ALLOWED: int
        MEDIA_BUNDLE_NOT_COMPATIBLE_TO_PRODUCT_TYPE: int
        MEDIA_BUNDLE_REJECTED_BY_MULTIPLE_ASSET_SPECS: int
        TOO_MANY_FILES_IN_MEDIA_BUNDLE: int
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: int
        UNSUPPORTED_HTML5_FEATURE: int
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: int
        VIDEO_FILE_NAME_TOO_LONG: int
        VIDEO_MULTIPLE_FILES_WITH_SAME_NAME: int
        VIDEO_NOT_ALLOWED_IN_MEDIA_BUNDLE: int
        CANNOT_UPLOAD_MEDIA_TYPE_THROUGH_API: int
        DIMENSIONS_NOT_ALLOWED: int