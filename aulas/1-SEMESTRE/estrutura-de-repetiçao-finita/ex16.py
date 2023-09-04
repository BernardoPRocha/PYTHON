i = int(input("Digite o valor de I: "))
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

print(f"Valores lidos: I={i}, A={a}, B={b}, C={c}")

if i == 1:
    # ordem crescente
    lista = [a, b, c]
    lista.sort()
    print(f"Ordem crescente: {lista}")
elif i == 2:
    # ordem decrescente
    lista = [a, b, c]
    lista.sort(reverse=True)
    print(f"Ordem decrescente: {lista}")
elif i == 3:
    # maior valor entre os outros dois
    if a > b and a > c:
        if b > c:
            print(f"Ordem: {b}, {a}, {c}")
        else:
            print(f"Ordem: {c}, {a}, {b}")
    elif b > a and b > c:
        if a > c:
            print(f"Ordem: {c}, {b}, {a}")
        else:
            print(f"Ordem: {a}, {b}, {c}")
    elif c > a and c > b:
        if a > b:
            print(f"Ordem: {b}, {c}, {a}")
        else:
            print(f"Ordem: {a}, {c}, {b}")
else:
    print("Valor de I inválido.")

    