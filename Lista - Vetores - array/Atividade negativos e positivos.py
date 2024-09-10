"""
Crie um algoritmo que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

"""
import os
os.system("cls || clear")

QUANTIDADE = 10
lista_de_numeros = []
lista_negativos = []
lista_positivos = []

print("=== Solicitando dados ===")
for i in range(QUANTIDADE):
    numero = float(input(f"Digite o {i+1}ª número: "))
    lista_de_numeros.append(numero)
    
    if numero < 0:
        lista_negativos.append(numero)
    else:
        lista_positivos.append(numero)

#comando len() - retorna a quantidade de elementos no vetor/lista
quantidade_negativos = len(lista_negativos) 
# comando sum() - retorna a soma dos elementos no vetor/lista
soma_positivos = sum(lista_positivos)

print("=== Exibindo resultados ===")
for i, numero in enumerate(lista_negativos):
    print(f"{i+1}ª número negativos: {numero}")

print(f"Soma dos positivos: {soma_positivos}")