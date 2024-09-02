"""
Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).

"""
import os 
os.system("cls || clear")

import time
num_linhas = 4
num_colunas = 6

#Laço para cada linha 
for i in range(num_linhas):
    #Laço para cada coluna dentro da linha
    for j in range(num_colunas):
        print("*", end="")
    print()
    time.sleep(1)

