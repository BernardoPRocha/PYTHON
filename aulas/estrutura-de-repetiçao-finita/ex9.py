num = 0
penultimo = ultimo = 1
print("Digite um número inteiro")
num = int(input())
frase = str(penultimo) + " " + str(ultimo) + " "
for i in range(2,num,1):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo 
    frase += str(termo) + " "
print(frase)
   

