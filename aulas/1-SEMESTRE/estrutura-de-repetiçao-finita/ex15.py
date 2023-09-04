valor_a_pagar = float(input("Digite o valor a ser pago: "))
valor_pago = float(input("Digite o valor efetivamente pago: "))

troco = valor_pago - valor_a_pagar
print(troco)

if troco < 0:
    print("Valor pago é menor que o valor a ser pago!")
else:
    notas50 = int(troco / 50)
    troco = troco % 50

    notas20 = int(troco / 20)
    troco = troco % 20

    notas10 = int(troco / 10)
    troco = troco % 10

    notas5 = int(troco / 5)
    troco = troco % 5

    moedas1 = int(troco)

    print(f"Notas de 50 reais: {notas50}")
    print(f"Notas de 20 reais: {notas20}")
    print(f"Notas de 10 reais: {notas10}")
    print(f"Notas de 5 reais: {notas5}")
    print(f"Moedas de 1 real: {moedas1}")
