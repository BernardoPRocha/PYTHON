frutas = ["maça","banana","uva"]
print(frutas)
print(frutas[2])
print(len(frutas))
frutas.append("cereja")
frutas.append("acerola")
print(frutas)
print(len(frutas))
print(frutas[-1])
print(frutas[2:5])
print(frutas[:4])
print(frutas[3:])
print(frutas[-4:-1])
frutas[1] = "manga"
print(frutas)
frutas[1:3] = ["morango","caqui"]
print(frutas)
frutas.insert(1,"melancia")
print(frutas)
citricos = ["limão", "laranja"]
frutas.extend(citricos)
print(frutas)
frutas.remove("acerola")
print(frutas)
frutas.pop(3)
print(frutas)
frutas.pop()
print(frutas)
print("--------------------")
for i in frutas:
    print(i)
print("--------------------")
for i in range(len(frutas)):
    print(frutas[i])
frutas.sort()
print(frutas)
numeros = [50,10,30,40,15,60,20]
numeros.sort()
print(numeros)