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

def calcular_quadrado(matriz):
    return multiplicar_matrizes(matriz, matriz)

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    print("Digite os elementos da matriz A:")
    matrizA = ler_matriz()

    matrizB = calcular_quadrado(matrizA)

    print("\nMatriz A:")
    imprimir_matriz(matrizA)

    print("\nMatriz B = A^2:")
    imprimir_matriz(matrizB)

if __name__ == "__main__":
    main()
