def investimento_juros_compostos(valor_inicial, taxa_juros, anos):
    meses = anos * 12
    taxa_mensal = taxa_juros / 100
    valor_final = valor_inicial * (1 + taxa_mensal) ** meses
    return valor_final

# Exemplo de uso
investimento = investimento_juros_compostos(1000, 0.5, 5)
print(f"Valor do investimento após 5 anos: R${investimento:.2f}")
