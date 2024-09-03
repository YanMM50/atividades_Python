"""
Crie um programa para ajudar o usuário a acompanhar suas metas de estudo. O usuário define uma meta de horas de estudo e o programa deve permitir que o usuário insira o número de horas estudadas até que o total atinja ou exceda a meta. O programa deve  exibir o total de horas estudadas e o valor excedente.

"""

import os
os.system("cls || clear")

soma_da_meta = 0
meta_diaria = 5

while True: 
    meta = float(input("Meta diaria em horas: "))
    soma_da_meta += meta

    if soma_da_meta >= meta_diaria:
        print("Tempo limite excedido.")
        print(f"Hoje você estudou por {soma_da_meta}")
        break
