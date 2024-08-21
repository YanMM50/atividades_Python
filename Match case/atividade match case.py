import os
os.system("cls|| clear")


print("""
1 - Soma
2 - Subitração
3 - Divisão
4 - Multiplicação
      """)

opcao = int(input("Digite uma opção: "))
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))


soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
divisao = primeiro_numero / segundo_numero
multiplicacao = primeiro_numero * segundo_numero

match(opcao):
    case 1:
        print(f"\nSoma: {soma}")
    case 2:
        print(f"\nSubtração: {subtracao}")
    case 3:
        print(f"\nDivisão: {divisao}")
    case 4:
        print(f"\nMultiplicção: {multiplicacao}")
    case _: 
        print("\nOpção invalida")





