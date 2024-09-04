"""
Crie um programa que ajude um estudante a calcular a média de suas notas. O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo. O programa deve calcular e exibir a média das notas inseridas.

"""

import os
os.system("cls || clear")

opcao = input("Deseja inserir uma nota? ").upper()
soma = 0
iteracoes = 0

while True:
    match opcao: 
        case "S":
            nota = float(input("Digite sua nota: "))
            if nota < 0 or nota > 10:
                print("Nota tem que ser maior que 0 e menor que 10.")
                break     
            iteracoes += 1
            soma = soma + nota
            opcao = input("Deseja inserir outra nota S or N? ").upper() 
        case "N":
            print("Finalizado.")
            break

media = soma / iteracoes
        
            


print(f"Média: {media}")