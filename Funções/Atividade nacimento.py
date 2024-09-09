"""
Escreva um programa que solicite ao usúario o ano de nacimento e, utilizando uma função, reotrne com a idade do usuário.

"""

import os
os.system("cls || clear")

data_nascimento = int(input("Digite sua data de nascimento: "))

def idade(n1):
    ano = 2024
    idade = ano - n1

    return idade


idade_real = idade(data_nascimento)


print(f"Idade : {idade_real} anos.")
