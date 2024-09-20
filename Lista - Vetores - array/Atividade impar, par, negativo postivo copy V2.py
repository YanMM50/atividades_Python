"""
Crie um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1 - quantidade de números pares e ímpares;
2 - a quantidade de números positivos e negativos;
3 - quantidade de números inseridos.

"""

import os
os.system("cls || clear")
import random

QUANTIDADE_REPETICOES = 5
lista_numero = []
contador = 0

for i in range(QUANTIDADE_REPETICOES):
    numero = random.randint(-10,10)
    lista_numero.append(numero)
    contador += 1

def verificando_par_impar():
    lista_par = []
    lista_impar = []

    for numero in lista_numero:
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)

    return lista_par, lista_impar

def verificando_positivo_negativo():
    lista_positivo = []
    lista_negativo = []

    for numero in lista_numero:
        if numero > 0:
            lista_positivo.append(numero)
        else:
            lista_negativo.append(numero)

    return lista_positivo, lista_negativo


lista_atualizada_par, lista_atualizada_impar = verificando_par_impar()
lista_atualizada_positivo, lista_atualizada_negativo = verificando_positivo_negativo()


print("=== Exibindo números inseridos ===")
for i, numero in enumerate(lista_numero):
    print(f"{i+1}º {numero}")
print(f"Números inseridos: {contador}")

print("=== Exibindo números pares ===")
for i, numero2 in enumerate(lista_atualizada_par):
    print(f"{i+1}º {numero2}")
print(f"Números pares inseridos: {len(lista_atualizada_par)}")

print("=== Exibindo números ímpares ===")
for i, numero3 in enumerate(lista_atualizada_impar):
    print(f"{i+1}º {numero3}")
print(f"Números ímpares inseridos: {len(lista_atualizada_impar)}")

print("=== Exibindo números positivos ===")
for i, numero4 in enumerate(lista_atualizada_positivo):
    print(f"{i+1}º {numero4}")
print(f"Números positivos inseridos: {len(lista_atualizada_positivo)}")

print("=== Exibindo números negativos ===")
for i, numero5 in enumerate(lista_atualizada_negativo):
    print(f"{i+1}º {numero5}")
print(f"Números negativos inseridos: {len(lista_atualizada_negativo)}")


