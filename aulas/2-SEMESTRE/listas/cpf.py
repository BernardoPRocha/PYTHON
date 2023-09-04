import re

def validar_cpf_formato(cpf):
    padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    if re.match(padrao, cpf):
        return True
    else:
        return False

def validar_cpf(cpf):
    cpf = re.sub('[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    digito_verificador1 = sum(int(cpf[i]) * (10 - i) for i in range(9)) % 11
    digito_verificador2 = sum(int(cpf[i]) * (11 - i) for i in range(10)) % 11

    if digito_verificador1 == int(cpf[9]) and digito_verificador2 == int(cpf[10]):
        return True
    else:
        return False

cpf = input("Digite o CPF (no formato 000.000.000-00): ")

if validar_cpf_formato(cpf):
    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")
else:
    print("CPF no formato incorreto!")
