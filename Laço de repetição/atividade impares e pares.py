import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Digite {i + 1} número: "))
    if numero % 2 == 0: # o sinal de % pega o resto da divisão exemplo 2 / 2 = 0 (== 0)
        pares = pares + 1
        
    else:
        impares = impares + 1
        

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")