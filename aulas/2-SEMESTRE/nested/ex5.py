#RM99209
import random

# Gerar uma matriz 5x5 de números reais aleatórios entre 10 e 20
matriz = [[random.uniform(10, 20) for _ in range(5)] for _ in range(5)]

# Imprimir a matriz
print("Matriz 5x5 gerada:")
for linha in matriz:
    print(linha)

# Calcular a soma dos valores nas posições indicadas
somas_posicoes = 0
for i in range(5):
    for j in range(i + 1, 5):
        soma = matriz[i][j]
        somas_posicoes += soma

# Calcular a soma dos valores nas posições opostas
somas_opostas = 0
for i in range(1, 5):
    for j in range(i):
        soma = matriz[i][j]
        somas_opostas += soma

# Imprimir os resultados
print("\nSoma dos valores nas posições indicadas:")
print(somas_posicoes)
print("\nSoma dos valores nas posições opostas:")
print(somas_opostas)

