import os
os.system("cls || clear")

def numeracao():
    print(f"Primeiro número: {numero_1}")
    print(f"Segundo número: {numero_2}")

def calcular_media(calculo1, calculo2):
    soma = calculo1 + calculo2
    media = soma / 2

    return media
    

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um segundo número: "))

media = calcular_media(numero_1, numero_2)
numeracao()

print(f"Media: {media}")
