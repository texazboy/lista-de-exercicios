valores = []

print("Digite 5 valores:")
for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

posicao_maior = valores.index(maior)
posicao_menor = valores.index(menor)

print("\nPosição do maior valor:", posicao_maior)
print("Posição do menor valor:", posicao_menor)