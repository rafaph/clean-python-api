from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class HttpResponse:
    status: int
    body: Any


@dataclass
class HttpRequest:
    body: Optional[Any] = None
