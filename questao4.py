vetor = []

print("Digite os 8 valores do vetor:")
for i in range(8):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    vetor.append(valor)

X = int(input("\nDigite o valor de X (posição no vetor): "))
Y = int(input("Digite o valor de Y (posição no vetor): "))

if 0 <= X < 8 and 0 <= Y < 8:
    soma = vetor[X] + vetor[Y]
    print(f"\nA soma dos valores nas posições {X} e {Y} é: {soma}")
else:
    print("\nErro: Posições X e Y devem estar entre 0 e 7 (inclusive).")
