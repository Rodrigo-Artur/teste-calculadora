"""Exemplo didatico: calcula o valor de uma compra com desconto."""


def calcular_total(preco, quantidade, desconto=0):
    if preco < 0:
        raise ValueError("Preco nao pode ser negativo")
    if quantidade < 0:
        raise ValueError("Quantidade nao pode ser negativa")
    if not 0 <= desconto <= 100:
        raise ValueError("Desconto precisa estar entre 0 e 100")
    return round(preco * quantidade * (1 - desconto / 100), 2)
