def imprimir_ordem_direta(vetor):
    print("Vetor na ordem direta:")
    for num in vetor:
        print(num, end=" ")
    print()

def imprimir_ordem_inversa(vetor):
    print("Vetor na ordem inversa:")
    for num in reversed(vetor):
        print(num, end=" ")
    print()

vetor = []

print("Digite 5 números reais para preencher o vetor:")
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(numero)

codigo = int(input("\nDigite um código (0 para finalizar, 1 para ordem direta, 2 para ordem inversa): "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    imprimir_ordem_direta(vetor)
elif codigo == 2:
    imprimir_ordem_inversa(vetor)
else:
    print("Código inválido. Digite 0, 1 ou 2.")
