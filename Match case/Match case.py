import os
os.system("cls|| clear")


print("""
1 - cadastar usuário
2 - excluir usuário
3 - sair do sistema
      """)

opcao = int(input("Digite uma opção: "))

match(opcao):
    case 1:
        print("\nCadastar usuário.")
    case 2:
        print("\nExcluir usuário.")
    case 3:
        print("\nSair do sistema.")
    case _:
        print("\nOpção inválida. ")


