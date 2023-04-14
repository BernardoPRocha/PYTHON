cont = 0 
print("Digite um número")
num = int(input())
while num != 0:
    print("Digite um número")
    num = int(input())
    cont += 1 #cont = cont + 1
print(f"Quantidade de números digitados {cont}")