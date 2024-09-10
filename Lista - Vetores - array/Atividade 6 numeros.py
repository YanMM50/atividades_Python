"""
Crie um programa que leia 6 números, armazenando em um vetor e informe quantos são pares e quantos são ímpares.

mostre os númros informados pelo usuário.

"""
import os
os.system("cls || clear")

QUANTIDADE_REPETICOES = 6
contador_par = 0
contador_impar = 0
lista_numero = []

for i in range (QUANTIDADE_REPETICOES):
    numero = int(input(f"Digite o {i+1}ª número: "))
    lista_numero.append(numero)
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print("\n=== Exibindo números ===")
for i, numero in enumerate(lista_numero):
    print(f"{i+1}ª {numero}")


print(f"Pares : {contador_par}")
print(f"Impares : {contador_impar}")
    
