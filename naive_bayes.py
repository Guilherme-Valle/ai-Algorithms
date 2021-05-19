

dicionario_atributos = {}

numero_de_registros, numero_de_atributos = input().rstrip().split(' ')
numero_de_registros = int(numero_de_registros)
numero_de_atributos = int(numero_de_atributos)
total_casos_0 = 0
total_casos_1 = 0

for i in range(numero_de_registros):
    atributos = input().rstrip().split(' ')
    dicionario_atributos[i] = {}
    if int(atributos[numero_de_atributos-1]) == 1:
        total_casos_1 += 1
    else:
        total_casos_0 += 1
    for z in range(numero_de_atributos):
        dicionario_atributos[i][z] = int(atributos[z])


def ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(x, y, z):
    ocorrencias = 0
    for i in range(numero_de_registros):
        if dicionario_atributos[i][x] == y and dicionario_atributos[i][numero_de_atributos-1] == z:
            ocorrencias += 1

    return ocorrencias


caso_de_teste = input().rstrip().split(' ')

casos_de_teste_0 = 1
casos_de_teste_1 = 1
for indice, valor in (enumerate(caso_de_teste)):
    casos_de_teste_0 *= (ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(indice, int(valor), 0) + 1) / (total_casos_0 + numero_de_registros)
    casos_de_teste_1 *= (ocorrencias_de_atributo_x_igual_a_y_com_a_classe_z(indice, int(valor), 1) + 1) / (total_casos_1 + numero_de_registros)

if casos_de_teste_0 > casos_de_teste_1:
    print(0)
else:
    print(1)


