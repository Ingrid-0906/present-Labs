import yfinance as yf

def extrair_dados_yahoo_finance(acao):
    dados = yf.download(acao, start="2021-01-01", end="2021-12-31")
    return dados

def extrair_dados_apple_e_google():
    dados_apple = extrair_dados_yahoo_finance("AAPL")
    dados_google = extrair_dados_yahoo_finance("GOOGL")
    return dados_apple, dados_google
