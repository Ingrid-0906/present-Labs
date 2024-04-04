import yfinance as yf

def extrair_dados_yahoo_finance(acao):
    """
    Extrai dados históricos de uma a��o da Yahoo Finance.

    Par�metros:
    acao (str): O ticker da a��o a ser consultada.

    Retorna:
    DataFrame: Um DataFrame contendo os dados hist�ricos da a��o.
    """
    dados = yf.download(acao, start="2023-01-01", end="2023-12-01")
    return dados
