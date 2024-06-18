x = []
y = []

print("Digite 5 números inteiros para preencher o vetor x:")
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro para o vetor x: "))
    x.append(numero)

print("\nDigite 5 números inteiros para preencher o vetor y:")
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro para o vetor y: "))
    y.append(numero)

soma = [x[i] + y[i] for i in range(5)]
produto = [x[i] * y[i] for i in range(5)]
diferenca = [num for num in x if num not in y]
interseccao = list(set(x) & set(y))
uniao = list(set(x) | set(y))

print("\nSoma entre x e y:")
print(soma)

print("\nProduto entre x e y:")
print(produto)

print("\nDiferença entre x e y (elementos de x que não estão em y):")
print(diferenca)

print("\nInterseção entre x e y:")
print(interseccao)

print("\nUnião entre x e y (elementos de x, e elementos de y que não estão em x):")
print(uniao)
