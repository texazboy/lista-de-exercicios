matriz1 = []
matriz2 = []
matriz_maior = []

print("Digite os elementos da primeira matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz1.append(linha)

print("\nDigite os elementos da segunda matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha)

print("\nMatriz dos maiores valores:")
for i in range(4):
    linha_maior = []
    for j in range(4):
        maior_valor = max(matriz1[i][j], matriz2[i][j])
        linha_maior.append(maior_valor)
    matriz_maior.append(linha_maior)
    print(linha_maior)
