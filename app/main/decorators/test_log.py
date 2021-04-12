from dataclasses import dataclass
from http import HTTPStatus
from unittest import TestCase, mock

import pytest

from app.data.protocols.log_error_repository import LogErrorRepository
from app.main.decorators.log import LogControllerDecorator
from app.presentation.helpers.http_helpers import server_error
from app.presentation.protocols import Controller, HttpRequest, HttpResponse


def make_controller() -> Controller:
    class ControllerStub(Controller):
        def handle(self, http_request: HttpRequest) -> HttpResponse:
            return HttpResponse(status=HTTPStatus.NOT_FOUND, body=None)

    return ControllerStub()


def make_log_error_repository() -> LogErrorRepository:
    class LogErrorRepositoryStub(LogErrorRepository):
        def log(self, stack: str) -> None:
            pass

    return LogErrorRepositoryStub()


@dataclass
class SutTypes:
    controller_stub: Controller
    sut: LogControllerDecorator
    log_error_repository_stub: LogErrorRepository


def make_sut() -> SutTypes:
    controller_stub = make_controller()
    log_error_repository_stub = make_log_error_repository()
    sut = LogControllerDecorator(controller_stub, log_error_repository_stub)

    return SutTypes(
        controller_stub=controller_stub,
        sut=sut,
        log_error_repository_stub=log_error_repository_stub,
    )


@pytest.mark.unit
class LogControllerDecoratorTests(TestCase):
    """
    LogControllerDecorator
    """

    @staticmethod
    def test_call_controller_handle():
        """
        Should call controller handle
        """
        sut_types = make_sut()
        sut, controller_stub = sut_types.sut, sut_types.controller_stub

        http_request = HttpRequest()

        with mock.patch.object(controller_stub, "handle") as handle_spy:
            sut.handle(http_request)
            handle_spy.assert_called_once_with(http_request)

    def test_return_the_same_controller_result(self):
        """
        Should return the same controller result
        """
        sut = make_sut().sut
        http_request = HttpRequest()
        http_response = sut.handle(http_request)

        self.assertEqual(
            http_response, HttpResponse(status=HTTPStatus.NOT_FOUND, body=None)
        )

    @staticmethod
    def test_call_log_error_repository_with_correct_error_if_server_error():
        """
        Should call LogErrorRepository with correct error if controller \
returns a server error
        """
        sut_types = make_sut()
        sut, controller_stub, log_error_repository_stub = (
            sut_types.sut,
            sut_types.controller_stub,
            sut_types.log_error_repository_stub,
        )
        stack = "any_stack"

        http_request = HttpRequest()

        with mock.patch.object(
            controller_stub, "handle", return_value=server_error(stack)
        ), mock.patch.object(log_error_repository_stub, "log") as log_spy:
            sut.handle(http_request)
            log_spy.assert_called_once_with(stack)
