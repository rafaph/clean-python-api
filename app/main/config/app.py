from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .middlewares import setup_middlewares
from .routes import setup_routes


def make_app():
    app = FastAPI(debug=True, default_response_class=ORJSONResponse)

    setup_middlewares(app)
    setup_routes(app)

    return app
