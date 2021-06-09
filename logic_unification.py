import re

loop = True
base_de_conhecimento = {}
while loop:
    sentenca = input().rstrip()
    if sentenca != 'END':
        output_regex = re.search(r'(.*?)\((.*)\)', sentenca)
        assinatura_funcao = output_regex.group(1)
        if assinatura_funcao not in base_de_conhecimento:
            base_de_conhecimento[assinatura_funcao] = []
        parametros_funcao = re.split(r',(?![^(]*[)])',output_regex.group(2))
        # print(parametros_funcao[0][parametros_funcao[0].find("(")+1:parametros_funcao[0].find(")")])
        base_de_conhecimento[assinatura_funcao].append(parametros_funcao)
    else:
        loop = False

consulta = input().rstrip()
output_regex = re.search(r'(.*?)\((.*)\)', consulta)

assinatura_consulta = output_regex.group(1)
parametros_consulta = re.split(r',(?![^(]*[)])',output_regex.group(2))


array_assinatura = base_de_conhecimento[assinatura_consulta]
isTrue = False
isFalse = False
resposta = []
for item in array_assinatura:
    if item[0] == parametros_consulta[0]:
        resposta.append(parametros_consulta[1] + '/' + item[1])
    if item[1] == parametros_consulta[1]:
        resposta.append(parametros_consulta[0] + '/' + item[0])
    if item[0] == parametros_consulta[0] and item[1] == parametros_consulta[1]:
        isTrue = True
    if parametros_consulta[0].isupper() and parametros_consulta[1].isupper():
        resposta.append(parametros_consulta[0] + '/' + item[0])
        resposta.append(parametros_consulta[1] + '/' + item[1])

for resultado in resposta:
    array = resultado.split('/')
    item_1 = array[0][array[0].find("(")+1:array[0].find(")")]
    item_2 = array[1][array[0].find("(")+1:array[1].find(")")]
    if ',' not in item_1:
        continue
    else:
        parametro_1 = item_1.split(',')[0]
        parametro_2 = item_1.split(',')[1]
        parametro_3 = item_2.split(',')[0]
        parametro_4 = item_2.split(',')[1]
        base_de_conhecimento = []
        if parametro_1.isupper() and parametro_2 == parametro_4:
            resposta = parametro_1 + '/' + parametro_3
        elif parametro_2.isupper() and parametro_1 == parametro_3:
            resposta = parametro_2 + '/' + parametro_4
        else:
            resposta = 'FALSE'
        break

if isTrue:
    print('TRUE')
elif len(base_de_conhecimento) == 0:
    print(resposta)
else:
    print(','.join(resposta))

