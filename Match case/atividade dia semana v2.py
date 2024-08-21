import os
os.system("cls || clear")


print("""
1 - Domingo
2 - Segunda-feira
3 - Terça-feira
4 - Quarta-feira
5 - Quinta-feira
6 - Sexta-feira
7 - Sabado
          """)


dia_da_semana = int(input("Digite um dia da semana (1 a 7): "))


match(dia_da_semana):
    case 1 | 7:
        dia_1 = "Final de semana."
    case 2 | 3 | 4 | 5 | 6:
        dia_1 = "Dia útil."
    case _:
        dia_1 = "Opção inválida."
           


print(f"\nDia: {dia_1}")
#print(f"{dia_1}")