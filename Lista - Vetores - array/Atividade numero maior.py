"""
Crie um programa que leia 5 números, armazenando em um vetor e informe qual é o menor número e o maior.

Mostre os números informados pelo usuário.

"""

import os
os.system("cls || clear")

numeros_lista = []
QUANTIDADE_NUMEROS = 5


for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}ª numero: "))
    numeros_lista.append(numero)


maior_numero = max(numeros_lista)
menor_numero = min(numeros_lista)

print("\n=== Exibindo números ===")
for i, numero in enumerate(numeros_lista):
    print(f"{i+1}ª: {numero}")

print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")