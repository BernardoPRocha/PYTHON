#Bernardo Rocha RM99209
#Kaylane Neves RM98919
#Kevin Beykam RM550154
import random
funcionarios = ['Gabriela', 'Kaylane', 'Bernardo', 'Kevin']
print('Bem-Vindo à Vinheria Agnello!')
funcionario = random.choice(funcionarios)
print(f'O funcionário que irá lhe atender é: ', funcionario)
cep = input('Por Favor, informe o seu CEP:')
an = int(input('Informe o seu ano de nascimento:'))
nome = str(input("Informe o seu nome:"))
#Verficando idade do comprador
idade = 2023 - an
if idade < 18:
    print('Desculpe, não é permitida a venda de bebidas alcóolicas para menores de 18 anos.')
    exit(0)
if idade >= 18:
    print("""Aqui está uma lista dos nosso vinhos disponíveis:

Cabernet Sauvignon: Um vinho tinto encorpado com notas de frutas escuras, como cassis e amora, e aromas de carvalho, como baunilha e tostado. Preço: R$400

Chardonnay: Um vinho branco encorpado com notas de frutas tropicais, como abacaxi e manga, e aromas de carvalho, como baunilha e manteiga. Preço: R$300

Pinot Noir: Um vinho tinto suave com notas de frutas vermelhas, como cerejas e morangos, e aromas de especiarias, como canela e cravo. Preço: R$500

Sauvignon Blanc: Um vinho branco leve com notas de frutas cítricas, como limão e grapefruit, e aromas de ervas frescas, como manjericão e menta. Preço: R$250

Malbec: Um vinho tinto encorpado com notas de frutas escuras, como ameixas e figos, e aromas de especiarias, como pimenta e cravo. Preço: R$ 300

""")

Vinho1 = 400.00
Vinho2 = 300.00
Vinho3 = 500.00
Vinho4 = 250.00
Vinho5 = 300.00

respostaMaiuscula = ""

while respostaMaiuscula != "N":
    print("Qual vinho você irá comprar?")
    Vinho = int(input("1 - Cabernet Sauvignon\n2 - Chardonnay\n3 - Pinot Noir\n4 - Sauvignon Blanc\n5 - Malbec\n"))
    match Vinho:
        case 1 : 
            print("Quantos unidades você deseja?")
            unidades = int(input())
            preço1 = float(400.00 * unidades)
            nomeVinho = "Cabernet Sauvignon"
        case 2:
            print("Quantos unidades você deseja?")
            unidades = int(input())
            preço2 = float(300.00 * unidades)
            nomeVinho = "Chardonnay"
        case 3:
            print("Quantos unidades você deseja?")
            unidades = int(input())
            preço3 = float(500.00 * unidades)
            nomeVinho = "Pinot Noir"
        case 4:
            print("Quantos unidades você deseja?")
            unidades = int(input())
            preço4 = float(250.00 * unidades)
            nomeVinho = "Sauvignon Blanc"
        case 5:
            print("Quantos unidades você deseja?")
            unidades = int(input())
            preço5 = float(300.00 * unidades)
            nomeVinho = "Malbec"
    resposta = str(input("Deseja continuar? [S/N] "))
    respostaMaiuscula = resposta.upper ()
valor_compra = preço1 + preço2 + preço3 + preço4 + preço5
print(f"Cliente {nome}, {funcionario} irá finalizar o seu pedido agora.")
print(f"Você comprou")



    
