import csv
novos_dados = [
    ['Tibúrcio','tiby','senha','23','13513513500'],
    ['Otto','otto','otto','88','01102203300']
]

with open('d:/usuarios.csv', 'a', encoding='utf-8', newline='') as f:
    escreve_csv = csv.writer(f)
    for i in novos_dados:
        escreve_csv.writerow(i)