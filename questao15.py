vetor = []

print("Digite 20 números inteiros para preencher o vetor:")
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

vetor_sem_repeticoes = list(set(vetor))

print("\nElementos do vetor sem repetições:")
for elemento in vetor_sem_repeticoes:
    print(elemento, end=" ")
print()
