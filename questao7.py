vetor = []

print("Digite 10 números inteiros para preencher o vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

maior = vetor[0]
posicao_maior = 0

for i in range(1, 10):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao_maior = i

print("\nVetor:")
print(vetor)

print(f"\nO maior elemento do vetor é {maior} e está na posição {posicao_maior}.")
