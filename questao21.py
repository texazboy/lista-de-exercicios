A = []
B = []

print("Digite 10 números inteiros para o vetor A:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro para o vetor A: "))
    A.append(numero)

print("\nDigite 10 números inteiros para o vetor B:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro para o vetor B: "))
    B.append(numero)

C = [A[i] - B[i] for i in range(10)]

print("\nVetor C (C = A - B):")
for num in C:
    print(num)
