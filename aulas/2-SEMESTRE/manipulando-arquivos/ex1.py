try:
    f = open('d:/tigres.txt','w')
    f.write("Um prato de trigo")
    f.write("\npara três tigres tristes")
    f.close

    f = open('d:/tigres.txt','r')
    print(f.read())
    f.close
except FileNotFoundError:
    print('Arquivo não encontrado')