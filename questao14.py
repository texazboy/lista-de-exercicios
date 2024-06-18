vetor = []

print("Digite 10 valores para preencher o vetor:")
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

valores_impressos = set()

print("\nValores iguais no vetor:")
for i in range(10):
    for j in range(i + 1, 10):
        if vetor[i] == vetor[j] and vetor[i] not in valores_impressos:
            print(vetor[i])
            valores_impressos.add(vetor[i])
