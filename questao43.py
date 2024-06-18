matriz = []
maior_valor = float('-inf')
posicao_maior = (0, 0)

print("Digite os elementos da matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        if valor > maior_valor:
            maior_valor = valor
            posicao_maior = (i, j)
    matriz.append(linha)

print("\nMatriz 4x4:")
for linha in matriz:
    print(linha)

print(f"\nO maior valor é {maior_valor} na posição {posicao_maior}")
