"""
Crie
um programa que, utilizando um laço `for`, calcule a soma dos números de 1 a 5
e mostre o resultado.

"""

import os
os.system("cls || clear")

import time

soma = 0

for i in range(1,6):
    print(f"{i}")
    time.sleep(1)
    soma += i


print(f"Soma: {soma}")
