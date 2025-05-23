
import pandas as pd
#import numpy as np
import requests
import time

import yfinance as yf # para dados históricos
import fundamentus as fd #type: ignore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def importa_historico(ticker, start_date, end_date ):
    """
    Importa dados históricos de cotação da biblioteca Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    print(f'Setor: {yf.Sector(ticker).value}')
    print(f'Indústria: {yf.Industry(ticker).value}')
    print(f'Mercado: {yf.Market(ticker).value}')
    return data

def importa_fundamentos_acoes():
    '''
    Importa dados fundamentalistas de ações do ticker utilizando o pacote fundamentus.
    '''
    todos_dados_acoes = fd.get_resultado()
    todos_dados_acoes.to_json('data_bronze/dados_fundamentalistas_acoes.json')


def importa_dados_fiis():
    '''
    Importa dados fundamentalistas de FIIs do ticker utilizando o pacote fundamentus.
    '''
    url = 'https://www.fundsexplorer.com.br/ranking'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Aguarda o carregamento da tabela via JS

    html = driver.page_source
    driver.quit()
    tables = pd.read_html(html)
    todos_dados_fiis = tables[0]
    print(todos_dados_fiis.head())
    todos_dados_fiis.to_json('data_bronze/dados_fundamentalistas_fiis.json', orient='records', force_ascii=False)




if __name__ == "__main__":
    #historico = importa_historico("AAPL", "2025-05-01", "2025-05-21")
    #print(historico)
    importa_fundamentos_acoes()
    importa_dados_fiis()
    
