import os
os.system("cls || clear")

#solicitando dados
numero = int(input("Digite um número para tabuada: "))

print(f"\nTabuada de multiplicação do número: {numero}")
for i in range(1,11):
    print(f"{numero} X {i} = {numero * i}")