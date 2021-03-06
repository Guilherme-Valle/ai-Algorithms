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
    for indice in range(numero_atributos - 1):
        soma_valor += registro[indice] * pesos[indice]
    soma_valor += 1*teste_bias
    return soma_valor

def atualiza_pesos(atributo, bias, valor_esperado, valor_retornado):
    for i in range(numero_atributos - 1):
        pesos[i] = pesos[i] + (taxa_de_aprendizado * atributo[i] * (valor_esperado - (valor_retornado)))
    bias += (taxa_de_aprendizado * (valor_esperado - (valor_retornado)))
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