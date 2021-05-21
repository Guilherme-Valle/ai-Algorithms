import math
# Dicionario a ser utilizado no algoritmo
dicionario_atributos = {}

numero_de_registros, numero_de_atributos = input().rstrip().split(' ')
numero_de_registros = int(numero_de_registros)
numero_de_atributos = int(numero_de_atributos)
total_casos_0 = 0
total_casos_1 = 0

for i in range(numero_de_registros):
    atributos = input().rstrip().split(' ')
    dicionario_atributos[i] = {}
    # Faz a totalização do número de registros com as classes 0 ou 1 para utilizar no cálculo
    if int(atributos[numero_de_atributos-1]) == 1:
        total_casos_1 += 1
    else:
        total_casos_0 += 1
    for z in range(numero_de_atributos):
        dicionario_atributos[i][z] = int(atributos[z])

def calcula_entropia(proporcao1, proporcao0):
            log0 = 0 if proporcao0 == 0 else math.log2(proporcao0)
            log1 = 0 if proporcao1 == 0 else math.log2(proporcao1)
            return (-proporcao1 * log1) - (proporcao0 * log0)


def ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(x, y, z):
    ocorrencias = 0
    for i in range(numero_de_registros):
        if dicionario_atributos[i][x] == y and dicionario_atributos[i][numero_de_atributos-1] == z:
            ocorrencias += 1

    return ocorrencias


def ocorrencias_de_atributo_x_igual_a_y(x, y):
    ocorrencias = 0
    for i in range(numero_de_registros):
        if dicionario_atributos[i][x] == y:
            ocorrencias += 1

    return ocorrencias

def verifica_se_todos_os_registros_dao_x(lista, x):
    for i in enumerate(lista):
        if dicionario_atributos[i[1]][numero_de_atributos-1] != x:
            return False
    return True


def registros_onde_atributo_x_igual_a_y(x, y):
    lista = []
    for i in range(numero_de_registros):
        if dicionario_atributos[i][x] == y:
            lista.append(i)
    return lista

def retorna_maior_ganho():
    ganhos_de_informacao = {}
    for indice in range(numero_de_atributos - 1):
        ocorrencias_fraco = ocorrencias_de_atributo_x_igual_a_y(indice, 0) / numero_de_registros
        ocorrencias_fraco *= calcula_entropia(
            ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(indice, 0, 1) / numero_de_registros,
            ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(indice, 0, 0) / numero_de_registros)
        ocorrencias_forte = ocorrencias_de_atributo_x_igual_a_y(indice, 1) / numero_de_registros
        ocorrencias_forte *= calcula_entropia(
            ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(indice, 1, 1) / numero_de_registros,
            ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(indice, 1, 0) / numero_de_registros)
        ganhos_de_informacao[indice] = entropia_geral - (ocorrencias_forte + ocorrencias_fraco)
    maior_ganho = {'atributo': 0, 'valor': ganhos_de_informacao[0]}
    for indice in range(numero_de_atributos - 1):
        if ganhos_de_informacao[indice] > maior_ganho['valor']:
            maior_ganho['atributo'] = indice
            maior_ganho['valor'] = ganhos_de_informacao[indice]
    return maior_ganho


entropia_geral = calcula_entropia(total_casos_1/numero_de_registros, total_casos_0/numero_de_registros)
caso_de_teste = input().rstrip().split(' ')

primeiro_maior_ganho = retorna_maior_ganho()

arvore_de_decisao = {primeiro_maior_ganho['atributo']: {
    '0': registros_onde_atributo_x_igual_a_y(primeiro_maior_ganho['atributo'], 0),
    '1': registros_onde_atributo_x_igual_a_y(primeiro_maior_ganho['atributo'], 1)
}}



if caso_de_teste[primeiro_maior_ganho['atributo']] == 0:
    if verifica_se_todos_os_registros_dao_x(arvore_de_decisao[primeiro_maior_ganho['atributo']]['0'], 0):
        print(0)
    else:
        print(1)

else:
    if verifica_se_todos_os_registros_dao_x(arvore_de_decisao[primeiro_maior_ganho['atributo']]['0'], 1):
        print(1)
    else:
        print(0)


