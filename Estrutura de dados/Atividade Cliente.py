import os
from dataclasses import dataclass

os.system("cls || clear")

# Etrutura de dados.

@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float


print("\n=== Solicitando dados dos clientes ===")

def coletando_dados():
    QUANTIDADE_CLIENTE = 4
    lista_de_alunos = []
    for i in range(QUANTIDADE_CLIENTE):
        cliente = Cliente(

            nome = input("Digite seu nome: "),
            sobrenome = input("Digite seu sobrenome: "),
            idade = int(input("Digite sua idade: ")),
            peso = float(input("Digite seu peso: ")),
            altura = float(input("Digite sua altura: "))
        )
        lista_de_alunos.append(cliente)
    return lista_de_alunos, cliente

lista_atualizada_clientes, cliente = coletando_dados()


# Salvar em um arquivo chamado: carteira_de_clientes.txt

nome_arquivo_cliente = "Lista_De_Clientes.txt"

with open(nome_arquivo_cliente, "w") as lista_clientes:
    for cliente in lista_atualizada_clientes:
        lista_clientes.write(f"{cliente.nome}, {cliente.sobrenome}, {cliente.idade}, {cliente.peso}, {cliente.altura}\n")
    
    lista_clientes.close()



# Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal.
print("\n=== Dados dos clientes salvo com sucesso! ===")
lista_atualizada_clientes = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_arquivo_cliente, "r") as arquivo_clientes:
    for linha in arquivo_clientes:
        nome, sobrenome, idade, peso, altura = linha.strip() .split(",")
        lista_atualizada_clientes.append(Cliente(nome=nome, sobrenome= sobrenome, idade = int(idade), peso = float(peso), altura = float(altura)))

arquivo_clientes.close()

print("\n===Exibindo dados dos alunos ===")
for aluno in lista_atualizada_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Sobrenome: {cliente.sobrenome}")
    print(f"Idade: {cliente.idade}")
    print(f"Peso: {cliente.peso}")
    print(f"Altura: {cliente.altura}")

