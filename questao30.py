vetor1 = []
vetor2 = []

print("Digite 10 números inteiros para preencher o primeiro vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro para o primeiro vetor: "))
    vetor1.append(numero)

print("\nDigite 10 números inteiros para preencher o segundo vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro para o segundo vetor: "))
    vetor2.append(numero)

interseccao = list(set(vetor1) & set(vetor2))

print("\nVetor interseção entre os dois vetores:")
print(interseccao)
