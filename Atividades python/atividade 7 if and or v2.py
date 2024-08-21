import os 
os.system ("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


if idade < 18 or idade > 65:
    resultado = "Não é obrigatorio votar!"
else:
    resultado = "Pode votar!"

print(f"Nome: {nome}")
print(f"Idade: {idade}") 
print(f"{resultado}") 