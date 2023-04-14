import random
winPC = 0
winJG = 0
resposta = ""
while resposta != "não":
    print("Escolha: \npedra\npapel\ntesoura")
    jg = input()
    sorteio = random.randint(1,3)
    match sorteio:
        case 1:
            pc = "pedra"
        case 2:
            pc = "papel"
        case 3:
            pc = "tesoura"

    d1 = (jg == "papel") and (pc == "tesoura")
    d2 = (jg == "pedra") and (pc == "papel")
    d3 = (jg == "tesoura") and (pc == "pedra")
    df = d1 or d2 or d3
    #verificações
    if jg == pc:
        print(f"Empate\nVocê: {jg}\nPC: {pc}")
    elif df:
        print(f"Derrota\nVocê: {jg}\nPC: {pc}")
        winPC += 1
    else :
        print(f"Vitória\nVocê: {jg}\nPC: {pc}")
        winJG += 1
    print("Você quer jogar ainda")
    resposta = str(input())
print(f"Jogador:{winJG} , PC:{winPC}")