import numpy
import random
acoes_possiveis = ['para_cima', 'para_direita', 'para_baixo', 'para_esquerda']
tamanho_matriz = int(input().rstrip())
epsilon, fator_de_desconto ,taxa_de_aprendizado = input().rstrip().split(' ')
valores_q = numpy.zeros((tamanho_matriz, tamanho_matriz, 4))
NUMERO_DE_TREINOS = 1000


def monta_matriz(n):
    matriz = numpy.full((n, n), 0)
    for indice in range(int(n)):
        matriz[indice] = input().rstrip().split(' ')

    return matriz


def verifica_estado_final(estados, linha, coluna):
    return False if estados[linha, coluna] == -1 else True


def escolhe_estado_inicial(estados, n):
    linha_aleatoria = random.randint(0, n-1)
    coluna_aleatoria = random.randint(0, n-1)
    return escolhe_estado_inicial(estados, n) if verifica_estado_final(estados, linha_aleatoria, coluna_aleatoria) \
        else {'linha': linha_aleatoria, 'coluna': coluna_aleatoria}


def qual_proximo_lugar(n, linha_atual, coluna_atual, acao):
    acao = acoes_possiveis[acao]
    nova_linha, nova_coluna = linha_atual, coluna_atual
    if acao == 'para_cima':
        nova_linha -= 1 if linha_atual > 0 else 0
    elif acao == 'para_baixo':
        nova_linha += 1 if linha_atual < n - 1 else 0
    elif acao == 'para_direita':
        nova_coluna += 1 if coluna_atual < n - 1 else 0
    elif acao == 'para_esquerda':
        nova_coluna -= 1 if coluna_atual > 0 else 0

    return {'linha': nova_linha, 'coluna': nova_coluna}


def qual_proximo_movimento(linha_atual, coluna_atual, epsilon, q):
    # print('Prox_mov: ' + str(linha_atual)+ ' '+ str(coluna_atual))
    return random.randint(0, 3) if random.uniform(0, 1) >= float(epsilon) else numpy.argmax(q[linha_atual, coluna_atual])


def calcula_diferenca_temporal(recompensa, desconto, max, q_old):
    return recompensa + (desconto * max) - q_old


def caminho_mais_curto(estados, linha_inicial, coluna_inicial):
    if verifica_estado_final(estados, linha_inicial, coluna_inicial):
        return null
    else:
        linha_atual, coluna_atual = linha_inicial, coluna_inicial
        menor_caminho = [[linha_atual, coluna_atual]]
        while not verifica_estado_final(estados, linha_atual, coluna_atual):
            proximo_movimento = qual_proximo_lugar(tamanho_matriz, linha_atual, coluna_atual,
                                                   qual_proximo_movimento(linha_atual, coluna_atual, epsilon, valores_q))
            linha_atual, coluna_atual = proximo_movimento['linha'], proximo_movimento['coluna']
            menor_caminho.append([linha_atual, coluna_atual])
        return menor_caminho


# treina modelo
def q_learning(estados, n):
    for treino in range(NUMERO_DE_TREINOS):
        estado_inicial = escolhe_estado_inicial(estados, n)
        linha, coluna = estado_inicial['linha'], estado_inicial['coluna']
        while not verifica_estado_final(estados, linha, coluna):
            proxima_acao = qual_proximo_movimento(linha, coluna, epsilon, valores_q)

            linha_antiga, coluna_antiga = linha, coluna

            proximo_movimento = qual_proximo_lugar(n, linha, coluna, proxima_acao)

            linha, coluna = proximo_movimento['linha'], proximo_movimento['coluna']

            valor_q_antigo = valores_q[linha_antiga, coluna_antiga, proxima_acao]

            diferenca_temporal = calcula_diferenca_temporal(estados[linha, coluna], float(fator_de_desconto), numpy.max(valores_q[linha, coluna]), valor_q_antigo)

            valores_q[linha_antiga, coluna_antiga, proxima_acao] = valor_q_antigo + (float(taxa_de_aprendizado) * diferenca_temporal)



matriz_estados = monta_matriz(tamanho_matriz)
linha_destino, coluna_destino = input().rstrip().split(' ')

q_learning(matriz_estados, tamanho_matriz)

caminho = caminho_mais_curto(matriz_estados, 3, 9)
for etapa in caminho:
    print(str(etapa[0]) + ' ' + str(etapa[1]))