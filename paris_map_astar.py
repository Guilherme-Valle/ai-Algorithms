from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionaAresta(self, x, y):
        self.grafo[x].append(y)
        self.grafo[y].append(x)
