vetor = []

print("Digite 15 números inteiros para preencher o vetor:")
for i in range(15):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

i = 0
while i < len(vetor):
    if vetor[i] == 0:
        for j in range(i, len(vetor) - 1):
            vetor[j] = vetor[j + 1]
        vetor[-1] = 0
    else:
        i += 1

print("\nVetor compactado:")
print(vetor)
