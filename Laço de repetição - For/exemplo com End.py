import os
os.system("cls || clear")

import time
import sys

# Simula uma barra de progresso que vai de 0% a 100%
for i in range(101):
    # Imprime o progresso na mesma linha
    print(f"\rProgresso: {i}%", end="")
    time.sleep(0.1)  # Simula uma tarefa demorada

print("\nConcluído!")
