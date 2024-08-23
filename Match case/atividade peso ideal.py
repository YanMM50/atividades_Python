import os
os.system("cls || clear")

peso_ideal = 0

print("""\n
1- Masculino (M)
2- Feminino (F)            """)

genero = input("Digite seu genero (M ou F): ").upper() #.upper() faz com que as letras se tornem maiusculas.
altura = float(input("Digite sua altura: "))            #.lower() faz o contrario.

match(genero):
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"\nSeu peso ideal seria: {peso_ideal: .2f}")
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"\nSeu peso ideal seria: {peso_ideal: .2f}")
    case _:
        print("Opção inválida.")
        

