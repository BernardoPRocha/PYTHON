somapeso = gordo = 0
while somapeso <= 100000:
    print("Digite o peso do hipopótamo")
    peso = float(input())
    if peso > gordo :
        gordo = peso
        somapeso += peso
print(f" O maior peso é {gordo}")