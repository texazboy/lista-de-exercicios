vetor = []

print("Digite os 10 valores do vetor:")
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i+1}: "))
    vetor.append(valor)

cont_pares = 0

for num in vetor:
    if num % 2 == 0:
        cont_pares += 1

print(f"O vetor possui {cont_pares} valores pares.")
