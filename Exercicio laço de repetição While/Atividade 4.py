"""
Crie um programa que ajude um usuário a controlar seus gastos mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve exibir o total gasto e o valor  excedente.

"""
import os
os.system("cls || clear")

TOTAL_DE_GASTOS = 1000

soma =0

while True:
    gastos = int(input("Digite seu gastos de hojé: "))
    soma += gastos

    if soma > TOTAL_DE_GASTOS:
        print("Limite atingido!")
        print(f"Total de gastos; {soma}")
        break
