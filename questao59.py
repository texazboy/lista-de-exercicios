def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x6:")
    for i in range(3):
        linha = []
        for j in range(6):
            elemento = float(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def soma_colunas_impares(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][1]
        soma += matriz[i][3]
    return soma

def media_colunas_segunda_quarta(matriz):
    soma_segunda_coluna = 0
    soma_quarta_coluna = 0
    for i in range(3):
        soma_segunda_coluna += matriz[i][1]
        soma_quarta_coluna += matriz[i][3]
    media_segunda_quarta = (soma_segunda_coluna + soma_quarta_coluna) / 3
    return media_segunda_quarta

def substituir_coluna_sexta(matriz):
    for i in range(3):
        soma_coluna_1_2 = matriz[i][0] + matriz[i][1]
        matriz[i][5] = soma_coluna_1_2
    return matriz

def main():
    matriz = ler_matriz()

    imprimir_matriz(matriz)

    soma_colunas_imp = soma_colunas_impares(matriz)
    print(f"Soma dos elementos das colunas ímpares (2ª e 4ª): {soma_colunas_imp}")

    media_segunda_quarta = media_colunas_segunda_quarta(matriz)
    print(f"Média aritmética da segunda e quarta colunas: {media_segunda_quarta:.2f}")

    matriz_modificada = substituir_coluna_sexta(matriz)

    print("\nMatriz modificada:")
    imprimir_matriz(matriz_modificada)

if __name__ == "__main__":
    main()
