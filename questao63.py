def verificar_ganhador(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != 0:
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != 0:
            return tabuleiro[0][i]
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return tabuleiro[0][2]
    
    return 0

def proxima_jogada(tabuleiro, minha_peca, peca_oponente):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = minha_peca
                if verificar_ganhador(tabuleiro) == minha_peca:
                    tabuleiro[i][j] = 0
                    return (i, j)
                tabuleiro[i][j] = 0
    
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = peca_oponente
                if verificar_ganhador(tabuleiro) == peca_oponente:
                    tabuleiro[i][j] = 0
                    return (i, j)
                tabuleiro[i][j] = 0
    
    import random
    posicoes_vazias = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == 0]
    return random.choice(posicoes_vazias) if posicoes_vazias else None

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

def main():
    tabuleiro = [
        [0,  1, -1],
        [1, -1,  0],
        [0,  0,  1]
    ]
    
    minha_peca = -1
    peca_oponente = 1
    
    print("Tabuleiro atual:")
    imprimir_tabuleiro(tabuleiro)
    
    proxima = proxima_jogada(tabuleiro, minha_peca, peca_oponente)
    
    if proxima:
        print(f"Próxima jogada: {proxima}")
    else:
        print("Não há mais jogadas disponíveis.")

if __name__ == "__main__":
    main()
