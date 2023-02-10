import os

from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from src.api.utils import currency_conversion
from ..config import URL_4217

api_router = APIRouter()
current_dir = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(current_dir, "../templates"))


@api_router.get("/", response_class=HTMLResponse, include_in_schema=False)
def index(request: Request, ):
    return templates.TemplateResponse("index.html", context={"request": request})


CURRENCY_CODES = ['USD', 'BRL', 'EUR', 'BTC', 'ETH']
TEXT_FROM = f'Moeda da qual deseja converter, por exemplo, USD. [Symbolos ISO]({URL_4217})'
TEXT_TO = f'Moeda para a qual deseja converter, por exemplo, BTC. [Symbolos ISO]({URL_4217})'


@api_router.get("/convert", tags=["currency"])
async def convert(
        from_currency: str = Query(..., description=TEXT_FROM, example="USD", values=CURRENCY_CODES),
        to_currency: str = Query(..., description=TEXT_TO, example="BTC", values=CURRENCY_CODES),
        amount: float = Query(..., description="Valor a ser convertido.")
):
    return currency_conversion(from_currency, to_currency, amount)


@api_router.post("/submit_form", include_in_schema=False)
async def submit_form(request: Request):
    # get submitted form data
    form_data = await request.form()

    # process submitted form data
    from_currency = form_data.get('from')
    to_currency = form_data.get('to')
    amount = form_data.get('amount')

    context = {"result": "Dados incorretos", "request": request}
    if from_currency.isalpha() and to_currency.isalpha() and amount.isnumeric():
        result_data = currency_conversion(from_currency, to_currency, amount)
        context = {"result": result_data, "request": request}

    response = templates.TemplateResponse("index.html", context=context)
    return response
