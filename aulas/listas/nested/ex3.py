matriz = []
qtdelin = 5
qtdecol = 2
for i in range(0, qtdelin, 1):
    linha = []
    for j in range(0, qtdecol, 1):
        valor = input(f"Digite primeiro o seu nome e depois o estado onde nasceu [{i}] [{j}]")
        linha.append(valor)
    matriz.append(linha[:])
print(matriz)
print("Escolha um estado brasileiro")
estado = input().lower()
for i in range(0, len(matriz), 1):
    if estado == matriz[i][1]:
        print(f"Nome: {matriz[i][0]}")