valores = []

print("Digite 5 valores:")
for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

media = sum(valores) / len(valores)

print("\nValores lidos:", valores)
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")
