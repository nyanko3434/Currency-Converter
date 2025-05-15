import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import get_settings

settings = get_settings()
client = TestClient(app)

@pytest.mark.asyncio
async def test_list_currencies_success():
    response = client.get("/api/v1/currencies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "NPR" in data
    assert data["NPR"] == "Nepalese Rupee"