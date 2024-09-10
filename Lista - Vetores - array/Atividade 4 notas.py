"""
Crie um programa que leia 4 notas, armazenando em um vetor e calcule a média aritmética

verigique a situação do aluno considerando:
-Média maior ou igual a 7: aprovado. 
-Média maior ou igual a 5: recuperação
-Média menor que 5: reprovado

Mostre as 4 notas informadas pelo usuário e informe a média.
"""

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 4    
lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado."
elif media >= 5:
    resultado = "Recuperação."
else:
    resultado = "Reprovado."

print("\n=== Exibindo notas ===")
for i, nota in enumerate(lista_notas):
    print(f"Sua {i+1}ª nota: {nota}")


print("\n=== Exibindo média ===")
print(f"Média: {media}")

print("\n=== Exibindo Resultado ===")
print(f"Resultado: {resultado}")
