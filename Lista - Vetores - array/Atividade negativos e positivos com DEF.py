"""
Crie um algoritmo que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

"""
import os
os.system("cls || clear")

QUANTIDADE = 4
lista_de_numeros = []
lista_negativos = []
lista_positivos = []

def verificar_numeros_positivos(lista_numeros):
    # Processamento.
    lista_de_positivos= []
    
    for numero in lista_numeros:
        if numero > 0:
            lista_de_positivos.append(numero)
        
    # comando sum() - retorna a soma dos elementos no vetor/lista
    soma_positivos = sum(lista_de_positivos)   
    return soma_positivos


def verificar_numeros_negativo(lista_numeros_negativos):
    # Processamento.
    lista_de_negativos = []
    for numero in lista_numeros_negativos:
        if numero < 0:
            lista_de_negativos.append(numero)

    #comando len() - retorna a quantidade de elementos no vetor/lista
    quantidade_negativos = len(lista_de_negativos) 
    return quantidade_negativos


print("=== Solicitando dados ===")
for i in range(QUANTIDADE):
    numero = float(input(f"Digite o {i+1}ª número: "))
    lista_de_numeros.append(numero)
    

#processando.
quantidade_de_negativos = verificar_numeros_negativo(lista_de_numeros)
soma_de_positivos = verificar_numeros_positivos(lista_de_numeros)


print("=== Exibindo resultados ===")

print(f"número negativos: {quantidade_de_negativos}")

print(f"Soma dos positivos: {soma_de_positivos}")