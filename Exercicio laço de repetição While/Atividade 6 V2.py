"""
Crie um programa que ajude um estudante a calcular a média de suas notas. O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo. O programa deve calcular e exibir a média das notas inseridas.

"""

import os
os.system("cls || clear")


soma = 0
iteracoes = 0

while True:
    nota = float(input("\nDigite a nota (ou um valor negativo para encerrar): "))

    if nota < 0:
        if iteracoes == 0:
            print("Nenhuma nota válida foi inserida.")
        else: 
            media = soma / iteracoes
            print(f"Média final : {media: .2f}")
            break

    soma += nota
    iteracoes += 1
    
            

