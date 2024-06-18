def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_soma_colunas(matriz):
    soma_colunas = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            soma_colunas[j] += matriz[i][j]
    return soma_colunas

def main():
    matriz = ler_matriz()

    soma_colunas = calcular_soma_colunas(matriz)

    print("\nMatriz inserida:")
    for linha in matriz:
        print(linha)

    print("\nSoma das colunas:")
    print(soma_colunas)

if __name__ == "__main__":
    main()
