def ler_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def contar_maiores_que_10(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1
    return contador

print("Digite os valores da matriz 4x4:")
matriz = ler_matriz()

quantidade_maiores_que_10 = contar_maiores_que_10(matriz)

print(f"\nA matriz possui {quantidade_maiores_que_10} valores maiores que 10.")
