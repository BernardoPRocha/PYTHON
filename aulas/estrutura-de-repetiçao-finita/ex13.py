cont = 0 
print("Digite o comprimento das asas de um pelicano em cm")
num = float(input())
while num != 0:
    cont += num #cont = cont + num
    print("Digite um comprimento")
    num = float(input())
print(f"Tamanho das asas em cm: {cont}")