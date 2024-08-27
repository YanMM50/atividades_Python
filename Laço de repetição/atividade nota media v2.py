import os
os.system("cls || clear")

QUANTIDADE_DE_NOTAS = 3 #uma constante
soma = 0 

for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f"Digite sua {i + 1 }º nota: "))
    soma = soma + nota

media = soma / QUANTIDADE_DE_NOTAS 

print(f" Média : {media}")

if media >= 7:
    print("Aprovado!")
elif media < 4:
    print("Resprovado!")
else:
    print("Recuperação!")

    
