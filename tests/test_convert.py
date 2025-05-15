import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import get_settings


settings = get_settings()
client = TestClient(app)

@pytest.mark.asyncio
async def test_convert_currency_success():
    response = client.post("/api/v1/convert", params={
        "from_currency": "INR",
        "to_currency": "NPR",
        "amount": 10
    })
    print(response.status_code)
    print(response.json())    
    assert response.status_code == 200
    data = response.json()
    assert data["from_currency"] == "INR"
    assert data["to_currency"] == "NPR"
    assert data["amount"] == 10
    assert "converted_amount" in data
    assert isinstance(data["converted_amount"], float)


@pytest.mark.asyncio
async def test_convert_currency_invalid_code():
    response = client.post("/api/v1/convert", params={
        "from_currency": "XXX",  # Invalid code
        "to_currency": "NPR",
        "amount": 10
    })
    assert response.status_code == 405  # API should handle it gracefully

