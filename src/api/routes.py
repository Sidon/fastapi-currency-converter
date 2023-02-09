from fastapi import APIRouter
from src.api.endpoints import convert_endpoint
from ..models import CurrencyConversion

api_router = APIRouter()


# @api_router.get("/convert", response_model=Any, tags=["currency"])
@api_router.get("/convert", tags=["currency"])
async def convert(conversion: CurrencyConversion):
    return convert_endpoint(
        conversion.from_currency,
        conversion.to_currency,
        conversion.amount
    )
