"""
Crie um programa que solicite ao usuário criar uma senha. O programa deve então pedir para confirmar a senha e garantir que ambas as senhas coincidam. Se as senhas não coincidirem, o programa deve continuar pedindo para o usuário inserir e confirmar a  tenha até que ambas sejam iguais.

"""

import os
os.system("cls || clear")

senha_cadastrada = "123"

while True:
    senha = input("Digite sua senha: ")

    if senha != senha_cadastrada:
        senha = input("Digite novamente: ")
    else: 
        print("Bem-vindo!")
        break
