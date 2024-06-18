vetor = []

print("Digite 10 números inteiros para preencher o vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

x = int(input("Digite um número inteiro para encontrar seus múltiplos no vetor: "))

multiplos = [num for num in vetor if num % x == 0]

print(f"\nMúltiplos de {x} encontrados no vetor:")
print(multiplos)
