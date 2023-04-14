pesoTotal = 0 
print("Digite o peso de um hipopótamo")
peso = float(input())
while pesoTotal < 100000:
    pesoTotal += float(peso)
    print("Digite um peso")
    peso = float(input())
print(f" Nossa :{pesoTotal}")