from app.presentation.protocols import Controller, HttpRequest, HttpResponse


class LogControllerDecorator(Controller):
    def __init__(self, controller: Controller):
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        http_response = self._controller.handle(http_request)
        return http_response
