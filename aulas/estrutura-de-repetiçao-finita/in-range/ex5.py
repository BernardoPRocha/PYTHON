soma = nota = 0.0
for i in range (1,31,1):
    print ("Digite uma nota")
    nota = float(input())
    #soma = soma + nota
    soma += nota
print("A média das notas é:", soma/30)