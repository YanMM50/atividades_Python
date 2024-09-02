"""
Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).

"""
import os 
os.system("cls || clear")

import time
#laço externo para linhas
for externo in range(4): # Para cada linha 0 a 3
    #laço interno para colunas
    for interno in range(6): # para cada coluna 0 a 5 
        print("*", end="  ") #imprime cada "*" sem quebrar a linha
    print()     # apos o laço interno imprime uma nova linha

