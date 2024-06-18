def ler_respostas_alunos():
    matriz_respostas = []
    print("Digite as respostas dos alunos (a, b, c ou d):")
    for i in range(5):
        linha = []
        for j in range(10):
            resposta = input(f"Digite a resposta do aluno {i+1} para a questão {j+1}: ")
            linha.append(resposta)
        matriz_respostas.append(linha)
    return matriz_respostas

def ler_gabarito():
    gabarito = []
    print("\nDigite o gabarito de respostas (a, b, c ou d):")
    for i in range(10):
        resposta = input(f"Digite a resposta correta para a questão {i+1}: ")
        gabarito.append(resposta)
    return gabarito

def calcular_pontuacao(matriz_respostas, gabarito):
    resultado = []
    for aluno_respostas in matriz_respostas:
        pontuacao = 0
        for i in range(10):
            if aluno_respostas[i] == gabarito[i]:
                pontuacao += 1
        resultado.append(pontuacao)
    return resultado

def main():
    matriz_respostas = ler_respostas_alunos()
    gabarito = ler_gabarito()
    
    resultado = calcular_pontuacao(matriz_respostas, gabarito)

    print("\nPontuação de cada aluno:")
    for i, pontuacao in enumerate(resultado):
        print(f"Aluno {i+1}: {pontuacao} pontos")

if __name__ == "__main__":
    main()
