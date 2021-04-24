from http import HTTPStatus

from app.data.protocols.log_error_repository import LogErrorRepository
from app.presentation.protocols import Controller, HttpRequest, HttpResponse


class LogControllerDecorator(Controller):
    def __init__(
        self, controller: Controller, log_error_repository: LogErrorRepository
    ):
        self._controller = controller
        self._log_error_repository = log_error_repository

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        http_response = self._controller.handle(http_request)
        if http_response.status == HTTPStatus.INTERNAL_SERVER_ERROR:
            self._log_error_repository.log_error(http_response.body.stack)
        return http_response
