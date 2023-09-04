#RM99209
numeros = set()
while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))
    if numero == 0:
        break
    numeros.add(numero)
numeros_pares = {numero for numero in numeros if numero % 2 == 0}
nome_arquivo = "numeros_pares.txt"
with open(nome_arquivo, 'w') as arquivo:
    for numero in numeros_pares:
        arquivo.write(str(numero) + '\n')
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
print(f"Conteúdo do arquivo {nome_arquivo} (números pares):\n{conteudo}")
