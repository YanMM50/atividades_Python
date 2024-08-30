"""
Escreva um algoritimo leia três njotas de um aluno. Caso seja menor que 0 ou maior que 10. mostre a pergunta novamente.

Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado recuperação ou reprovado considerando os seguintes critérios:

se a média for a partir de 7, aprovado;
se a média for entre 5 e 6,9, o aluno está em recuperação;
caso seja menor que 5, o aluno está reprovado.

"""

import os
os.system("cls || clear")

QUANTIDADE_DE_REPETICAO = 3
soma = 0

for i in range(QUANTIDADE_DE_REPETICAO):
    while True:
        nota = float(input(f"Digite sua {i + 1}º nota: "))
        soma += 1

        if nota < 0 or nota > 10:
            print("Erro, Digite novamente.")
            nota = float(input("Digite sua nota: "))
        else:
            break    


media = soma / 3

if media >= 7:
    print("Aprovado")
elif media == 5 or media <= 6.9:
    print("Recuperação")
elif media < 5:
    print("Reprovado")


print(f"Média {media}")

    

