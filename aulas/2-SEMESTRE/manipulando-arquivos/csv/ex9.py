import csv

def cadastrar_filme():
    titulo = input("Título do filme: ")
    genero = input("Gênero: ")
    duracao = input("Duração (em minutos): ")
    censura = input("Censura: ")
    diretor = input("Diretor: ")
    
    return [titulo, genero, duracao, censura, diretor]

nome_arquivo = "d:/filmes.csv"

with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Título", "Gênero", "Duração", "Censura", "Diretor"])

    while True:
        filme = cadastrar_filme()

        escritor.writerow(filme)
        
        continuar = input("Deseja cadastrar outro filme? (s/n): ")
        if continuar.lower() != 's':
            break

print("Filmes cadastrados com sucesso!")

