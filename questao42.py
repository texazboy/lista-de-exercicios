linhas = 3
colunas = 3

matriz = [[0]*colunas for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = i * j

print("Matriz preenchida com o produto da linha pelo índice da coluna:")
for linha in matriz:
    print(linha)
