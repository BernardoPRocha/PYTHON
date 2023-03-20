print("Qual o seu salário")
sal = float(input())
print("Há quantos anos você trabalha")
tempo = int(input())
if tempo < 5 :
    print(sal * 1.05)
elif tempo <= 10 :
    print(sal * 1.10)
elif tempo <= 15 :
    print(sal * 1.15)
else :
    print(sal * 1.20)

