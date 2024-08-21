import os 
os.system ("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


if idade >= 18 and idade <= 65:
    resultado = "Pode votar!"
else:
    resultado = "Não é obrigatorio votar!"

print(f"Nome: {nome}")
print(f"Idade: {idade}") 
print(f"{resultado}") 