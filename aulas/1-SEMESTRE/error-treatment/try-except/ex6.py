import re
erro = ""
try:
    print("Digite seu nome")
    nome = input()
    if re.search("\d", nome):
        erro = "Nome não pode conter números"
        raise ValueError
    print("Digite seu CEP (Somente Digitos)")
    cep = input()
    if not re.search("\d(8)", cep) or len(cep) > 8:
        erro = "CEP inválido"
        raise ValueError
except ValueError:
    print("Apenas letras ou numeros")
finally:
    print("Final")