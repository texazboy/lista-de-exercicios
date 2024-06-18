vetor = []

print("Digite 10 números reais para preencher o vetor:")
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(numero)

vetor.sort()

print("\nVetor ordenado:")
print(vetor)
