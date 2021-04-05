from unittest import TestCase

import pytest
from fastapi.testclient import TestClient

from app.main.config import make_app


@pytest.mark.integration
class CorsMiddlewareTests(TestCase):
    """
    CORS Middleware
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = make_app()
        cls.client = TestClient(cls.app)

    def test_enable_cors(self):
        """
        Should enable CORS
        """
        self.app.get("/test_cors")(lambda: {})

        response = self.client.get("/test_cors")
        self.assertEqual(response.status_code, 200)

        self.assertIn("access-control-allow-origin", response.headers)
        self.assertEqual(response.headers["access-control-allow-origin"], "*")

        self.assertIn("access-control-allow-methods", response.headers)
        self.assertEqual(response.headers["access-control-allow-methods"], "*")

        self.assertIn("access-control-allow-headers", response.headers)
        self.assertEqual(response.headers["access-control-allow-headers"], "*")
