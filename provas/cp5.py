import random


with open('roda.txt', 'w') as roda_file:
    roda_file.write("100\n200\n300\n400\n500\n600\n700\n800\n900\n1000\nPerdeu a vez")


with open('palavras.csv', 'w') as palavras_file:
    palavras_file.write("ELEFANTE,GIRAFA,CROCODILO")

jogadores = []
pontuacoes = []


for i in range(3):
    nome = input(f"Digite o nome do jogador {i + 1}: ")
    jogadores.append(nome)
    pontuacoes.append(0)

letras_acertadas = []
letras_palpite = []
letras_faltando = []

palavras = ["ELEFANTE", "GIRAFA", "CROCODILO"]

for palavra in palavras:
    letras_faltando.extend(list(set(palavra) - set(letras_faltando)))

rodada = 0

while letras_faltando:
    jogador_atual = rodada % 3
    print(f"\nÉ a vez de {jogadores[jogador_atual]}")

    input("Pressione Enter para rodar a roda...")

    opcoes_roda = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "Perdeu a vez"]


    if not opcoes_roda:
        print("Todas as opções da roda foram escolhidas. O jogo terminou.")
        break

    opcao_roda_descricao = random.choice(opcoes_roda)

    print(f"A roda parou em: {opcao_roda_descricao}")

    if opcao_roda_descricao == 'Perdeu a vez':
        print("Que pena! Você perdeu a vez.")
    elif opcao_roda_descricao == '1000':
        print("Parabéns! Você ganhou 1000 pontos.")
        pontuacoes[jogador_atual] += 1000
    else:
        opcao_roda_pontuacao = int(opcao_roda_descricao)
        letra = input("Escolha uma letra: ").upper()

        if letra in letras_acertadas:
            print("Essa letra já foi escolhida antes.")
        elif letra in letras_faltando:
            letras_acertadas.append(letra)
            letras_palpite.append(letra)
            pontuacao_roda = letras_palpite.count(letra) * opcao_roda_pontuacao
            pontuacoes[jogador_atual] += pontuacao_roda
            print(f"A letra '{letra}' aparece na(s) palavra(s)!")
            letras_faltando = list(set(letras_faltando) - set([letra]))
        else:
            print(f"A letra '{letra}' não aparece na(s) palavra(s).")
            letras_palpite.append(letra)

    for palavra in palavras:
        palavra_mostrada = ""
        for letra in palavra:
            if letra in letras_acertadas:
                palavra_mostrada += letra
            else:
                palavra_mostrada += "_"
        print(f"Palavra : {palavra_mostrada}")

    if len(letras_faltando) <= 3:
        palpite = input("Faltam apenas 3 letras! Dê seu palpite das palavras use vírgula para separar as palavras: ").upper()
        if palpite == ",".join(palavras):
            print(f"Parabéns, {jogadores[jogador_atual]}! Você acertou as palavras e ganhou {sum(pontuacoes)} pontos.")
            break
        else:
            print(f"Que pena, {jogadores[jogador_atual]}! Seu palpite estava errado, você perdeu todos os pontos.")
            pontuacoes[jogador_atual] = 0

    print("\nLetras escolhidas: ", ', '.join(letras_palpite))
    for i in range(3):
        print(f"{jogadores[i]}: {pontuacoes[i]} pontos")

    rodada += 1

print("Fim do jogo!")
