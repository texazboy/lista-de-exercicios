primeiro_vetor = []

print("Digite 10 números inteiros no intervalo [0, 50]:")
for i in range(10):
    while True:
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        if 0 <= numero <= 50:
            primeiro_vetor.append(numero)
            break
        else:
            print("Número fora do intervalo permitido. Digite novamente.")

segundo_vetor = [num for num in primeiro_vetor if num % 2 != 0]

print("\nElementos do primeiro vetor e do segundo vetor (apenas ímpares):")
for i in range(10):
    if i < len(primeiro_vetor):
        print(f"{primeiro_vetor[i]:2}", end=" ")
    else:
        print("   ", end=" ")

    if i < len(segundo_vetor):
        print(f"{segundo_vetor[i]:2}")
    else:
        print()

if len(primeiro_vetor) > 10:
    for i in range(10, len(primeiro_vetor)):
        print(f"   {segundo_vetor[i]:2}")
