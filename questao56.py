def ler_notas():
    matriz_notas = []
    print("Digite as notas dos alunos:")
    for i in range(10):
        notas = []
        for j in range(3):
            nota = float(input(f"Digite a nota do aluno {i+1} na prova {j+1}: "))
            notas.append(nota)
        matriz_notas.append(notas)
    return matriz_notas

def determinar_pior_nota_alunos(notas):
    pior_nota_prova1 = 0
    pior_nota_prova2 = 0
    pior_nota_prova3 = 0

    for aluno in notas:
        if aluno[0] == min(aluno):
            pior_nota_prova1 += 1
        elif aluno[1] == min(aluno):
            pior_nota_prova2 += 1
        elif aluno[2] == min(aluno):
            pior_nota_prova3 += 1
    
    return pior_nota_prova1, pior_nota_prova2, pior_nota_prova3

def main():
    notas = ler_notas()

    pior_nota_prova1, pior_nota_prova2, pior_nota_prova3 = determinar_pior_nota_alunos(notas)

    print(f"\nNúmero de alunos cuja pior nota foi na prova 1: {pior_nota_prova1}")
    print(f"Número de alunos cuja pior nota foi na prova 2: {pior_nota_prova2}")
    print(f"Número de alunos cuja pior nota foi na prova 3: {pior_nota_prova3}")

if __name__ == "__main__":
    main()
