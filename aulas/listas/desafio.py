def imprimeBoneco(erros):
    if erros == 5:
        print("----------")
        print("l         www")
        print("l        d-.-b")
        print("l        (---)")
        print("l      o=l   l=o")
        print("l         U U")
        print("l")

    elif erros == 4:
        print("----------")
        print("l         www")
        print("l        d-.-b")
        print("l        (---)")
        print("l      o=l   l=o")
        print("l")
        print("l")

    elif erros == 3:
        print("----------")
        print("l         www")
        print("l        d-.-b")
        print("l        (---)")
        print("l")
        print("l")
        print("l")

    elif erros == 2:
        print("----------")
        print("l         www")
        print("l        d-.-b")
        print("l")
        print("l")
        print("l")
        print("l")

    elif erros == 1:
        print("----------")
        print("l         www")
        print("l")
        print("l")
        print("l")
        print("l")
        print("l")


import random 
sorteioPalavra = random.randint(1,3)
match sorteioPalavra:
    case 1:
        palavra = "esperança"
        frase = "É a última que morre"
    case 2:
        palavra = "nostalgia"
        frase = "Sensação de passado"
    case 3:
        palavra = "ancestral"
        frase = "Aquele que morreu"

