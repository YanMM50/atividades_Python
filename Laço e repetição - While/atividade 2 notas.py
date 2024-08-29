"""
Escreva um algoritmo que solicite duas notas para um aluno.
caso seja menor que 0 ou maior que 10, mostre a pegunta novamente.
Calcule e mostre a média aritmética do aluno.

"""
import os
os.system("cls || clear")


while True:
    nota_um = float(input("Digite uma nota: "))
    nota_dois = float(input("Digite a segunda nota: "))

    if nota_um < 0 or nota_um > 10: #poderia usar so o if colocando assim: (nota_um < 0 or nota_um > 10) or ... nota_doi...
        print("\nA nota um deve ser maior ou igual 0 e menor e iqual a 10.")
    elif nota_dois < 0 or nota_dois > 10:
        print("\nA nota dois deve ser maior ou igual 0 e menor e iqual a 10.")
    else:
        break


soma = nota_um + nota_dois
media = soma / 2

print(f"Média: {media}")

