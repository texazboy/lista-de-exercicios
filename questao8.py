valores = []

print("Digite 6 valores inteiros:")
for i in range(6):
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    valores.append(valor)

print("\nValores na ordem inversa:")
for i in range(5, -1, -1):
    print(valores[i])
