import csv
with open('d:/usuarios.csv', 'r', encoding='utf-8') as f:
    usuarios = csv.reader(f)
    next(usuarios)
    for i in usuarios:
        if i[3] == '18':
            print(i[0])