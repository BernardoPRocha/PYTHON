print("Qual a quantidade de pessoas")
pessoas = int(input())
print("Quantas tulipas foram consumidas")
tulipa = int(input())
print("Quantas pizzas foram consumidas")
pizzas = int(input())
print("Total cobertura das pizzas")
coberturas = int(input())
conta = ((tulipa * 19.8) + (pizzas * 49) + (coberturas * 2.5)) * 1.1
pagamento = conta / pessoas 
print(f"O valor da conta é de R${conta:.2f}")
print(f"Cada um deve pagar: {pagamento:.2f}")