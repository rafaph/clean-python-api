from http import HTTPStatus

from fastapi import Request, Response

from app.presentation.protocols import Controller, HttpRequest


def adapt_route(controller: Controller):
    async def handler(request: Request, response: Response):
        http_request = HttpRequest(body=await request.json())
        http_response = controller.handle(http_request)
        response.status_code = http_response.status

        if http_response.status == HTTPStatus.OK:
            return http_response.body

        error = http_response.body
        return {"error": str(error)}

    return handler
