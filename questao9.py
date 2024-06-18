def eh_par(numero):
    return numero % 2 == 0

valores = []

print("Digite 6 valores inteiros pares:")
contador = 0
while contador < 6:
    valor = int(input(f"Digite o {contador+1}º valor inteiro par: "))
    if eh_par(valor):
        valores.append(valor)
        contador += 1
    else:
        print("O valor digitado não é par. Por favor, digite um número inteiro par.")

print("\nValores na ordem inversa:")
for i in range(5, -1, -1):
    print(valores[i])
