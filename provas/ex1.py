#Bernardo Rocha RM99209
#Kaylane Neves RM98919
#Kevin Beykam RM550154
import random
#Escolhendo o nome do computador
sorteioNome = random.randint(1,3)
match sorteioNome:
    case 1:
        pc = "Kaylane"
    case 2:
        pc = "Kevin"
    case 3:
        pc = "Bernardo"
#Sorteando o número do computador
sorteioNum = 0 
sorteioNum = random.randint(1,5)
#Perguntando as opções do jogador
print("Digite o seu nome")
nomeJogador = str(input())
print("Escolha entre PAR ou ÍMPAR")
escolha = str(input())
print("Escolha um número entre 1 a 5")
numero = int(input())
#Decidindo a jogada do computador
if escolha == "PAR":
    escolhaPC = "ÍMPAR"
else:
    escolhaPC = "PAR"
#Escrevendo as respostas dos jogadores
print("Você",nomeJogador)
print("Seu oponente:",pc)
print("Você escolheu",escolha, "e o número", numero)
print("O", pc, "escolheu", escolhaPC, "e o número", sorteioNum)
total = numero + sorteioNum
print("O total deu:", total)
#Conta para decidir se o número é par ou ímpar
resto = total % 2
#Código para decidir se o jogador perdeu ou ganhou
if escolha == "PAR":
    if resto == 0 :
        print("Você Ganhou!!!")
    else: 
        print("Você Perdeu!!!")
elif escolha == "ÍMPAR":
    if resto == 0 :
        print("Você Perdeu!!!")
    else :
        print("Você Ganhou!!!")