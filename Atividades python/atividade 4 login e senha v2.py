import os
os.system ("cls || clear")

#Declarando variáveis
login_salvo: str = "Yan"
senha_salva  = "123"

#Solicitando dados.
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

#verificando.
if login != login_salvo and senha != senha_salva:
    print("Login ou senha inválidos.")
else:
    print("Bem-vindo!")


