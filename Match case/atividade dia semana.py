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
    case 1:
        dia = "Domingo"
        dia_1 = "Final de semana."
    case 2:
        dia = "Segunda-feira"
        dia_1 = "Dia útil."
    case 3:
        dia = "Terça-feira"
        dia_1 = "Dia útil."
    case 4:
        dia = "Quarta-feira"
        dia_1 = "Dia útil."
    case 5:
        dia = "Quinta-feira"
        dia_1 = "Dia útil."
    case 6:
        dia =  "Sexta-feira"
        dia_1 = "Dia útil."
    case 7:
        dia = "Sabado"
        dia_1 = "Final de semana."
    case _:
        print("Invalido.") 


print(f"\nDia: {dia}, {dia_1}")
#print(f"{dia_1}")