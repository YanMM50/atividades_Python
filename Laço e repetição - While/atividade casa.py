"""
Escreva um algoritimo leia três njotas de um aluno. Caso seja menor que 0 ou maior que 10. mostre a pergunta novamente.

Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado recuperação ou reprovado considerando os seguintes critérios:

se a média for a partir de 7, aprovado;
se a média for entre 5 e 6,9, o aluno está em recuperação;
caso seja menor que 5, o aluno está reprovado.

"""

import os
os.system("cls || clear")

nota_um = float(input("Digite sua primeira nota: "))
nota_dois = float(input("Digite sua segunda nota: "))
nota_tres = float(input("Digite sua terceira nota: "))

while True:
    if nota_um < 0 or nota_um > 10:
        print("Erro, Digite novamente.")
        nota_um = float(input("Digite sua primeira nota: "))
    elif nota_dois < 0 or nota_dois > 10:
        print("Erro, Digite novamente.")
        nota_dois = float(input("Digite sua segunda nota: "))
    elif nota_tres < 0 or nota_tres > 10:
        print("Erro, Digite novamente.")
        nota_tres = float(input("Digite sua terceira nota: "))
    else:
        break    


soma = nota_um + nota_dois + nota_tres
media = soma / 3

if media >= 7:
    print("Aprovado")
elif media == 5 or media <= 6.9:
    print("Recuperação")
elif media < 5:
    print("Reprovado")

print(f"Média {media}")

    

