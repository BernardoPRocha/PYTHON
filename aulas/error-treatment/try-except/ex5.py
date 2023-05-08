import re
frase = "Quem ri por ultimo ri melhor"
print(re.findall("ri", frase))
print(re.findall("chora", frase))
busca = re.search("ultimo", frase)
print(busca)
print(busca.start())
print(busca.end())
print(re.search("segundo", frase))
print(re.split("\s", frase))
print(re.split("\s", frase, 2))
print(re.sub("ri", "chora", frase))
print(re.sub("ri", "chora", frase, 1))