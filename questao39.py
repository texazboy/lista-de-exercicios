def triangulo_de_pascal(n):
    tri = []
    for linha in range(n):
        nova_linha = [1]
        for j in range(1, linha):
            nova_linha.append(tri[linha-1][j-1] + tri[linha-1][j])
        if linha > 0:
            nova_linha.append(1)
        tri.append(nova_linha)
    return tri

n = int(input("Digite o número de linhas do Triângulo de Pascal que você deseja gerar: "))

resultado = triangulo_de_pascal(n)

for linha in resultado:
    print(" ".join(map(str, linha)))