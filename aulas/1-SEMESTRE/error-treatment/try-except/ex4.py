try :
    print("Digite 2 numeros inteiros")
    num1 = int(input())
    if not type(num1) is int:
        raise ValueError
    num2 = int(input())
    if not type(num2) is int:
        raise ValueError
    if num2 <= 0:
        raise ZeroDivisionError
    print(f"Divisão: {num1 // num2}")
except ValueError:
    print("Erro: Somente números inteiros são permitidos")
except ZeroDivisionError:
    print("Erro: Segundo número deve ser maior que zero")
finally: 
    print("Obrigado por utilizar o nosso programa. Volte em breve!")