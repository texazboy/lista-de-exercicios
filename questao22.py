A = []
B = []
C = []

print("Digite 10 números inteiros para o vetor A:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro para o vetor A: "))
    A.append(numero)

print("\nDigite 10 números inteiros para o vetor B:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro para o vetor B: "))
    B.append(numero)

for i in range(10):
    if i % 2 == 0:
        C.append(A[i])
    else:
        C.append(B[i])

print("\nVetor C (posições pares de A e posições ímpares de B):")
print(C)
