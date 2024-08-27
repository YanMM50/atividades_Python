import os
os.system("cls || clear")

import time

numero = int(input("Digite um valor: "))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1)
