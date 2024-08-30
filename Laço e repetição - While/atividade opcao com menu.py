"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota. Mostre um menu conforme o descrito abaixo

"""

import os 
os.system("cls || clear")

print("""
S - Inserir mais uma nota;
P - Ver quantas notas foram inseridas; 
N - Calcular a média aretmética das notas informadas.
      """)

opcao = input("Deseja inserir mais uma nota? ").upper()
loop = 0
soma = 0


while True:
    match(opcao):
        case "S":
            nota = float(input("Digite mais uma nota: "))
            loop += 1
            soma = soma + nota 
            opcao = input("Deseja continuar: ").upper()
        case "P":
            print(f"Notas inseridas: {loop}.")
            opcao = input("Deseja continuar: ").upper()
        case "N":
            media = soma / loop
            print(f"Média: {media}")
            opcao = input("Deseja continuar: ").upper()
        case _:
            print("Acabou.")
            break


