import os
os.system("cls || clear")

# Entrada
lista_notas = []

for i in range(2):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota) #Adiciona uma nota a lista.


# Saída.

for i, nota in enumerate (lista_notas):
    print(f"{i}ª nota: {nota}")