from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

middleware_class = BaseHTTPMiddleware


async def _dispatch(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


params = {"dispatch": _dispatch}
