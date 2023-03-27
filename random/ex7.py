import random
print("Escolha: \npedra\npapel\ntesoura\nlagarto\nspock")
print("-=" * 11)
jg = input()
sorteio = random.randint(1,3)
match sorteio:
    case 1:
        pc = "pedra"
    case 2:
        pc = "papel"
    case 3:
        pc = "tesoura"
    case 4:
        pc = "lagarto"
    case 5:
        pc = "spock"
print("-=" * 11)
d1 = (jg == "papel") and (pc == "tesoura")
d2 = (jg == "papel") and (pc == "lagarto")
d3 = (jg == "pedra") and (pc == "papel")
d4 = (jg == "pedra") and (pc == "spock")
d5 = (jg == "tesoura") and (pc == "pedra")
d6 = (jg == "tesoura") and (pc == "spock")
d7 = (jg == "lagarto") and (pc == "tesoura")
d8 = (jg == "lagarto") and (pc == "pedra")
d9 = (jg == "spock") and (pc == "lagarto")
d10 = (jg == "spock") and (pc == "papel")
df = d1 or d2 or d3 or d4 or d5 or d6 or d7 or d8 or d9 or d10
#verificações
if jg == pc:
    print(f"Empate\nVocê: {jg}\nPC: {pc}")
elif df:
    print(f"Derrota\nVocê: {jg}\nPC: {pc}")
else :
    print(f"Vitória\nVocê: {jg}\nPC: {pc}")