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

def calcular_transposta(matriz):
    transposta = []
    for i in range(3):
        linha_transposta = []
        for j in range(3):
            linha_transposta.append(matriz[j][i])
        transposta.append(linha_transposta)
    return transposta

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elemento) for elemento in linha))

def main():
    matriz = ler_matriz()
    print("\nMatriz original:")
    imprimir_matriz(matriz)
    
    transposta = calcular_transposta(matriz)
    print("\nTransposta da matriz:")
    imprimir_matriz(transposta)

if __name__ == "__main__":
    main()
