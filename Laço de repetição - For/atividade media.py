import os
os.system("cls || clear")

soma = 0

for i in range(4):
    nota = float(input(f"Digite sua {i + 1}º nota: "))
    soma =  soma + nota
    


media = soma / 4

print(f"Média: {media}")