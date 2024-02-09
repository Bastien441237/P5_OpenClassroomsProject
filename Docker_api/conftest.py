import pytest
from Moreno_Bastien_5_code_API_022024 import create_app

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client
