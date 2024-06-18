def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = float(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(matriz1, matriz2):
    matriz_resultante = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return matriz_resultante

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    print("Matriz A:")
    matrizA = ler_matriz()

    print("\nMatriz B:")
    matrizB = ler_matriz()

    matrizC = multiplicar_matrizes(matrizA, matrizB)

    print("\nMatriz resultante C = A * B:")
    imprimir_matriz(matrizC)

if __name__ == "__main__":
    main()
