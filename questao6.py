vetor = []

print("Digite 10 números para preencher o vetor:")
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for num in vetor:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior elemento do vetor é: {maior}")
print(f"O menor elemento do vetor é: {menor}")
