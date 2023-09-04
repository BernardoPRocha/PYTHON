#Bernardo Rocha RM99209
num = {0}
maiorNum = None
print("Digite um tipo numérico entre real ou inteiro")
tipoNum = str(input())
if tipoNum.lower() == "real":
    num.clear()
    while len(num) < 10:  
        print("Digite um numero real")
        numDigitado = input()
        num.add(numDigitado)
        if maiorNum is None or numDigitado > maiorNum:
            maiorNum = numDigitado
elif tipoNum.lower() == "inteiro":
    num.clear()
    while len(num) < 10:
        print("Digite um numero inteiro")
        numDigitado = int(input())
        num.add(numDigitado)
        if maiorNum is None or numDigitado > maiorNum:
            maiorNum = numDigitado
print(f"Você escolheu {tipoNum}, seu maior número foi {maiorNum},\n seus numeros foram {num} e a quantidade de números digitados foram {len(num)} ")
