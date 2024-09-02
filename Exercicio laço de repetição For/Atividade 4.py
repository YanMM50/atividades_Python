"""
Escreva
um programa que use um laço `for` para exibir a tabuada do 2, de 2 até 20.

"""
import os
os.system("cls || clear")

import time


print("Tabuada de 2:")

for i in range(1,21):
    print(f"2 X {i} = {2 * i}")
    time.sleep(1)
