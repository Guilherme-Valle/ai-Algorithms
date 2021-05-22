numero_registros, numero_atributos = [int(x) for x in input().rstrip().split(' ')]
bias, taxa_de_aprendizado = [float(x) for x in input().rstrip().split(' ')]
pesos = {}
atributos = {}
instancias = {}
pesos = [float(x) for x in input().rstrip().split(' ')]
MAX_ITERACOES = 100

for indice in range(int(numero_registros)):
    atributos[indice] = [int(x) for x in input().rstrip().split(' ')]

numero_instancias = input().rstrip()
for indice in range(int(numero_instancias)):
    instancias[indice] = [int(x) for x in input().rstrip().split(' ')]

def funcao_escada(x):
    return 1 if x >= 0 else -1

def testa_registro(registro, teste_bias):
    soma_valor = 0
    #print(registro)
    #print('Pesos pro teste do registro: ')
    #print(pesos)
    for indice in range(numero_atributos - 1):
     #   print('Conta de valor: ' + str(registro[indice])  + ' * (' + str(pesos[indice]) + ')')
        soma_valor += registro[indice] * pesos[indice]
    #print('Conta bias: 1 *' + str(teste_bias) )
    soma_valor += 1*teste_bias
    #print('Soma: ' + str(soma_valor))
    return soma_valor

def atualiza_pesos(atributo, bias, valor_esperado, valor_retornado):
    #print('Pesos antigos: ')
    #print(pesos)
    #print('Resultado esperado: ' + str(valor_esperado))
    #print('Resultado retornado: ' + str(valor_retornado))
    for i in range(numero_atributos - 1):
        #print('Conta peso: ' + str(pesos[i]) + ' + (' + str(taxa_de_aprendizado) + ') * ' + str(atributo[i]) + ' * ('
        #      + str(valor_esperado) + ' - (' + str(valor_retornado) + ')')
        pesos[i] = pesos[i] + (taxa_de_aprendizado * atributo[i] * (valor_esperado - (valor_retornado)))
        #print('w' + str(i) + ' = ' + str(pesos[i]))
    bias += (taxa_de_aprendizado * (valor_esperado - (valor_retornado)))
    #print('Pesos novos: ')
    #print(pesos)
    #print('Bias novo:' + str(bias))
    return bias

def verifica_se_rede_esta_treinada(bias):
    rede_treinada = True
    for indice in range(numero_registros - 1):
        if funcao_escada(testa_registro(atributos[indice], bias)) != atributos[indice][numero_registros-1]:
            rede_treinada = False

    return rede_treinada


def treinar_rede_neural(bias):
    num_teste = 0
    while not verifica_se_rede_esta_treinada(bias) and num_teste < MAX_ITERACOES:
        for indice in range(numero_registros):
            num_teste += 1
            atributo = atributos[indice]
            resultado_retornado = funcao_escada(testa_registro(atributo, bias))
            resultado_esperado = atributo[numero_atributos - 1]
            if resultado_retornado != resultado_esperado:
                bias = atualiza_pesos(atributo, bias, resultado_esperado, resultado_retornado)
    return bias

def formata_pesos(pesos):
    string = ''
    for peso in pesos:
            string += "%.1f" % peso + ' '
    return string


bias = treinar_rede_neural(bias)

print(formata_pesos(pesos) + '' + "%.1f" % bias)

for indice in range(int(numero_instancias)):
    print(funcao_escada(testa_registro(instancias[indice], bias)))