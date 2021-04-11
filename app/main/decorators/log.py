from http import HTTPStatus

from app.presentation.protocols import Controller, HttpRequest, HttpResponse


class LogControllerDecorator(Controller):
    def __init__(self, controller: Controller):
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        self._controller.handle(http_request)
        return HttpResponse(status=HTTPStatus.NOT_FOUND, body=None)
