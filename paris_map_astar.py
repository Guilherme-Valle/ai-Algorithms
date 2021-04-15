from collections import defaultdict
import heapq
import re

ESTACOES = {
    'E1': {'E1': 0,
           'E2': 10,
           'E3': 18.5,
           'E4': 24.8,
           'E5': 36.4,
           'E6': 38.8,
           'E7': 35.8,
           'E8': 25.4,
           'E9': 17.6,
           'E10': 9.1,
           'E11': 16.7,
           'E12': 27.3,
           'E13': 27.6,
           'E14': 29.8,
           'CONEXOES': ['E2-AZUL']},
    'E2': {'E1': 10,
           'E2': 0,
           'E3': 8.5,
           'E4': 14.8,
           'E5': 26.6,
           'E6': 29.1,
           'E7': 26.1,
           'E8': 17.3,
           'E9': 10,
           'E10': 3.5,
           'E11': 15.5,
           'E12': 20.9,
           'E13': 19.1,
           'E14': 21.8,
           'CONEXOES': ['E1-AZUL', 'E10-AMARELA', 'E9-AMARELA', 'E3-AZUL']},
    'E3': {'E1': 18.5,
           'E2': 8.5,
           'E3': 0,
           'E4': 6.3,
           'E5': 18.2,
           'E6': 20.6,
           'E7': 17.6,
           'E8': 13.6,
           'E9': 9.4,
           'E10': 10.3,
           'E11': 19.5,
           'E12': 19.1,
           'E13': 12.1,
           'E14': 16.6,
           'CONEXOES': ['E2-AZUL', 'E9-VERMELHA', 'E4-AZUL', 'E13-VERMELHA']},
    'E4': {'E1': 24.8,
           'E2': 14.8,
           'E3': 6.3,
           'E4': 0,
           'E5': 13,
           'E6': 14.4,
           'E7': 11.5,
           'E8': 12.4,
           'E9': 12.6,
           'E10': 16.7,
           'E11': 23.6,
           'E12': 18.6,
           'E13': 12.8,
           'E14': 15.4,
           'CONEXOES': ['E3-AZUL', 'E13-VERDE', 'E8-VERDE', 'E5-AZUL']},
    'E5': {'E1': 36.4,
           'E2': 26.6,
           'E3': 18.2,
           'E4': 13,
           'E5': 0,
           'E6': 3,
           'E7': 2.4,
           'E8': 19.4,
           'E9': 23.3,
           'E10': 28.2,
           'E11': 34.2,
           'E12': 24.8,
           'E13': 14.5,
           'E14': 17.9,
           'CONEXOES': ['E4-AZUL', 'E6-AZUL', 'E7-AMARELA', 'E8-AMARELA']},
    'E6': {'E1': 38.8,
           'E2': 29.1,
           'E3': 20.6,
           'E4': 14.4,
           'E5': 3,
           'E6': 0,
           'E7': 3.3,
           'E8': 22.3,
           'E9': 25.7,
           'E10': 30.3,
           'E11': 36.7,
           'E12': 27.6,
           'E13': 15.2,
           'E14': 18.2,
           'CONEXOES': ['E5-AZUL']},
    'E7': {'E1': 35.8,
           'E2': 26.1,
           'E3': 17.6,
           'E4': 11.5,
           'E5': 2.4,
           'E6': 3.3,
           'E7': 0,
           'E8': 20,
           'E9': 23,
           'E10': 27.3,
           'E11': 34.2,
           'E12': 25.7,
           'E13': 12.4,
           'E14': 15.6,
           'CONEXOES': ['E5-AMARELA']},
    'E8': {'E1': 25.4,
           'E2': 17.3,
           'E3': 13.6,
           'E4': 12.4,
           'E5': 19.4,
           'E6': 22.3,
           'E7': 20,
           'E8': 0,
           'E9': 8.2,
           'E10': 20.3,
           'E11': 16.1,
           'E12': 6.4,
           'E13': 22.7,
           'E14': 27.6,
           'CONEXOES': ['E4-VERDE', 'E5-AMARELA', 'E9-AMARELA', 'E12-VERDE']},
    'E9': {'E1': 17.6,
           'E2': 10,
           'E3': 9.4,
           'E4': 12.6,
           'E5': 23.3,
           'E6': 25.7,
           'E7': 23,
           'E8': 8.2,
           'E9': 0,
           'E10': 13.5,
           'E11': 11.2,
           'E12': 10.9,
           'E13': 21.2,
           'E14': 26.6,
           'CONEXOES': ['E2-AMARELA', 'E3-VERMELHA', 'E8-AMARELA', 'E11-VERMELHA']},
    'E10': {'E1': 9.1,
            'E2': 3.5,
            'E3': 10.3,
            'E4': 16.7,
            'E5': 28.2,
            'E6': 30.3,
            'E7': 27.3,
            'E8': 20.3,
            'E9': 13.5,
            'E10': 0,
            'E11': 17.6,
            'E12': 24.2,
            'E13': 18.7,
            'E14': 21.2,
            'CONEXOES': ['E2-AMARELA']},
    'E11': {'E1': 16.7,
            'E2': 15.5,
            'E3': 19.5,
            'E4': 23.6,
            'E5': 34.2,
            'E6': 36.7,
            'E7': 34.2,
            'E8': 16.1,
            'E9': 11.2,
            'E10': 17.6,
            'E11': 0,
            'E12': 24.2,
            'E13': 18.7,
            'E14': 21.2,
            'CONEXOES': ['E9-VERMELHA']},
    'E12': {'E1': 27.3,
            'E2': 20.9,
            'E3': 19.1,
            'E4': 18.6,
            'E5': 24.8,
            'E6': 27.6,
            'E7': 25.7,
            'E8': 6.4,
            'E9': 10.9,
            'E10': 24.2,
            'E11': 14.2,
            'E12': 0,
            'E13': 28.8,
            'E14': 33.6,
            'CONEXOES': ['E8-VERDE']},
    'E13': {'E1': 27.6,
            'E2': 19.1,
            'E3': 12.1,
            'E4': 10.6,
            'E5': 14.5,
            'E6': 15.2,
            'E7': 12.4,
            'E8': 22.7,
            'E9': 21.2,
            'E10': 18.7,
            'E11': 31.5,
            'E12': 28.8,
            'E13': 0,
            'E14': 5.1,
            'CONEXOES': ['E3-VERMELHA', 'E4-VERDE', 'E14-VERDE']},
    'E14': {'E1': 29.8,
            'E2': 21.8,
            'E3': 16.6,
            'E4': 15.4,
            'E5': 17.9,
            'E6': 18.2,
            'E7': 15.6,
            'E8': 27.6,
            'E9': 26.6,
            'E10': 21.2,
            'E11': 35.5,
            'E12': 33.6,
            'E13': 5.1,
            'E14': 0,
            'CONEXOES': ['E13-VERDE']},

}


