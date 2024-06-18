def ler_matriz():
    matriz = []
    print("Digite as informações dos alunos:")
    for i in range(5):
        aluno = []
        print(f"\nAluno {i+1}:")
        matricula = int(input("Digite o número de matrícula: "))
        media_provas = int(input("Digite a média das provas: "))
        media_trabalhos = int(input("Digite a média dos trabalhos: "))
        aluno.append(matricula)
        aluno.append(media_provas)
        aluno.append(media_trabalhos)
        aluno.append(media_provas + media_trabalhos) 
        matriz.append(aluno)
    return matriz

def encontrar_maior_nota_final(matriz):
    maior_nota = matriz[0][3]
    matricula_maior_nota = matriz[0][0]
    for aluno in matriz:
        if aluno[3] > maior_nota:
            maior_nota = aluno[3]
            matricula_maior_nota = aluno[0]
    return matricula_maior_nota

def calcular_media_notas_finais(matriz):
    soma_notas_finais = sum(aluno[3] for aluno in matriz)
    media_notas_finais = soma_notas_finais / len(matriz)
    return media_notas_finais

def main():
    matriz_alunos = ler_matriz()

    matricula_maior_nota = encontrar_maior_nota_final(matriz_alunos)
    print(f"\nMatrícula do aluno com a maior nota final: {matricula_maior_nota}")

    media_notas_finais = calcular_media_notas_finais(matriz_alunos)
    print(f"Média das notas finais: {media_notas_finais:.2f}")

if __name__ == "__main__":
    main()
