X = []
Y = []

print("Digite 5 números reais para preencher o vetor X:")
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número real para o vetor X: "))
    X.append(numero)

print("\nDigite 5 números reais para preencher o vetor Y:")
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número real para o vetor Y: "))
    Y.append(numero)

produto_escalar = sum(X[i] * Y[i] for i in range(5))

print("\nVetor X:")
print(X)
print("\nVetor Y:")
print(Y)
print("\nProduto Escalar (X . Y):")
print(produto_escalar)
