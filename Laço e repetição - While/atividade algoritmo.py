import os
os.system("cls || clear")


nota = float(input("Digite uma nota: "))


while nota < 0 or nota > 10:
    print("\nA nota deve ser maior ou igual 0 e menor e iqual a 10.")
    nota = float(input("Digite uma nova nota: "))


print(f"Sua nota: {nota}")