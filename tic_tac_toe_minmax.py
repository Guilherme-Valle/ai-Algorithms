CASA_LIVRE = '-1'
LANCE_ADVERSARIO = '0'
LANCE_JOGADOR = '1'


# Verifica se há célula jogável
def existemLancesValidos(tabuleiro, n):
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == CASA_LIVRE:
                return True
    return False


def existeVencedorDiagonalPrincipal(tabuleiro, n):
    x = tabuleiro[0][0]
    if x == CASA_LIVRE:
        return False
    for i in range(n):
        if x != tabuleiro[i][i] or x == CASA_LIVRE:
            return False
    return x


def existeVencedorNaColuna(tabuleiro, coluna, n):
    x = tabuleiro[0][coluna]
    if x == CASA_LIVRE:
        return False
    for i in range(n):
        if x != tabuleiro[i][coluna] or x == CASA_LIVRE:
            return False
    return x


def existeVencedorNaLinha(tabuleiro, linha, n):
    x = tabuleiro[linha][0]
    if x == CASA_LIVRE:
        return False
    for i in range(n):
        if x != tabuleiro[linha][i] or x == CASA_LIVRE:
            return False
    return x


def existeVencedor(tabuleiro, n):
    if existeVencedorDiagonalPrincipal(tabuleiro, n):
        return existeVencedorDiagonalPrincipal(tabuleiro, n)
    for linha_ou_coluna in range(n):
        if existeVencedorNaColuna(tabuleiro, linha_ou_coluna, n):
            return existeVencedorNaColuna(tabuleiro, linha_ou_coluna, n)
        if existeVencedorNaLinha(tabuleiro, linha_ou_coluna, n):
            return existeVencedorNaLinha(tabuleiro, linha_ou_coluna, n)


def minmax(tabuleiro, profundidade, turnoMax, n):
    valorMovimento = existeVencedor(tabuleiro, n)
    if valorMovimento == LANCE_JOGADOR:
        return 1000
    if valorMovimento == LANCE_ADVERSARIO:
        return -1000
    if max:
        melhorMovimento = -1000
        for i in range(n):
            for j in range(n):
                if tabuleiro[i][j] == CASA_LIVRE:
                    tabuleiro[i][j] = LANCE_ADVERSARIO
                    melhorMovimento = max(melhorMovimento, minmax(tabuleiro, profundidade + 1, not turnoMax, n))
                    tabuleiro[i][j] = CASA_LIVRE
        return melhorMovimento
    else:
        melhorMovimento = 1000
        for i in range(n):
            for j in range(n):
                if tabuleiro[i][j] == CASA_LIVRE:
                    tabuleiro[i][j] = LANCE_JOGADOR
                    melhorMovimento = min(melhorMovimento, minmax(tabuleiro, profundidade + 1, not turnoMax, n))
                    tabuleiro[i][j] = CASA_LIVRE
        return melhorMovimento


def encontraMelhorLance(tabuleiro, n):
    melhorAvaliacao = -1000
    melhorMovimento = '-1,-1'
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == CASA_LIVRE:
                tabuleiro[i][j] = LANCE_JOGADOR
                valorAvaliacao = minmax(tabuleiro, 0, False, n)
                tabuleiro[i][j] = CASA_LIVRE
                if valorAvaliacao > melhorAvaliacao:
                    melhorAvaliacao = valorAvaliacao
                    melhorMovimento = str(i) + ',' + str(j)

    if melhorMovimento == '-1,-1':
        for i in range(n):
            if tabuleiro[i][i] == CASA_LIVRE:
                melhorMovimento = str(i) + ',' + str(i)
                break
    return melhorMovimento


def jogoDaVelha(tabuleiro, n):
    if not existemLancesValidos(tabuleiro, n) or existeVencedor(tabuleiro, n):
        print('-1, -1')
        return
    melhorLance = encontraMelhorLance(tabuleiro, n)
    print(melhorLance)


# 1 - Verifica se há lances válidos
# 2 - Verifica se há vencedor
# 3 - Jogada que evita derrota
# 4 - Jogada vencedora
# 5 - Jogada na diagonal
# 6 - Último lance válido
n = int(input().rstrip())
estados = {}

for i in range(n):
    estados[i] = input().rstrip().split(' ')
jogoDaVelha(estados, n)
