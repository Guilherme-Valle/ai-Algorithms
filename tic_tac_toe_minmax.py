# Verifica se há célula jogável
def existemLancesValidos(tabuleiro, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if tabuleiro[i][j] == -1:
                return True
    return False


def existeVencedor(tabuleiro, n):
    # Checa linhas
    return


tab = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1],
]

if existeVencedor(tab, 3):
    print('Linha preenchida')
else:
    print('Sem linha preenchida')
