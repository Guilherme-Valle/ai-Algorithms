# Passos:
# 1) transformar sentenças para sentenças python
# 2) substituir as variaveis da base por true, e as que não são da base por false
# 3) roda eval na sentença com as variaveis substituidas

def gera_base_de_conhecimento(variavel_verdadeira):
    for chave, regra in regras.items():
        regras[chave] = regra.replace(variavel_verdadeira, 'True')


def verifica_variavel_verdadeira(variavel):
    return 2


regras = {}

# lista de variaveis TODO preencher
variaveis = []
numero_de_regras = int(input().rstrip())
print(numero_de_regras)
for i in range(numero_de_regras):
    regra = input().rstrip().split('=>')
    variaveis.append(regra[0].split('^'))
    variaveis.append(regra[0].split('|'))
    regras[regra[1].strip()] = regra[0].strip().replace('^', "and").replace('|', "or")

base = input().rstrip().split(',')
for item in base:
    gera_base_de_conhecimento(item)

consulta = input().rstrip()

print(variaveis)
