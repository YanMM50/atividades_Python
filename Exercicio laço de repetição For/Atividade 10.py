"""
Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`.

"""

import os
os.system("cls || clear")

import time

soma = 0

for i in range(1,10,2):
    print(f"Número impares: {i}")        
    soma += i 
    time.sleep(1)

print(f"Soma: {soma}")
