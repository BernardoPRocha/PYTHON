dicionario = {
    "montadora":"Ford",
    "modelo":"Mustang",
    "ano":2000,
    }

print(dicionario)
print(len(dicionario))
print(dicionario["modelo"])
print(dicionario.get("modelo"))
print(dicionario.keys())
print(dicionario.values())
dicionario["ano"] = 1994
print(dicionario)
dicionario.update({"ano":2023,"modelo":"Ferrari"})
print(dicionario)
dicionario["cor"] = "vermelho"
print(dicionario)

# dicionario2 = dict(montadora = "Ford", modelo = "Mustang", ano = 1964, ano = 2000) 

# print(dicionario2)
# print(len(dicionario2))
# print(dicionario2["modelo"])
# print(dicionario2.get("modelo"))
# print(dicionario2.keys())
# print(dicionario2.values())

#Nested Dictionary (Dicionário Aninhado)
clientes = {
    "cliente1" : {"nome":"Astrogildo","ano":1998},
    "cliente2" : {"nome":"Berisvaldo","ano":1999},
    "cliente3" : {"nome":"Gumercindo","ano":2000}
}
print(clientes)
print(len(clientes["cliente2"]))

