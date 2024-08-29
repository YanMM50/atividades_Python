"""
Crie um programa que solicete ao usuário seu logi e senha.
O programa eve contiuar pedino o login e senha até que ambos estejam corretos.

"""


import os
os.system("cls || clear")

LOGIN_CORRETO = "Yan"
SENHA_CORRETA = "123"

while True:
    login = input("Digite seu login: ").strip()
    senha = input("Digite sua senha: ")

    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\nBem-vindo!")
        break
    else:
        print("""
              Login ou senha incorreta.
              Tente novamente. """)
        
        





