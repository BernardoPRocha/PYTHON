def divisao(n1, n2):
    result = n1 / n2
    return result

print("Digite dois numeros inteiros")
num1 = int(input())

num2 = int(input())

resultado = divisao(num1, num2)
print(f"A divisão é: {resultado:.2f}")
