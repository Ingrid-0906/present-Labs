import yfinance as yf

def extrair_dados_yahoo_finance(acao):
    dados = yf.download(acao, start="2023-01-01", end="2023-12-01")
    return dados
