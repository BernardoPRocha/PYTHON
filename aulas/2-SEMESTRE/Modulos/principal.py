import area
print("Escolha qual área deseja calcular")
print("(1) Retângulo")
print("(2) Triangulo")
print("(3) Círculo")
escolha = int(input("Número da escolha: "))
if escolha == 1:
    lado = float(input("Digite valor de lado: "))
    altura = float(input("Digite o valor da altura: "))
    resultado = area.area_retangulo(lado, altura)
    print("Área do retangulo: {:.2f}".format(resultado))
elif escolha == 2:
    lado = float(input("Digite valor do lado: "))
    altura = float(input("Digite o valor da altura"))
    resultado = area.area_triangulo(lado, altura)
    print("Área do triangulo: {:.2f}".format(resultado))
elif escolha == 3:
    raio = float(input("Digite o valor do raio: "))
    resultado = area.area_circulo(raio)
    print("Área do círculo: {:.2f}".format(resultado))
else: 
    print("Opção de escolha invalida")