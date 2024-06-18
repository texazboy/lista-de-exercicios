matriz = []

print("Digite os elementos da matriz 5x5:")
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

x = int(input("Digite o valor que deseja buscar na matriz: "))

encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            print(f"O valor {x} foi encontrado na posição [{i}][{j}]")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print(f"O valor {x} não foi encontrado na matriz.")
