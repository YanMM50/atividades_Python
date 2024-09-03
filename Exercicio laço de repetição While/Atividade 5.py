"""
Desenvolva um programa que solicite ao usuário inserir um código de promoção para obter um desconto. O código correto é "PROMO2024". O usuário tem 3 tentativas para acertar o código. Se o código estiver correto, exiba uma mensagem de "Código aceito" e o desconto. Se o usuário errar o código nas 3 tentativas, exiba uma mensagem de "Código inválido".

"""

import os
os.system("cls || clear")

TENTATIVAS = 3
codigo_promocao = "PROMO2024"
tentativa = 0
  
while True:
    codigo = input("Digite o codigo da promoção: ")
    tentativa += 1
        
    if codigo == codigo_promocao:
        print(f"Codigo aceito, ganhou o desconto de 20%")
        break
        
    else:
        print(f"Tentativas restantes: {TENTATIVAS - tentativa}")

    if tentativa >= TENTATIVAS:
        print("Código invalido. tentativas esgotadas")
        break

        
        


