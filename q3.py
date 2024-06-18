
numeros = []
quadrados = []

for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)
    quadrados.append(numero ** 2)

print("Conjunto de números reais:")
for numero in numeros:
    print(numero)

print("Conjunto de quadrados:")
for quadrado in quadrados:
    print(quadrado)