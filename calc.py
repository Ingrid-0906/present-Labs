import yfinance as yf

def extrair_dados_yahoo_finance(acao):
    """
    Extrai dados históricos de uma ação da Yahoo Finance.

    Parâmetros:
    acao (str): O ticker da ação a ser consultada.

    Retorna:
    DataFrame: Um DataFrame contendo os dados históricos da ação.
    """
    dados = yf.download(acao, start="2023-01-01", end="2023-12-01")
    return dados
