"""
Crie um programa que leia 3 notas, armazenando em um vetor e calcule a média aritmética.

"""

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3    
lista_notas = []


for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas) #Sum soma as notas da lista.
media = soma / QUANTIDADE_NOTAS

print("\n=== Exibindo notas ===")
for i ,nota in enumerate(lista_notas):
    print(f"Sua {i+1}ª nota: {nota} ")


print("\n=== Exibindo Média ===")
print(f"Média: {media}")