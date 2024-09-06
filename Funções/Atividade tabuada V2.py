"""
Faça um  programa que imprime a tabuada de um número informado pelo usuário de 1 a 10 utilizando uma função para exibir o resultado

"""

import os
os.system("cls || clear")


numero = int(input("Digite um número: "))

def tabuada(n1,i):
    return f"{n1} X {i} = {n1 * i}"


for i in range(11):
    print(tabuada(numero,i))



    