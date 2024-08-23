import os
os.system("cls || clear")

print("""
1- Pagamento à vista
2- Pagamento à prazo      """)

desconto = 0


forma_de_pagamento = input("Digite a forma de pagamento: ")

if forma_de_pagamento == "Pagamento à vista":
    print("\nVocê ganhou 10% de desconto")
else:
    print("\nValor do produto: R$100,00")


if forma_de_pagamento == "Pagamento à prazo":
    quantidade_de_parcelas = int(input("\nQuantas parcelas? (ate 6x) "))

if forma_de_pagamento == "Pagamento à prazo" and quantidade_de_parcelas > 6:
    print("\nInválido.")

match (forma_de_pagamento):
    case "Pagamento à vista":
        desconto = 100 * 0.10
        preco_final = 100 - desconto

        print(f"""\n
            Valor do produto: R$100,00
            Forma de pagamento: à vista
            Valor do desconto: {desconto}%
            Total a pagar: {preco_final}
              """) 
    case "Pagamento à prazo":
        preco_parcelado = 100 / quantidade_de_parcelas
        preco_final = 100

        print(f"""\n
              Valor do produto: R$100,00
              Forma de pagamento: à prazo
              Quantidade de parcelas: {quantidade_de_parcelas}
              Valor por parcela: {preco_parcelado:.2f} 
              Total à prazo: {preco_final}
              """)    

# o 2f é a quantidade de casas decimais
