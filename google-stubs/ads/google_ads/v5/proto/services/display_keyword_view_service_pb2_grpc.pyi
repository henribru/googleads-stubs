from typing import Any, Optional

class DisplayKeywordViewServiceStub:
    GetDisplayKeywordView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DisplayKeywordViewServiceServicer:
    def GetDisplayKeywordView(self, request: Any, context: Any) -> None: ...

def add_DisplayKeywordViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class DisplayKeywordViewService:
    @staticmethod
    def GetDisplayKeywordView(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
