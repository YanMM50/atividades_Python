"""
Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while. O programa deve parar quando o usuário inserir 0 ou um número positivo. Mostre a quantidade de números negativos.

"""

import os 
os.system("cls || clear")

print("Apenas insira números negativos.")

contador = 0

while True:
    numero = int(input("Digite um número: "))
    if numero <= -1:
        contador += 1
    else:
        break


print(f"Quantidades de números negativos: {contador}")
