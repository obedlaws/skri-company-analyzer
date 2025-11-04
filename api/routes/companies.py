from fastapi import APIRouter
from services import parsers

companies = APIRouter(
    prefix="/companies",
    tags=["companies"]
)

@companies.get("/{company_ticker}")
async def get_company_analysis(company_ticker: str):
    print(company_ticker)
    parsers.parse_company_info(company_ticker)
    return {"company": company_ticker}