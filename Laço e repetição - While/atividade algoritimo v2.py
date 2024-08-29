import os
os.system("cls || clear")


while True:
    nota = float(input("Digite uma nova nota: "))

    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior ou igual 0 e menor e iqual a 10.")
    else:
        break #para o laço de repetição. 

print(f"Sua nota: {nota}")