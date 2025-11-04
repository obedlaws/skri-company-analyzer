from typing import Dict, Any
import yfinance as yf

import pandas as pd

def parse_company_info(company_tikcer: str) -> Dict[str, Any]:
    lower_company_ticker = company_tikcer.capitalize()
    # print(lower_company_ticker)
    stock = yf.Ticker(lower_company_ticker)
    cash_flow = stock.cash_flow
    balance_sheet = stock.balance_sheet
    