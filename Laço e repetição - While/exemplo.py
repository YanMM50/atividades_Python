import os
os.system("cls || clear")

contador = 0 
continua = 's'

while continua == 's':
    #comando a serem repetidos.
    print("Repetindo...")

    contador += 1 #abreviado
    #contador = contador + 1

    continua = input("Tecle 's' se deseja continuar: ").strip().lower() #strip pra tirar a barra de espaço, lower caso digite a letra maiuscula ele ira diminuir
    

if contador == 0:
    print("O bloco NÃO foi repetido")
else:
    print(f"O bloco foi repetido {contador} vezes")
