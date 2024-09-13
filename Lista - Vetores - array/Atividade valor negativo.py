"""
Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números, caso seja infromado um valor negativo, atribua o valor 0.

-Liste os valores do vetor

"""

import os 
os.system("cls || clear")
QUANTIDADE = 5
lista_numeros = []

for i in range(QUANTIDADE):
    num = float(input(f"Digite o {i+1}ª número: "))
    lista_numeros.append(num)


def verificando_negativo(negativo):

    lista_negativo = []
    

    for numero in negativo:
        if numero < 0 :
            numero = 0
            lista_negativo.append(numero)
        else:
            lista_negativo.append(numero)

    return lista_negativo

negativo = verificando_negativo(lista_numeros)


for i, numero in enumerate (negativo):
    print(f"{i+1}ª número: {numero}")




