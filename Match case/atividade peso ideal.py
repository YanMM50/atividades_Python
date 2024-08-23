import os
os.system("cls || clear")

print("""\n
1- Masculino (M)
2- Feminino (F)            """)

genero = input("Digite seu genero: ")
altura = float(input("Digite sua altura: "))

match(genero):
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"\nSeu peso ideal seria: {peso_ideal: .2f}")
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"\nSeu peso ideal seria: {peso_ideal: .2f}")
