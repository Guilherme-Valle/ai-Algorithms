import heapq
import re
import math

ESTADOS = {
    "1": {
        "1": 0,
        "2": 270,
        "3": 475,
        "4": 675,
        "5": 749,
        "6": 828,
        "7": 1017,
        "8": 980,
        "9": 1318,
        "10": 1093,
        "11": 1664,
        "12": 1924,
        "CONEXOES": ['2', '3', '4', '8', '10']
    },
    "2": {
        "1": 270,
        "2": 0,
        "3": 225,
        "4": 394,
        "5": 484,
        "6": 612,
        "7": 837,
        "8": 938,
        "9": 1236,
        "10": 1238,
        "11": 1646,
        "12": 2128,
        "CONEXOES": ['1', '3']
    },
    "3": {
        "1": 475,
        "2": 225,
        "3": 205,
        "4": 290,
        "5": 426,
        "6": 712,
        "7": 933,
        "8": 933,
        "9": 1230,
        "10": 1376,
        "11": 1683,
        "12": 2343,
        "CONEXOES": ['1', '2', '4']
    },
    "4": {
        "1": 675,
        "2": 394,
        "3": 205,
        "4": 0,
        "5": 99,
        "6": 247,
        "7": 623,
        "8": 933,
        "9": 1190,
        "10": 1508,
        "11": 1673,
        "12": 2457,
        "CONEXOES": ['1', '3', '8', '7', '5']
    },
    "5": {
        "1": 749,
        "2": 484,
        "3": 290,
        "4": 99,
        "5": 0,
        "6": 152,
        "7": 551,
        "8": 902,
        "9": 1158,
        "10": 1524,
        "11": 1632,
        "12": 2508,
        "CONEXOES": ['4', '6', '7']
    },
    "6": {
        "1": 828,
        "2": 612,
        "3": 426,
        "4": 247,
        "5": 152,
        "6": 0,
        "7": 430,
        "8": 846,
        "9": 1078,
        "10": 1545,
        "11": 1553,
        "12": 2553,
        "CONEXOES": ['5', '7']
    },
    "7": {
        "1": 1017,
        "2": 837,
        "3": 712,
        "4": 623,
        "5": 551,
        "6": 430,
        "7": 0,
        "8": 493,
        "9": 657,
        "10": 1298,
        "11": 1227,
        "12": 2334,
        "CONEXOES": ['4', '6', '5', '8']
    },
    "8": {
        "1": 980,
        "2": 938,
        "3": 933,
        "4": 933,
        "5": 902,
        "6": 846,
        "7": 493,
        "8": 0,
        "9": 325,
        "10": 845,
        "11": 746,
        "12": 1860,
        "CONEXOES": ['1', '4', '7', '9', '10']
    },
    "9": {
        "1": 1318,
        "2": 1236,
        "3": 1230,
        "4": 1190,
        "5": 1158,
        "6": 1078,
        "7": 657,
        "8": 325,
        "9": 0,
        "10": 957,
        "11": 488,
        "12": 1938,
        "CONEXOES": ['8', '10', '11']
    },
    "10": {
        "1": 1093,
        "2": 1238,
        "3": 1376,
        "4": 1508,
        "5": 1524,
        "6": 1545,
        "7": 1298,
        "8": 845,
        "9": 957,
        "10": 0,
        "11": 965,
        "12": 1032,
        "CONEXOES": ['1', '8', '9', '11', '12'],
    },
    "11": {
        "1": 1664,
        "2": 1646,
        "3": 1683,
        "4": 1673,
        "5": 1632,
        "6": 1553,
        "7": 1227,
        "8": 746,
        "9": 488,
        "10": 965,
        "11": 0,
        "12": 1787,
        "CONEXOES": ['9', '10', '12'],
    },
    "12": {
        "1": 1924,
        "2": 2128,
        "3": 2343,
        "4": 2457,
        "5": 2508,
        "6": 2533,
        "7": 2334,
        "8": 1860,
        "9": 1938,
        "10": 1032,
        "11": 1787,
        "12": 0,
        "CONEXOES": ['10', '11'],
    },
}


def existeConexaoQueNaoEstaNaFilaFechada(conexoes, fila):
    for conexao in conexoes:
        if conexao not in fila:
            return True
    return False


def distanciaEntreEstados(origem, destino):
    return ESTADOS[origem][destino]


def astarCOVID(origem, destino, qtd_vacinas, taxas_estados):
    caminho = []
    filaAberta = []
    nos_expandidos = []
    heapq.heappush(filaAberta, (0, origem))
    filaFechada = {origem: 0}
    while filaAberta:
        atual = heapq.heappop(filaAberta)[1]
        nos_expandidos.append(atual)
        if existeConexaoQueNaoEstaNaFilaFechada(ESTADOS[str(atual)]['CONEXOES'], filaFechada) or atual == destino:
            caminho.append(atual)
        if atual == destino:
            vacinas_utilizadas = 0
            for etapa in caminho:
                vacinas_utilizadas += math.floor(int(qtd_vacinas) * (0.2 * (1 - float(taxas_estados[etapa]))))
            print('-'.join(caminho) + '\n' + str(int(qtd_vacinas) - int(vacinas_utilizadas)))
            break
        for no in ESTADOS[atual]['CONEXOES']:
            if no not in nos_expandidos:
                g = filaFechada[atual] + distanciaEntreEstados(atual, no)
                if no in filaFechada:
                    filaFechada[str(no)] = g if filaFechada[str(no)] > g else filaFechada[str(no)]
                else:
                    filaFechada[str(no)] = g
                f = g + distanciaEntreEstados(no, destino)
                heapq.heappush(filaAberta, (f, no))


entry = input().rstrip()
origem, destino = entry.split(' ')
vacinas = input().rstrip()
dicionario = {}
for valores in range(12):
    valor = input().rstrip()
    estado, indice = valor.split(' ')
    dicionario[estado] = indice
astarCOVID(str(origem), str(destino), vacinas, dicionario)
