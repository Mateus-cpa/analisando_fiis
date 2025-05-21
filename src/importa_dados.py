import requests as req
import pandas as pd
import numpy as np

import yfinance as yf

def import_data(stock, start_date, end_date):
    """
    Import stock data from Yahoo Finance.
    """
    data = yf.download(stock, start=start_date, end=end_date)
    print(f'Setor: {yf.Sector(stock)}')
    print(f'Indústria: {yf.Industry(stock)}')
    print(f'Mercado: {yf.Market(stock)}')
    return data

if __name__ == "__main__":
    data = import_data("AAPL", "2025-05-01", "2025-05-21")
    print(data)