"""
Crie um programa que leia 3 notas, armazenando em um vator e mostre as notas informadas.

"""

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    lista_notas.append(nota)

for i, nota in enumerate(lista_notas):
    print(f"Sua {i+1}ª {nota}")