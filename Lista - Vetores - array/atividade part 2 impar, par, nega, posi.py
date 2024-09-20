"""
Altere o algoritmo que acabou de criar e faça com que o usuário insira números inteiros até quie seja inserido o número 0

1. A quantidade de números positivos que são pares;
2. A quantidade de números ímpares;
3. A quantidade de números negativos;
4. A quantidade de números inseridos.

"""

import os
os.system("cls || clear")
import random


lista_numero = []
contador = 0

while True:
    numero = int(input(f"Digite um número: "))
    lista_numero.append(numero)
    contador += 1
    if numero == 0:
        break


def verificando_par_impar():
    lista_positivos_par = []
    lista_impar = []

    for numero in lista_numero:
        if numero % 2 == 0 and numero > 0:
            lista_positivos_par.append(numero)

        elif numero % 2 != 0 and numero > 0:
            lista_impar.append(numero)

    return lista_positivos_par, lista_impar

def verificando_positivo_negativo():
    lista_positivo = []
    lista_negativo = []

    for numero in lista_numero:
        if numero > 0:
            lista_positivo.append(numero)
        elif numero < 0: 
            lista_negativo.append(numero)

    return lista_positivo, lista_negativo


lista_atualizada_par, lista_atualizada_impar = verificando_par_impar()
lista_atualizada_positivo, lista_atualizada_negativo = verificando_positivo_negativo()


print("\n=== Exibindo números inseridos ===")
print(f"Números inseridos: {contador}")

print("\n=== Exibindo números positivos pares ===")
for i, numero2 in enumerate(lista_atualizada_par):
    print(f"{i+1}º {numero2}")
print(f"Números pares inseridos: {len(lista_atualizada_par)}")

print("\n=== Exibindo números ímpares ===")
for i, numero3 in enumerate(lista_atualizada_impar):
    print(f"{i+1}º {numero3}")
print(f"Números ímpares inseridos: {len(lista_atualizada_impar)}")

print("\n=== Exibindo números negativos ===")
for i, numero5 in enumerate(lista_atualizada_negativo):
    print(f"{i+1}º {numero5}")
print(f"Números negativos inseridos: {len(lista_atualizada_negativo)}")


