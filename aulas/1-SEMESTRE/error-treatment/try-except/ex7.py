import re
try:
    print("Digite seu nome")
    nome = input()
    if re.search("\d", nome):
        raise ValueError
    print("Digite o seu telefone. (com DDD)")
    telefone = input()
    if not re.search("\d", telefone):
        erro = "Somente numeros"
        raise ValueError
except ValueError:
    print("erro")

    
        
    
