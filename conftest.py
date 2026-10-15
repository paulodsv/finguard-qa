import pytest
import httpx


@pytest.fixture
def api_client():
    with httpx.Client(
        base_url="http://localhost:8000",
        timeout=10.0,
    ) as client:
        yield client