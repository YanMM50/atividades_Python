import os
os.system("cls || clear")

#apresentando opções
print("""
1- Janeiro
2- Fevereiro
3- Março
4- Abril        
5- Maio
6- Junho
7- Julho
8- Agosto
9- Setembro
10- Outubro
11- Novembro
12- Dezembro     """)

#solicitando 
mes = int(input("\nEscolha um número de acordo com o mês (1 a 12): "))

#definindo as opções
match(mes):
    case 1:
        print("\nJaneiro")
    case 2:
        print("\nFevereiro")
    case 3:
        print("\nMarço")
    case 4:
        print("\nAbril")
    case 5:
        print("\nMaio")
    case 6:
        print("\nJunho")
    case 7:
        print("\nJulho")
    case 8:
        print("\nAgosto")
    case 9:
        print("\nSetembro")
    case 10:
        print("\nOutubro")
    case 11:
        print("\nNovembro")
    case 12:
        print("\nDezembro")
    case _:
        print("\nInválido.")

#Teste if aniversario
if mes == 1 or  mes == 2 or mes == 3 or mes == 4 or mes == 5 or mes == 6 or mes == 7 or mes == 8 or mes == 9 or mes == 10  or mes == 11 or mes == 12:
    escolha = input("\nDigite a data do seu aniversario: ")
