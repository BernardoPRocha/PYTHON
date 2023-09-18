import csv

# Função para buscar e exibir filmes com base na escolha do usuário
def buscar_filmes_por_opcao(escolha, valor):
    with open("d:/filmes.csv", 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        encontrados = []
        
        for linha in leitor:
            if linha[escolha].strip() == valor:
                encontrados.append(linha)
        
        if encontrados:
            print(f"Filmes com {escolha} igual a '{valor}':")
            for filme in encontrados:
                print(f"Título: {filme['Título']}")
                print(f"Gênero: {filme['Gênero']}")
                print(f"Duração: {filme['Duração']}")
                print(f"Censura: {filme['Censura']}")
                print(f"Diretor: {filme['Diretor']}")
                print()
        else:
            print(f"Nenhum filme com {escolha} igual a '{valor}' foi encontrado.")

# Menu de opções
while True:
    print("Escolha uma opção:")
    print("1. Buscar por Título")
    print("2. Buscar por Diretor")
    print("3. Buscar por Gênero")
    print("4. Sair")
    
    opcao = input("Opção: ")
    
    if opcao == '1':
        titulo = input("Digite o título do filme: ")
        buscar_filmes_por_opcao('Título', titulo)
    elif opcao == '2':
        diretor = input("Digite o nome do diretor: ")
        buscar_filmes_por_opcao('Diretor', diretor)
    elif opcao == '3':
        genero = input("Digite o gênero do filme: ")
        buscar_filmes_por_opcao('Gênero', genero)
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
