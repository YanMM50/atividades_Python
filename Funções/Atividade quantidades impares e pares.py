"""
Crie um programa que leia 6 números e informe por meio de uma função 
- Quantos númros são pares;
-Quantos números são ímpares.

"""

import os
os.system("cls || clear")


def impar_par():
    contador_par = 0
    contador_impar = 0

    for i in range(6):
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
    print(f"Ímpares: {contador_impar}")
    print(f"Pares: {contador_par}")
   

impar_par()