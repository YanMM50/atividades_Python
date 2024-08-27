import os
os.system("cls || clear")

soma = 0 

for i in range(3):
    nota = float(input(f"Digite sua {i + 1 }º nota: "))
    soma = soma + nota

media = soma / 3 

print(f" Média : {media}")

if media >= 7:
    print("Aprovado!")
elif media < 4:
    print("Resprovado!")
else:
    print("Recuperação!")

    
