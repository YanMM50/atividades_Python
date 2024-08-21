import os
os.system ("cls || clear")

#solicitando dados.
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

#verificar
login_correto = login == "Yan"
senha_correta = senha == "123"


if login_correto and senha_correta:
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos.")


