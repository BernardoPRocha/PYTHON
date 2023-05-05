import random
#sorteio do funcionario
sorteio = random.randint(1,5)
if sorteio == 1: nomefunc = "Bernardo"
elif sorteio == 2: nomefunc = "Kaylane"
elif sorteio == 3: nomefunc = "Kevin"
elif sorteio == 4: nomefunc = "Gabriela"
else: nomefunc = "Rodrigo"
#mesagem de boas-vindas
print(f"Bem-Vindo à Vinheria Agnello. \nO funcionário {nomefunc} vai acompanhá-lo nesta compra." )
#requisitando informações
print("Informe o seu nome")
nome = input()
print("Informe o seu CEP")
cep = input()
print("Informe o ano de seu nascimento")
anoNasc = int(input())
#verificando a maioridade
idade = 2023 - anoNasc
if idade < 18:
    print(f"{nome} não é permitida a venda para menores de 18 anos!")
else:
    #variáveis para auxiliar nos cálculos 
    subtotal = total = 0
    #preparando a mesagem final
    msgfinal = f"Dados da compra: \nAtendido por: {nomefunc} \nCliente: {nome}\nItens da compra\t\tValor\t\tQtde\tSubtotal\n"
    #repetindo a venda de vinhos
    continua = "sim"
    while continua.lower() == "sim":
        #exibindo opçoes de vinhos
        print("Escolha um dos vinhos da lista: \n(1) Vinho suave tinto\tR$ 15.00\n(2) Vinho seco tinto\tR$25.00\n(3) Vinho suave branco\tR$35.00\n(4) Vinho seco branco\tR$30.00\n(5)Vinho sem álcool\tR$40.00")
        #armazenando o vinho escolhido e a quantidade
        vinho = int(input())
        print("Em qual quantidade deseja adquirir este vinho?")
        qtde = int(input())
        match vinho:
            case 1:
                subtotal = 15 * qtde
                msgfinal += f"Vinho suave tinto\tR$15.00\t\t{qtde}\tR$ {subtotal:.2f}\n"
            case 2:
                subtotal = 25 * qtde
                msgfinal += f"Vinho seco tinto\tR$25.00\t\t{qtde}\tR$ {subtotal:.2f}\n"
            case 3:
                subtotal = 35 * qtde
                msgfinal += f"Vinho suave branco\tR$35.00\t\t{qtde}\tR$ {subtotal:.2f}\n"
            case 4:
                subtotal = 30 * qtde
                msgfinal += f"Vinho seco branco\tR$30.00\t\t{qtde}\tR$ {subtotal:.2f}\n"
            case 5:
                subtotal = 40 * qtde
                msgfinal += f"Vinho sem álcool\tR$40.00\t\t{qtde}\tR$ {subtotal:.2f}\n"
            case _ :
                print("Por favor, escolha uma das opções da lista")
        total += subtotal
        #continuando a compra ou não
        print("Deseja continuar comprando? (responda sim ou não)")
        continua = input()
    #finalizando a compra
    print(msgfinal)
    #verficando o frete
    if total < 200:
        print("Valor do frete: R$30.00")
    else:
        print("Frete Grátis!!")
#exibindo mensagem de despedida 
print(f"{nome}, foi um prazer atendê-lo. Volte em breve!")
