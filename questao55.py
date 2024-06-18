def ler_gabarito():
    gabarito = []
    print("Digite o gabarito de respostas (a, b, c, d ou e):")
    for i in range(10):
        resposta = input(f"Digite a resposta correta para a questão {i+1}: ")
        gabarito.append(resposta)
    return gabarito

def ler_respostas_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    respostas = []
    for i in range(10):
        resposta = input(f"Digite a resposta do aluno para a questão {i+1}: ")
        respostas.append(resposta)
    return matricula, respostas

def calcular_nota(respostas_aluno, gabarito):
    nota = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    return nota

def calcular_percentual_aprovacao(notas):
    aprovados = sum(1 for nota in notas if nota >= 7.0)
    percentual_aprovacao = (aprovados / len(notas)) * 100
    return percentual_aprovacao

def main():
    gabarito = ler_gabarito()
    print("\nGabarito registrado com sucesso.\n")

    notas = []
    for i in range(3):
        print(f"Aluno {i+1}:")
        matricula, respostas_aluno = ler_respostas_aluno()
        nota = calcular_nota(respostas_aluno, gabarito)
        notas.append(nota)
        print(f"Matrícula: {matricula}")
        print(f"Respostas: {respostas_aluno}")
        print(f"Nota: {nota}\n")

    percentual_aprovacao = calcular_percentual_aprovacao(notas)
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")

if __name__ == "__main__":
    main()
