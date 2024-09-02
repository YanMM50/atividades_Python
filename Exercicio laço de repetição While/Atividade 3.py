""" 
Escreva um programa que multiplique um número inicial por um fator dado pelo usuário até que o produto exceda 100. Exiba o produto final e o número de multiplicações realizadas.

"""
import os 
os.system("cls || clear")

contador = 0
NUMERO_INICIAL = 2

while True:
    nota = int(input("Digite um número: "))
    contador += 1
    produto = NUMERO_INICIAL * nota

    if produto > 100:
        print(f"Produto = {produto}")
        print(f"Multiplicações realizadas: {contador}")
        break
