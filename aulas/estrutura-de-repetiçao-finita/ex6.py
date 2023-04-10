fat = 1
num = 0
print("Digite um numero inteiro")
num = int(input())
for i in range(num,1,-1):
    fat *= i 
    #fat = fat * i
print ("O fatorial de",num,"é",fat)