def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 2x2:")
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = float(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz1, matriz2):
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado

def subtrair_matrizes(matriz1, matriz2):
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            subtracao = matriz1[i][j] - matriz2[i][j]
            linha.append(subtracao)
        resultado.append(linha)
    return resultado

def adicionar_constante(matriz, constante):
    for i in range(2):
        for j in range(2):
            matriz[i][j] += constante

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    print("Matriz 1:")
    matriz1 = ler_matriz()

    print("\nMatriz 2:")
    matriz2 = ler_matriz()

    while True:
        print("\nMENU DE OPÇÕES:")
        print("a) Somar as duas matrizes")
        print("b) Subtrair a primeira matriz da segunda")
        print("c) Adicionar uma constante às duas matrizes")
        print("d) Imprimir as matrizes")
        print("e) Sair")

        opcao = input("Escolha uma opção (a, b, c, d, e): ")

        if opcao == 'a':
            resultado_soma = somar_matrizes(matriz1, matriz2)
            print("\nResultado da soma das matrizes:")
            imprimir_matriz(resultado_soma)
        elif opcao == 'b':
            resultado_subtracao = subtrair_matrizes(matriz1, matriz2)
            print("\nResultado da subtração das matrizes:")
            imprimir_matriz(resultado_subtracao)
        elif opcao == 'c':
            constante = float(input("Digite a constante a ser adicionada às matrizes: "))
            adicionar_constante(matriz1, constante)
            adicionar_constante(matriz2, constante)
            print("\nMatriz 1 após adição da constante:")
            imprimir_matriz(matriz1)
            print("\nMatriz 2 após adição da constante:")
            imprimir_matriz(matriz2)
        elif opcao == 'd':
            print("\nMatriz 1:")
            imprimir_matriz(matriz1)
            print("\nMatriz 2:")
            imprimir_matriz(matriz2)
        elif opcao == 'e':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
