v = []
v1 = []
v2 = []

print("Digite 10 números inteiros para preencher o vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    v.append(numero)

for num in v:
    if num % 2 != 0:
        v1.append(num)
    else:
        v2.append(num)

print("\nElementos utilizados de v1:")
print(v1)
print("\nElementos utilizados de v2:")
print(v2)
