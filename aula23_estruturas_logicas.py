"""
ESTRUTURAS LÓGICAS EM PYTHON

AND, OR, NOT, IS
"""
ativo = True
logado = False

if ativo and logado:
    print("Bem vindo usuário")
elif not ativo and not logado:
    print("usuário não cadastrado")
elif not ativo:
    print("ative seu usuário")
elif not logado:
    print("Faça login")



