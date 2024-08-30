"""
Crie um programa que solicite ao usuário seu login e uma senha.

O programa deve contiuar pedindo o login e senha até que ambos estejam corretos.

O Programa deve solicitar o login e seha apenas três vezes. caso ultrapasse o número de tentativas, o programa deve ser finalizado

"""

import os 
os.system("cls || clear")

QUANTIDADE_DE_REPETICAO = 3
LOGIN_CORRETO = "Yan"
SENHA_CORRETA = "123"
tentativas = 0


while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
            print("Bem-vindo!")
            break

    else: 
        print(f"login ou senha invalidos. {3 - tentativas} restantes.")
        tentativas += 1 #tentativas = tentativas + 1
        
        if tentativas > QUANTIDADE_DE_REPETICAO:
            print("Limite de tentativas atingido.")
            break
            


