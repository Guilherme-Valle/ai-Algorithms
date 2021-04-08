from collections import defaultdict


class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionaAresta(self, x, y):
        self.grafo[x].append(y)

    def exibeResultado(self, caminho):
        result = ''
        for idx, no in enumerate(caminho):
            result += str(no) if (idx == len(caminho) - 1) else str(no) + '-'
        print(result, end="")

    def buscaEmLargura(self, origem, objetivo):
        fila = []
        caminho = []
        verticesVisitados = {}
        fila.append(origem)
        verticesVisitados[origem] = 1
        while fila:
            noAtual = fila.pop(0)
            caminho.append(noAtual)
            if noAtual == objetivo:
                self.exibeResultado(caminho)
                break
            for item in self.grafo[noAtual]:
                if item in verticesVisitados:
                    continue
                fila.append(item)
                caminho.append(item)
                verticesVisitados[item] = 1
                if item == objetivo:
                    self.exibeResultado(caminho)
                    return
