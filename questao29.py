numeros = []

print("Digite 6 números inteiros:")
for i in range(6):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

soma_pares = sum(pares)
quantidade_impares = len(impares)

print("\nNúmeros pares digitados:")
print(pares)
print(f"Soma dos números pares digitados: {soma_pares}")

print("\nNúmeros ímpares digitados:")
print(impares)
print(f"Quantidade de números ímpares digitados: {quantidade_impares}")
