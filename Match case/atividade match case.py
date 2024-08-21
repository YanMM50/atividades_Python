import os
os.system("cls|| clear")


print("""
1 - Soma (+)
2 - Subitração (-)
3 - Divisão (/)
4 - Multiplicação (*)
      """)

opcao = input("Digite uma opção: ")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))


soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
divisao = primeiro_numero / segundo_numero
multiplicacao = primeiro_numero * segundo_numero

match(opcao):
    case "+":
        print(f"\nSoma: {soma}")
    case "-":
        print(f"\nSubtração: {subtracao}")
    case "/":
        print(f"\nDivisão: {divisao}")
    case "*":
        print(f"\nMultiplicção: {multiplicacao}")
    case _: 
        print("\nOpção invalida")





