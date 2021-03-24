mapa_romania = {
    'Arad' : { 'conexoes': [ { 'cidade':'Zerind', 'distancia': 75},
                             { 'cidade':'Timisoara', 'distancia': 118},
                             { 'cidade':'Sibiu', 'distancia': 140} ] },

    'Sibiu' : { 'conexoes': [ { 'cidade':'Fagaras', 'distancia': 99},
                              { 'cidade':'Rimnicu Vilcea', 'distancia': 80},
                              { 'cidade':'Oradea', 'distancia': 151},
                              { 'cidade':'Arad', 'distancia': 140} ]  },
}

def romania_astar():
    print(mapa_romania['Arad']['conexoes'][0]['cidade'])