def removeLetras(string):
    return re.sub('[^0-9]', '', string)


def distanciaEntreEstacoes(origem, destino):
    return ESTACOES[origem][destino]


def existeConexaoQueNaoEstaNaFilaFechada(conexoes, fila):
    for conexao in conexoes:
        conexao = conexao.split('-')[0]
        if conexao not in fila:
            return True
    return False


def corLinhaConectandoAntecessores(estacao, conexoes):
    for conexao in conexoes:
        estacao_conexao = conexao.split('-')[0]
        linha = conexao.split('-')[1]
        if estacao == estacao_conexao:
            return linha
    return "Nao ha"


# distancia/velocidade * 60

def astar(origem, destino, velocidade, baldeacao):
    caminho = []
    nos_expandidos = []
    filaAberta = []
    heapq.heappush(filaAberta, (0, origem))
    filaFechada = {}
    filaFechada[origem] = 0
    while filaAberta:
        topo_fila = heapq.heappop(filaAberta)
        atual = topo_fila[1]
        nos_expandidos.append(atual)
        if existeConexaoQueNaoEstaNaFilaFechada(ESTACOES[atual]['CONEXOES'], filaFechada):
            caminho.append(atual)
        if atual == destino:
            caminho_string = '-'.join(map(removeLetras, caminho))
            nos_expandidos_string = '-'.join(map(removeLetras, nos_expandidos))
            distancia = (filaFechada[atual] / float(velocidade)) * 60
            print(nos_expandidos_string + "\n" + caminho_string + "\n" + "%.1f" % distancia)
            break
        for no in ESTACOES[atual]['CONEXOES']:
            conexao = no.split('-')[0]
            linhaAtual = no.split('-')[1]
            if conexao in filaFechada:
                continue
            if not any(conexao == item for index, item in filaAberta):
                tem_baldeacao = False
                if len(caminho) > 1:
                    if linhaAtual != corLinhaConectandoAntecessores(atual, ESTACOES[caminho[len(caminho) - 2]]["CONEXOES"]):
                        tem_baldeacao = True

                g = filaFechada[atual] + distanciaEntreEstacoes(atual, conexao)
                g += (velocidade * baldeacao) / 60 if tem_baldeacao else 0
                filaFechada[conexao] = g
                f = g + distanciaEntreEstacoes(conexao, destino)
                heapq.heappush(filaAberta, (f, conexao))


entry = input().rstrip()
inputs = entry.split(' ')
origem = inputs[0]
destino = inputs[1]
velocidade = input().rstrip()
baldeacao = input().rstrip()
astar('E' + str(origem), 'E' + str(destino), velocidade, baldeacao)
