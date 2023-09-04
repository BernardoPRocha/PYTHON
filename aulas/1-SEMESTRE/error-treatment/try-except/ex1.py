try:
    print("Digite 2 números inteiros")
    num1 = int(input())
    num2 = int(input())
    print(f"Adição: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")
    try : 
        print(f"Divisão: {num1 // num2}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    print(f"Multiplicação: {num1 * num2}")
except ValueError:
    print("Somente números inteiros são aceitos")