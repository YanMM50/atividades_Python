"""
Crie um programa que permita ao usuário registrar o número de calorias consumidas em cada refeição. O programa deve continuar registrando as calorias até que o total de calorias consumidas ultrapasse 2000 calorias. Após exceder 2000 calorias, exiba o total de calorias consumidas e o excesso.

"""
import os
os.system("cls || clear")

soma = 0 

while True:
    calorias = int(input("calorias cosumidas: "))
    soma += calorias

    if soma > 2000:
        print(f"Calorias totais consumida: {soma}")
        print(f"Excesso de calorias: {soma}")
        break
