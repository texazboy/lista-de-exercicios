vetor = []

print("Digite 10 números inteiros para preencher o vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

for i in range(10):
    if vetor[i] < 0:
        vetor[i] = 0

print("\nVetor com valores negativos substituídos por 0:")
print(vetor)
