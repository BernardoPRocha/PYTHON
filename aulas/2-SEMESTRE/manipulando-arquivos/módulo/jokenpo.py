import random

def sortear_jogada_computador():
    jogadas = ["pedra", "papel", "tesoura"]
    jogada_computador = random.choice(jogadas)
    return jogada_computador
