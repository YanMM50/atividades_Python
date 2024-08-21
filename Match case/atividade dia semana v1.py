import os
os.system("cls || clear")  # Limpar o terminal

print("""
1 - Domingo
2 - Segunda-feira
3 - Terça-feira
4 - Quarta-feira
5 - Quinta-feira
6 - Sexta-feira
7 - Sábado
""")

# Lê o dia da semana como um número inteiro
dia_da_semana = int(input("Digite um dia da semana (1 a 7): "))

# Determina a mensagem com base no valor de dia_da_semana
if dia_da_semana == 1 or dia_da_semana == 7:
    mensagem = "Final de semana."
elif 2 <= dia_da_semana <= 6:
    mensagem = "Dia útil."
else:
    mensagem = "Entrada inválida."

# Imprime a mensagem apropriada
print(f"\nDia {dia_da_semana}: {mensagem}")