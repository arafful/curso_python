"""
Tipos string estão sempre limitados entre aspas simples ou duplas
"""

simples = 'Estou entre aspas simples'

duplas = "Entre aspas duplas e também sou string"

print("Simples: ", simples, " -> ", type(simples))
print("Duplas:  ", duplas, " -> ", type(duplas))

name = "Bell's galery"
citacao = '"Bela bosta" - André Rafful'

print(name)
print(citacao)

endereco = ("Rua Teófilo Braga, 170")
cep = "13057"
print(endereco, type(endereco))
print(cep, type(cep))
