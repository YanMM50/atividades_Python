"""
Crie funções que recebam 2 números e retorne a soma, subtração, divisão ea multiplicação deste dois números informados

Obs.: Crie uma função para cada operação

"""

import os
os.system("cls || clear")


numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite um segundo número: "))
opcao = int(input("""Digite uma opção: 
                  1 - Soma
                  2 - Subitração
                  3 - Divisão
                  4 - Multiplicação: """))

def operacao(n1, n2, opcao):
    match(opcao):
        case 1:
            resultado = n1 + n2
        case 2:
            resultado = n1 - n2
        case 3:
            resultado = n1 / n2
        case 4:
            resultado = n1 * n2
        case _:
            print("Invalido.")
    return resultado



resultado = operacao(numero_um, numero_dois, opcao)
print(f"Resultado = {resultado}")
    
    


