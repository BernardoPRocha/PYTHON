cont = 0
while True:
    try:
        print("Digite valor de QI")
        print("ou para 0 encerrar")
        QI = int(input())
        if QI == 0:
            break
        if QI < 140:
            continue
        cont += 1
    except ValueError:
        print("Erro! Apenas números inteiros")
print(f"Quantidade de gênios {cont}")