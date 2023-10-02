from jokenpo import sortear_jogada_computador

def verificar_vencedor(jogada_usuario, jogada_computador):
    if jogada_usuario == jogada_computador:
        return "Empate"
    elif (jogada_usuario == "pedra" and jogada_computador == "tesoura") or \
         (jogada_usuario == "papel" and jogada_computador == "pedra") or \
         (jogada_usuario == "tesoura" and jogada_computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

print("Bem-vindo ao jogo Jokenpo!")

jogada_usuario = input("Escolha sua jogada (pedra, papel ou tesoura): ").lower()

if jogada_usuario not in ["pedra", "papel", "tesoura"]:
    print("Jogada inválida. Escolha entre pedra, papel ou tesoura.")
else:
    jogada_computador = sortear_jogada_computador()
    print(f"O computador escolheu: {jogada_computador}")
    
    resultado = verificar_vencedor(jogada_usuario, jogada_computador)
    print(resultado)
