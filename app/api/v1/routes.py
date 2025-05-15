from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import ConvertRequest, ConvertResponse
from app.core.currency import get_exchange_amount, get_currency_list

router = APIRouter()

@router.post("/convert", response_model=ConvertResponse)
async def convert_currency(request: ConvertRequest = Depends(ConvertRequest)):
    converted_amount = await get_exchange_amount(
        from_currency=request.from_currency,
        to_currency=request.to_currency,
        amount=request.amount
    )
    if converted_amount is None:
        raise HTTPException(status_code=405, detail="Conversion failed")
    return ConvertResponse(
        from_currency=request.from_currency,
        to_currency=request.to_currency,
        amount=request.amount,
        rate=converted_amount / request.amount,
        converted_amount=converted_amount
    )

@router.get("/currencies")
async def list_currencies():
    try:
        currencies = await get_currency_list()
        return currencies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e