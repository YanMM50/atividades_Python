"""


"""

import os
os.system("cls || clear")

lista_numero = []
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f"Digite o {i+1}ª numero: "))
    lista_numero.append(numero)

def impar_par(n1):
    contador_par = 0
    contador_impar = 0

    for numero in n1:
        if numero % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
    return contador_par, contador_impar
   
pares, impares = impar_par(lista_numero)

print("=== Exibindo números ===")
for i, numero in enumerate(lista_numero):
    print(f"{i+1}ª: {numero}")


print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")