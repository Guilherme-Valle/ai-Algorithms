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
        parametros_funcao = output_regex.group(2).split(',')
        base_de_conhecimento[assinatura_funcao].append(parametros_funcao)
    else:
        loop = False

consulta = input().rstrip()
output_regex = re.search(r'(.*?)\((.*)\)', consulta)

assinatura_consulta = output_regex.group(1)
parametros_consulta = output_regex.group(2).split(',')


array_assinatura = base_de_conhecimento[assinatura_consulta]
resposta = []
for item in array_assinatura:
    if item[0] == parametros_consulta[0]:
        resposta.append(parametros_consulta[1] + '/' + item[1])
    if item[1] == parametros_consulta[1]:
        resposta.append(parametros_consulta[0] + '/' + item[0])
    if parametros_consulta[0].isupper() and parametros_consulta[1].isupper():
        resposta.append(parametros_consulta[0] + '/' + item[0])
        resposta.append(parametros_consulta[1] + '/' + item[1])


print(','.join(resposta))