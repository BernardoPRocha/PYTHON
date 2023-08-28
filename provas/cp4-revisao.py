import re 
import random
def sorteianome(funcionarios):
    return random.choice(funcionarios)

funcionarios = ("Astrogildo", "Berisvaldo", "Gumercindo")
nomefunc = sorteianome(funcionarios)

vinhos = {
    "Vinho 1": {"nome":"Tinto","valor":15.0,"estoque":10},
    "Vinho 2": {"nome":"Agudo","valor":15.0,"estoque":10},
    "Vinho 3": {"nome":"Sunco","valor":15.0,"estoque":10},
    "Vinho 4": {"nome":"Seco","valor":15.0,"estoque":10},
    "Vinho 5": {"nome":"Branco","valor":15.0,"estoque":10}
}

print(f"Bem-Vindo à Vinheria Agnello.")
print(f"O funcionário {nomefunc} vai acompanhá-lo")

erro = ""
try :
    print("Informe seu nome")
    nome = input()
    if re.search("\d", nome):
        erro = "O nome não pode conter números"
        raise ValueError
    print("Informe o seu CEP")
    cep = input()
    if re.search("[0-9]{5}-\d{3}", cep) or len(cep) > 9:
        erro = "CEP inválido (formato: 00000-000)"
        raise ValueError
    print("Digite ano de nascimento")
    anonasc = int(input())
    if re.search("\d{4}", str(anonasc)):
        erro = "Ano de nascimento inválido (formato: 0000)"
        raise ValueError
    
    cliente = {
        "nome": nome,
        "cep": cep,
        "ano_nascimento": anonasc
    }

    idade = 2023 - cliente["ano_nasc"]
    if idade < 18:
        print(f"{cliente['nome']} : não é permitida a venda para menores de idade")
    else :
        print("Escolha um dos vinhos da lista:")
        for i in range(1, len(vinhos)+1, 1):
            if vinhos["vinho"+str(i)]["estoque"] > 0:
                print(f"({i}) {vinhos['vinho'+str(i)]['nome']['valor']:.1f}")
        vinho = int(input())
        print("Quantidade de vinho?")
        qtde = int(input())
        if "vinho"+str(vinho) in vinhos:
            #verificando se há quantidade suficiente deste vinho
            estoque = vinhos['vinho'+str(vinho)]['estoque']
            if estoque > 0 and qtde <= estoque:
                #atualizando o estoque
                novo_estoque = estoque - qtde
                vinhos['vinho'+str(vinho)]['estoque'] = novo_estoque 
                #registrando a compra no List
                compra = []
                compra.append(vinhos['vinho'+str(vinho)]['nome'])
                compra.append(vinhos['vinho'+str(vinho)]['valor'])
                compra.append(qtde)
                compra.append(vinhos['vinho'+str(vinho)]['nome']*qtde)
            else:
                print("Quantidade informada excede estoque")
        else:
            print("Opção inválida da lista de vinhos")
        #exibindo dados da compra
        print(":"*70)
        print(f"{nome}, foi um prazer atendê=lo")
        msg = "Tipo do vinho \t\t preço \t qtde \t subtotal \n"
        for i in compra :
            msg += str(i) + " \t "
        print(msg)
        print(":"*70)
        #exibindo o estoque 
        print("Nosso estoque ficou:")
        for i in range(1, len(vinhos)+1, 1):
            vinho = vinhos['vinho'+str(vinho)]['nome']
            valor = vinhos['vinho'+str(vinho)]['valor']
            estoque = vinhos['vinho'+str(vinho)]['estoque']
            print(f"Vinho: {vinho} \t Preço: R$ {valor:.1f} Estoque: {estoque}")
        print(":"*70)
except ValueError :
    print(erro)