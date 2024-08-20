import os
os.system("cls || clear")

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
    resultado = "Maior valor"  
else:
    resultado = "Menor valor" 

if segundo_numero > primeiro_numero:
    resultado_2 = "Maior valor"
else:
    resultado_2 = "Menor valor" 

print("\nExibindo resultado: ")
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Media: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"\nResultado: \n{resultado} {primeiro_numero} \n{resultado_2} {segundo_numero}")