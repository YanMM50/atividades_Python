"""
Crie uma função que receba um número e mostre uma mensagem informando se o número é par ou ímpar.

"""
import os
os.system("cls || clear")


numero = int(input("Digite um número: "))


def impar_par(n1:int):
    # impares = 0
    # pares = 0
    if n1 % 2 == 0:
        # Pares += 1
        print("Par")
    else:
        # impares += 1
        print("ímpares")
    # return pares, impares

impar_par(numero)






