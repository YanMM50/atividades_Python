"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota, se a resposta do usário for "N", o pragrama fará a média aritmética das notas informadas e mostrará a media artmética para o usuário. 

Obs: Use um contador dentro do laço de repetição para contar a quantidade de iterações (Loops)

"""

import os 
os.system("cls || clear")

opcao = (input("Deseja digitar uma nota? ")).upper()
#opcao = opcao.upper() #Converter em maiúscula.
loops = 0
soma = 0

while True:    
    match(opcao):
        case "S":
            nota = float(input(f"Digite uma nota: "))
            loops += 1
            soma = soma + nota
            opcao = (input("Deseja digitar mais uma nota? ")).upper()

        case "N":
            media = soma / loops
            break




print(f"Média: {media}")
print(f"Iterações: {loops}")


        




