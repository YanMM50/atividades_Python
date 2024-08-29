"""
Escreva um algoritmo que solicite duas notas para um aluno.
caso seja menor que 0 ou maior que 10, mostre a pegunta novamente.
Calcule e mostre a média aritmética do aluno.

"""
import os
os.system("cls || clear")

QUANTIDADE_DE_NOTA = 2 #constante
soma = 0

for i in range(QUANTIDADE_DE_NOTA):   
    while True:
        nota = float(input(f"Digite {i+1}ª nota: "))

        if nota >= 0 and nota <= 10:
            break
        else:
            print("\nA nota deve ser maior ou igual 0 e menor e iqual a 10.")
    soma += nota


media = soma / QUANTIDADE_DE_NOTA

print(f"Média: {media}")

