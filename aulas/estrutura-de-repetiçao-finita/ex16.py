I = 0
A = 0
B = 0
C = 0 
print("Digite o valor de I")
I = int(input())
print("Digite o valor de A")
A = float(input())
print("Digite o valor de B")
B = float(input())
print("Digite o valor de C")
C = float(input())
lista = (A, B , C)
crescente = sorted(lista)
decrescente = sorted(lista, reverse=True)
meio = (max)
match I:
    case 1:
        print(crescente)
    case 2:
        print(decrescente)
    case 3:
        print(meio)