from fastapi import Request, Response

from app.presentation.protocols import Controller, HttpRequest


def adapt_route(controller: Controller):
    async def handler(request: Request, response: Response):
        http_request = HttpRequest(body=await request.json())
        http_response = controller.handle(http_request)
        response.status_code = http_response.status
        return http_response.body

    return handler
