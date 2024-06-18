def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

vetor = []

print("Digite 10 números inteiros para preencher o vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

print("\nElementos primos e suas respectivas posições no vetor:")
for i in range(10):
    if eh_primo(vetor[i]):
        print(f"Número primo: {vetor[i]}, Posição: {i}")
