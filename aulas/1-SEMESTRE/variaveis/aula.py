print("Escolha sua bebida para o cafe da manha")
bebida = input()
match bebida.lower() :
    case "cafe":
        print("O cafe da manha é um café")
    case "leite":
        print("O cafe da manha é um leite")
    case "suco":
        print("O cafe da manha é um suco")
    case "cha":
        print("O cafe da manha é um chá")
    case other:
        print("Escolha sua bebida para o cafe da tarde")
