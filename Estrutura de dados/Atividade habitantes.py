
import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Habitantes:
    idade:int
    sexo:str
    salario:float

@dataclass
class Final:
    lista_final:list

def menu():
    print("""
Código  |   Descrição
   1    |  Adicionar pessoa
   2    |  Exibir resultados
   3    |  Sair
""")

def limpar_tela():
    os.system("cls || clear ")

def criando_arquivo(a, b):
    with open(a,"a") as arquivo_habitantes:
        for habitantes in b:
            arquivo_habitantes.write(f"{habitantes.idade},{habitantes.sexo},{habitantes.salario}\n")
        arquivo_habitantes.close()

def criando_arquivo_final(a, b):
    with open(a,"a") as arquivo_habitantes:
        for habitantes in b:
            arquivo_habitantes.write(f"{habitantes}, \n")
        arquivo_habitantes.close()

def lendo_arquivos(a):
    with open(a, "r") as lendo_habitantes:
        for linha in lendo_habitantes:
            idade, sexo, salario = linha.strip().split(",")
            lista_final.append(Habitantes(idade = int(idade), sexo = sexo, salario = float(salario)))
        lendo_habitantes.close()
    return lista_final

def media(a):
    QUANTIDADE = len(a)
    soma = sum(a)
    if QUANTIDADE == 0:
        return 0
    else:
        media = soma / QUANTIDADE
        return media

while True:
    lista_final = []
    menu()
    opcao = int(input("Resposta: "))
    match opcao:
        case 1:
            habitantes = Habitantes(
                idade = int(input("Digite sua idade: ")),
                sexo = input("Digite seu gênero: ").lower().strip(),
                salario = float(input("Digite quanto de salário você recebe: ")),
            )
            lista_final.append(habitantes)
            nome_arquivo = "dados.txt"
            criando_arquivo(nome_arquivo, lista_final)
            limpar_tela()
        case 2:
            lista_final1 = []
            contador = 0
            limpar_tela()
            lista_salario = []
            lista_idade = []
            nome_arquivo = "dados.txt"
            lista_final1 = lendo_arquivos(nome_arquivo)
            for habitantes in lista_final1:
                lista_idade.append(habitantes.idade)
                if habitantes.sexo == "f" and habitantes.salario >= 5000:
                    contador += 1
                lista_salario.append(habitantes.salario)
                
            media_salario = media(lista_salario)
            maior_idade = max(lista_idade)
            menor_idade = min(lista_idade)
            lista_final.append(contador) 
            lista_final.append(media_salario) 
            lista_final.append(maior_idade)
            lista_final.append(menor_idade) 
            nome_arquivo = "pesquisa_habitantes.txt"
            criando_arquivo_final(nome_arquivo, lista_final)
            print("\n=== Exibindo resultado ===")
            print(f"Média salário do grupo: {media_salario}")
            print(f"Maior idade do grupo: {maior_idade}")
            print(f"Menor idade do grupo: {menor_idade}")
            print(f"Quantidade de mulheres com salário a partir de R$ 5000,00: {contador}")
        case 3:
            print("Programa encerrado")
            break
        case _:
            print("Opção inválida. Tente novamente")
            continue