vetor = []

print("Digite 10 valores numéricos para preencher o vetor:")

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    vetor.sort()

print("\nValores ordenados:")
print(vetor)
