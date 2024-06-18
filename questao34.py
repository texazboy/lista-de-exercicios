vetor = []

print("Digite 10 números inteiros diferentes para preencher o vetor:")

for i in range(10):
    while True:
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        if numero not in vetor:
            vetor.append(numero)
            break
        else:
            print("Número já digitado anteriormente. Digite outro número.")

print("\nVetor final:")
print(vetor)
