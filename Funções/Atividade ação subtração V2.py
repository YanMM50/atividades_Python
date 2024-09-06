"""
Crie funções que recebam 2 números e retorne a soma, subtração, divisão ea multiplicação deste dois números informados

Obs.: Crie uma função para cada operação

"""

import os
os.system("cls || clear")

numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite um segundo número: "))


def soma(n1, n2):    
        soma = n1 + n2
        return soma #tem como fazer a conta dentro do return 

def subtracao(n1, n2):    
        subtracao = n1 - n2
        return subtracao 

def divisao(n1, n2):    
        divisao = n1 / n2
        return divisao

def multiplicacao(n1, n2):    
        multiplicacao = n1 * n2
        return multiplicacao


resultado = soma(numero_um, numero_dois)
resultado2 = subtracao(numero_um, numero_dois)
resultado3 = divisao(numero_um, numero_dois)
resultado4 = multiplicacao(numero_um, numero_dois)

print(f"Soma: {resultado}")
print(f"Subitração: {resultado2}")
print(f"Divisão: {resultado3}")
print(f"Multiplicação: {resultado4}")

    
    


