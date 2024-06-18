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

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][i]
    return soma

def main():
    matriz = ler_matriz()
    soma_diagonal = soma_diagonal_principal(matriz)
    print(f"A soma dos elementos da diagonal principal é: {soma_diagonal}")

if __name__ == "__main__":
    main()
