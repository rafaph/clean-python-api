import abc
from .http import HttpRequest, HttpResponse


class Controller(abc.ABC):
    @abc.abstractmethod
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        raise NotImplementedError("Every controller must implement a handle.")
