#RM99209
import random

# Gerar uma matriz 5x5 de números inteiros aleatórios entre 10 e 30
matriz = [[random.randint(10, 30) for _ in range(5)] for _ in range(5)]

# Imprimir a matriz
print("Matriz 5x5 gerada:")
for linha in matriz:
    print(linha)

# Calcular a soma da linha 4
soma_linha_4 = sum(matriz[3])

# Calcular a soma da coluna 2
soma_coluna_2 = sum(matriz[i][1] for i in range(5))

# Calcular a soma da diagonal principal
soma_diagonal_principal = sum(matriz[i][i] for i in range(5))

# Calcular a soma da diagonal secundária
soma_diagonal_secundaria = sum(matriz[i][4 - i] for i in range(5))

# Calcular a soma de todos os valores da matriz
soma_total = sum(sum(matriz[i]) for i in range(5))

# Imprimir os resultados
print("\nResultados:")
print(f"Soma da linha 4: {soma_linha_4}")
print(f"Soma da coluna 2: {soma_coluna_2}")
print(f"Soma da diagonal principal: {soma_diagonal_principal}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")
print(f"Soma de todos os valores da matriz: {soma_total}")
