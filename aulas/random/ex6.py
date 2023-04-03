print("Digite o valor de I")
I = int(input())
print("Digite valores para A, B, C")
A = float(input())
B = float(input())  
C = float(input())
match I:
    case 1:
        print("Área do quadrado:", A * A)
    case 2:
        print("Área do retângulo:", A * B)
    case 3:
        print("Àrea do triangulo:", A * B / 2)
    case 4:
        print("Àrea do trapézio:", (A * B) * C / 2)
    case _:
        print("Valor inválido de I")
