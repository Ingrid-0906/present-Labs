import yfinance as yf

def extrair_dados_yahoo_finance(acao):
    dados = yf.download(acao, start="2021-01-01", end="2021-12-31")
    return dados

