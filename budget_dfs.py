from collections import deque

# Problema dos dois jarros de água: resolução com deep-search
# Operações possíveis:
# enche(balde) = Enche um dos baldes
# esvazia(balde) = Esvazia um dos baldes
# transfere(a, b) = Transfere água do balde A para o balde B
# 1 - Cria uma pilha vazia
# 2 - Insere o estado inicial (0, 0)
# 3 - Para cada estado gera os estados possíveis e, caso não tenha sido visitado ainda, guarda na pilha
# 4 - Ao achar solução, para o loop e imprime o caminho
def solucao_balde_dfs():
    estados_visitados = {}
    caminho = []
    pilha = deque()
    pilha.append((0, 0))
    while len(pilha) > 0:
        # Desempilha
        estado_atual = pilha.pop()
        # Verifica se o estado já foi visitado, se sim, pula
        if (estado_atual[0], estado_atual[1]) in estados_visitados:
            continue

        # Adiciona estado ao caminho percorrido e aos estados já visitados
        caminho.append([estado_atual[0], estado_atual[1]])
        estados_visitados[(estado_atual[0], estado_atual[1])] = 1

        # Verifica se o estado é final
        if (estado_atual[1] == 2):
            for i in (range(len(caminho))):
                print("(", caminho[i][0], ",",
                      caminho[i][1], ")")
            break
        # Enche ambos os baldes e adiciona na pilha
        pilha.append((3, estado_atual[1]))
        pilha.append((estado_atual[0], 4))

        # Passa toda água do maior pode para o menor
        if estado_atual[1] > 0 and (estado_atual[0] + estado_atual[1]) <= 3:
            pilha.append((estado_atual[0] + estado_atual[1], 0))

        # Passa parte da água do jarro maior para o menor
        if estado_atual[1] > 0 and (estado_atual[0] + estado_atual[1] > 3):
            pilha.append((3, estado_atual[1] - (3 - estado_atual[0])))

        # Passa toda agua do jarro menor para o maior
        if estado_atual[0] > 0 and (estado_atual[0] + estado_atual[1] <= 4):
            pilha.append((0, estado_atual[0] + estado_atual[1]))

        # Passa parte da água do jarro menor para o maior
        if estado_atual[0] > 0 and (estado_atual[0] + estado_atual[1] > 4):
            pilha.append((estado_atual[0] - (4 - estado_atual[1]) ,4))

        # Esvazia baldes
        pilha.append((estado_atual[0], 0))
        pilha.append((0, estado_atual[1]))