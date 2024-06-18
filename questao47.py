matriz = []

print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma_acima_diagonal = 0
for i in range(3):
    for j in range(i + 1, 3):
        soma_acima_diagonal += matriz[i][j]

print(f"A soma dos elementos acima da diagonal principal é: {soma_acima_diagonal}")
