import heapq
mapa_romania = {
    'Arad': {'cidade': 'Arad',
             'conexoes': [{'cidade': 'Zerind', 'distancia': 75},
                          {'cidade': 'Timisoara', 'distancia': 118},
                          {'cidade': 'Sibiu', 'distancia': 140}]},
    'Sibiu': {'cidade': 'Sibiu',
              'conexoes': [{'cidade': 'Fagaras', 'distancia': 99},
                           {'cidade': 'Rimnicu Vilcea', 'distancia': 80},
                           {'cidade': 'Oradea', 'distancia': 151},
                           {'cidade': 'Arad', 'distancia': 140}]},
    'Fagaras': {'cidade': 'Fagaras',
                'conexoes': [{'cidade': 'Bucharest', 'distancia': 211},
                             {'cidade': 'Sibiu', 'distancia': 99}]},
    'Rimnicu Vilcea': {
        'cidade': 'Rimnicu Vilcea',
        'conexoes': [{'cidade': 'Craiova', 'distancia': 146},
                     {'cidade': 'Sibiu', 'distancia': 80},
                     {'cidade': 'Pitesti', 'distancia': 97}]},
    'Pitesti': {'cidade': 'Pitesti',
                'conexoes': [{'cidade': 'Bucharest', 'distancia': 101},
                             {'cidade': 'Rimnicu Vilcea', 'distancia': 97},
                             {'cidade': 'Craiova', 'distancia': 138}]},
    'Bucharest': {'cidade': 'Bucharest',
                  'conexoes': [{'cidade': 'Fagaras', 'distancia': 211},
                               {'cidade': 'Pitesti', 'distancia': 101},
                               {'cidade': 'Urziceni', 'distancia': 85},
                               {'cidade': 'Giurgiu', 'distancia': 90}]},
    'Giurgiu': {'cidade': 'Giurgiu',
                'conexoes': [{'cidade': 'Bucharest', 'distancia': 90}]},
    'Urziceni': {'cidade': 'Urziceni',
                 'conexoes': [{'cidade': 'Bucharest', 'distancia': 85},
                              {'cidade': 'Vaslui', 'distancia': 142},
                              {'cidade': 'Hirsova', 'distancia': 98},
                              ]},
    'Hirsova': {
        'cidade': 'Hirsova',
        'conexoes': [{'cidade': 'Urziceni', 'distancia': 98},
                     {'cidade': 'Eforie', 'distancia': 86}]},
    'Eforie': {
        'cidade': 'Eforie',
        'conexoes': [{'cidade': 'Hirsova', 'distancia': 86}]},
    'Vaslui': {
        'cidade': 'Vaslui',
        'conexoes': [{'cidade': 'Urziceni', 'distancia': 142},
                     {'cidade': 'Iasi', 'distancia': 92}]},
    'Iasi': {
        'cidade': 'Iasi',
        'conexoes': [{'cidade': 'Neamt', 'distancia': 87},
                     {'cidade': 'Vaslui', 'distancia': 92}]},
    'Neamt': {'cidade': 'Neamt',
              'conexoes': [{'cidade': 'Iasi', 'distancia': 87}]},
    'Craiova': {'cidade': 'Craiova',
                'conexoes': [{'cidade': 'Pitesti', 'distancia': 138},
                             {'cidade': 'Rimnicu Vilcea', 'distancia': 146},
                             {'cidade': 'Drobeta', 'distancia': 120}]},
    'Drobeta': {
        'cidade': 'Drobeta',
        'conexoes': [{'cidade': 'Craiova', 'distancia': 120},
                     {'cidade': 'Mehadia', 'distancia': 75}]},
    'Mehadia': {
        'cidade': 'Mehadia',
        'conexoes': [{'cidade': 'Drobeta', 'distancia': 75},
                     {'cidade': 'Lugoj', 'distancia': 70}]},
    'Lugoj': {
        'cidade': 'Lugoj',
        'conexoes': [{'cidade': 'Mehadia', 'distancia': 70},
                     {'cidade': 'Timisoara', 'distancia': 111}]},
    'Timisoara': {
        'cidade': 'Timisoara',
        'conexoes': [{'cidade': 'Arad', 'distancia': 118},
                     {'cidade': 'Lugoj', 'distancia': 111}]},
    'Zerind': {
        'cidade': 'Zerind',
        'conexoes': [{'cidade': 'Arad', 'distancia': 75},
                     {'cidade': 'Oradea', 'distancia': 71}]},
    'Oradea': {'cidade': 'Zerind',
               'conexoes': [{'cidade': 'Zerind', 'distancia': 71},
                            {'cidade': 'Sibiu', 'distancia': 151}]}
}

heuristica_romania = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def romania_astar(inicio, objetivo):
    caminho = {}
    filaFechada = {}
    filaAberta = []
    heapq.heappush(filaAberta, (0, inicio))
    filaFechada[inicio] = 0
    while filaAberta:
        elemento_atual = mapa_romania[heapq.heappop(filaAberta)[1]]
        for sucessor in mapa_romania[elemento_atual['cidade']]['conexoes']:
            if sucessor['cidade'] == objetivo:
                break
            g = filaFechada[elemento_atual['cidade']] + int(sucessor['distancia'])
            if sucessor['cidade'] not in filaFechada or g < filaFechada[sucessor['cidade']]:
                filaFechada[sucessor['cidade']] = g
                f = g + heuristica_romania[sucessor['cidade']]
                heapq.heappush(filaAberta, (f, sucessor['cidade']))
                caminho[sucessor['cidade']] = sucessor['cidade']
    print(caminho)
