from typing import Any
from unittest import TestCase

import pytest
from fastapi import Body
from fastapi.testclient import TestClient

from app.main.config import app


@pytest.mark.integration
class BodyParserMiddlewareTests(TestCase):
    """
    Body Parser Middleware
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_parse_body_as_json(self):
        """
        Should parse body as json
        """

        def dispatch(data: Any = Body(...)):
            return data

        app.post("/test_body_parser")(dispatch)
        json_data = {"name": "My Name"}
        response = self.client.post("/test_body_parser", json=json_data)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), json_data)
