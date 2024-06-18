import random

def gerar_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            elemento = random.randint(1, 20)
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def matriz_triangular_inferior(matriz):
    for i in range(4):
        for j in range(i + 1, 4):  # apenas acima da diagonal principal
            matriz[i][j] = 0
    return matriz

def imprimir_matriz(matriz, mensagem):
    print(mensagem)
    for linha in matriz:
        print(linha)

def main():
    matriz_original = gerar_matriz()
    imprimir_matriz(matriz_original, "\nMatriz Original:")

    matriz_transformada = matriz_triangular_inferior(matriz_original)
    imprimir_matriz(matriz_transformada, "\nMatriz Transformada em Triangular Inferior:")

if __name__ == "__main__":
    main()
