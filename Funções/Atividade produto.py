"""
Fazer um programa que solicita o preço de um produto e inflaciona esse preço em 10%, se ele for menor que 100 e em 20% se ele for maior ou igual a 100

Ultilize uma função para obter o resultado solicitado

"""

import os
os.system("cls || clear")

preco = float(input("Digite um preço: R$"))


def produto(n1):
    if n1 < 100:
        valor = n1 + (n1 * 0.1)
        # valor = n1 * 1.1
    else:
        valor = n1 + (n1 * 0.2)
    return valor


valor = produto(preco)
print(f"Valor com inflação: R$:{valor:.2f}")

