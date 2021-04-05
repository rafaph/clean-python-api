from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .middlewares import setup_middlewares

app = FastAPI(debug=True, default_response_class=ORJSONResponse)

setup_middlewares(app)
