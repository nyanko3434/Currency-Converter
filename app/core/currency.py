import httpx
from app.core.config import get_settings

settings = get_settings()


async def get_exchange_amount(from_currency: str, to_currency: str, amount: float) -> float:
    url = f"{settings.API_BASE_URL}/convert"
    params = {
        "access_key": settings.EXCHANGE_RATE_API_KEY,
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    if data.get("success") and "result" in data:
        return data["result"]
    else:
        return None


async def get_currency_list() -> dict:
    url = f"{settings.API_BASE_URL}/list"
    params = {
        "access_key": settings.EXCHANGE_RATE_API_KEY
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    if data.get("success") and "currencies" in data:
        return data["currencies"]
    else:
        raise ValueError(f"Failed to fetch currency list: {data}")