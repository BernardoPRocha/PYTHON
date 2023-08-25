#Bernardo Rocha RM99209
#Kaylane Neves RM98919
#Kevin Beykam RM550154
import re

# Função para realizar o sorteio do funcionário
def sorteio_funcionario(integrantes):
    import random
    return random.choice(integrantes)

# Lista de integrantes do grupo
integrantes_grupo = ("Bernardo", "Kevin", "Kaylane")

# Dicionário de vinhos
vinhos = {
    1: {"nome": "Vinho Doce da Casa", "preco": 50.00, "estoque": 35},
    2: {"nome": "Vinho Espumante Brut", "preco": 35.00, "estoque": 0},
    3: {"nome": "Vinho Rosé Especial", "preco": 45.00, "estoque": 24},
    4: {"nome": "Vinho Branco Seco", "preco": 60.00, "estoque": 28},
    5: {"nome": "Vinho Tinto Reserva", "preco": 25.00, "estoque": 16}
}

# Função para calcular a idade
def calcular_idade(ano_nascimento):
    ano_atual = 2023
    return ano_atual - ano_nascimento

print("Bem-vindo à Vinheria Agnello!")

# Sorteio do funcionário
funcionario = sorteio_funcionario(integrantes_grupo)
print(f"O funcionário que irá acompanhar sua compra é: {funcionario}\n")

# Validações usando regex
try:
    print("Digite o seu nome.")
    nome_cliente = input()
    if re.search("\d", nome_cliente):
        erro = "Nomes não podem conter números" 
        raise ValueError
    print("Digite o seu CEP no formato: '12345-678'.")
    cep = input()
    if not re.search("^\d{5}-\d{3}$", cep):
        erro = "CEP deve conter 8 dígitos"
        raise ValueError
    print("Digite seu ano de nascimento no formato: '1234'.")
    ano_nascimento = input()
    if not re.search("\d{4}", ano_nascimento) or len(ano_nascimento) > 4: 
        erro = "Ano de nascimento deve conter 4 dígitos"
        raise ValueError
except ValueError:
    print(erro)
    exit()

ano_nascimento = int(ano_nascimento)
idade = calcular_idade(ano_nascimento)

if idade < 18:
    print("Desculpe, não é permitida a venda de bebidas alcoólicas a menores de idade.")
    
# Armazenar informações do cliente em um dicionário
cliente = {
    "nome": nome_cliente,
    "CEP": cep,
    "ano_nascimento": ano_nascimento
}

print("\nOpções de vinho disponíveis:")
for numero, vinho in vinhos.items():
    if vinho["estoque"] >= 1:
        print(f"{numero}. {vinho['nome']} - R${vinho['preco']:.2f}")

escolha_vinho = int(input("Escolha o número do vinho que deseja comprar: "))
    
if escolha_vinho not in vinhos or vinhos[escolha_vinho]["estoque"] == 0:
    print("Vinho indisponível.")
    
    
quantidade_compra = int(input("Digite a quantidade de garrafas que deseja comprar: "))
if quantidade_compra > vinhos[escolha_vinho]["estoque"]:
    print("Quantidade em estoque insuficiente.")

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

vinho_escolhido = vinhos[escolha_vinho]["nome"]
preco_unitario = vinhos[escolha_vinho]["preco"]
subtotal = preco_unitario * quantidade_compra
    
vinhos[escolha_vinho]["estoque"] -= quantidade_compra
    
# Informações da compra
print("\nInformações da compra:")
print(f"Nome do cliente: {cliente['nome']}")
print(f"Funcionário que atendeu: {funcionario}")
print(f"Vinho comprado: {vinho_escolhido}")
print(f"Quantidade comprada: {quantidade_compra}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Subtotal: R${subtotal:.2f}")
    
print("\nVolte Sempre!")

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#Estoque restante
print("\nNosso estoque ficou:")
for numero, vinho in vinhos.items():
    print(f" {vinho['nome']}     Preço R${vinho['preco']:.2f}     Estoque: {vinho['estoque']}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")