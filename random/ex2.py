from random import randint 
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("Suas opções: ( 0 ) Pedra ( 1 ) Papel ( 2 ) Tesoura ")
jogador = int(input("Qual a sua jogada? "))
print("-=" * 11)
print("Computador jogou {}" .format(itens[computador]))
print("Jogador jogou {}" .format(itens[jogador]))
print("-=" * 11)

if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador venceu")
    elif jogador == 2:
        print("Computador venceu")

elif computador == 1:
    if jogador == 0:
        print("Computador venceu")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador venceu")

elif computador == 2:
    if jogador == 0:   
        print("Jogador venceu")
    elif jogador == 1:
        print("Computador venceu")
    elif jogador == 2:  
        print("Empate")
    