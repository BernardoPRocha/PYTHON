#RM99209
ditado = input("Digite um ditado popular: ")
nome_arquivo = "ditado_popular.txt"
with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write("\n" + ditado)
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
print(f"Conteúdo do arquivo {nome_arquivo}:\n{conteudo}")
