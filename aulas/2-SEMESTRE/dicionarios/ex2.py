carta = {
    "KI":7400,
    "TÉCNICAS":6000,
    "VELOCIDADE":66,
    "TRANSFORMAÇÕES":3,
}
print(f"Essas são as características da carta:{carta}")
print("Escolha uma nova característa.")
caracNova = str.upper(input())
print("Agora escolha um valor para essa característica")
valor = int(input())
carta[f"{caracNova}"] = valor
print(f"Escolha entre uma dessas opções: {carta.keys()}")
carac = str.upper(input())
if carac == "KI" :
    print(f"A quantidade de KI é {carta['KI']}")
elif carac == "TECNICAS" :
    print(f"A quantidade de TÉCNICAS é {carta['TECNICAS']}")
elif carac == "VELOCIDADE" :
    print(f"A quantidade de VELOCIDADE é {carta['VELOCIDADE']}")
elif carac == "TRANSFORMAÇÕES" :
    print(f"A quantidade de TRANSFORMAÇÕES é {carta['TRANSFORMAÇÕES']}")
elif carac == caracNova :
    print(f"A quantidade de {caracNova} é {valor}")
else :
    print("Essa característica não existe.")