"""
Crie um programa que peça ao usuário para inserir números inteiros até que a soma dos números ímpares inseridos seja maior que 200. O programa deve exibir o total de números ímpares inseridos e a soma desses números. 

"""
import os
os.system("cls || clear")

impares = 0
soma = 0
pares = 0

while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        pares = pares + 1
    else: 
        impares += 1 
        soma += numero

    if soma > 200:
        print("Limite excedido")
        break

print(f"Total de número impares: {impares}")
print(f"Soma dos números impares: {soma}")