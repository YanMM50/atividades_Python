"""
Escreva um programa que permita ler 3 notas de um aluno, usando laço de repetição e informe por meio de uma função a média;

"""

import os
os.system("cls || clear")

soma = 0
contador = 0

for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1


def media(n1, contador):
    media = n1 / contador
    return media

soma_media = media(soma, contador)


print(f"Média: {soma_media}")
