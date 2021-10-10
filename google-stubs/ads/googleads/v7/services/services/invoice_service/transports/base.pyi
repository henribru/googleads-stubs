import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.services.types import invoice_service

class InvoiceServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def list_invoices(
        self,
    ) -> typing.Callable[
        [invoice_service.ListInvoicesRequest], invoice_service.ListInvoicesResponse
    ]: ...
