"""
Escreva um programa que permita ler 2 notas de um aluno e:

-informe por meio de uma função a média;

-informe por meio de uma função se a média for maior ou igual a 7, o aluno estará aprovado, caso contrário, estará reporvado.



"""

import os
os.system("cls || clear")

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma segunda nota: "))


def media(n1, n2):
    media = (n1 + n2) / 2
    return media


def aprovado_ou_reprovado(media):
    if media >= 7:
        resultado = "Aprovado."
    else:
        resultado = "Reprovado."
    return resultado

media = media(nota1, nota2)
resultado = aprovado_ou_reprovado(media)

print(f"Média: {media}")
print(f"Resultado: {resultado}")

