"""
Crie um algoritmo que aceite apenas 6 valores inteiros, positivos e pares, em seguida, mostre na tela os valores lidos na ordem inversa.

Caso seja informado um número diferente dos critérios apresentados a cima, repita a pergunta para o usuário.

"""

import os
os.system("cls || clear")

QUANTIDADE = 6

def verificar_lista():
    lista_valores = []

    for i in range(QUANTIDADE):
        while True:
            numero = int(input(f"Digite um número: "))

            if numero % 2 != 0 or numero < 0:
                print("Invalido. Valor tem que ser inteiro, positivo e par.")
            else:
                lista_valores.append(numero) 
                break
    return lista_valores

lista_atualizada = verificar_lista()

print("\n=== Exibindo ===")
for i, numero in enumerate(reversed(lista_atualizada)):
    print(f"{len(lista_atualizada)- i}º - {numero}")


    
