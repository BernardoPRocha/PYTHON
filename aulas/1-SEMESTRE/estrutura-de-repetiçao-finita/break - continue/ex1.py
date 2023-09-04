senha = ""
frase = "Acesso Concedido!"
cont = 0
while senha != "p4ssw0rd":
    print("Digite a sua senha")
    senha = str(input())
    cont += 1
    if cont >= 5:
        frase = "Conta Bloquada!"
        break
print(frase)