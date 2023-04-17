preço = 0
valorPago = 0
troco = 0
print("Digite o valor da compra")
preço = float(input())
print("Digite o valor pago")
valorPago = float(input())
troco = valorPago - preço
if preço == valorPago:
    print("O valor da compra é igual ao valor pago")
else:
    print(f"O troco é de R${troco}")
