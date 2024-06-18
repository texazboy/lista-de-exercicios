numeros = []
quadrados = []

print("Digite 10 números reais:")
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)
    quadrados.append(numero ** 2)

print("\nConjunto original:")
print(numeros)

print("\nQuadrados das componentes:")
print(quadrados)
