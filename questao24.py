alunos = []

print("Digite o número do aluno e sua altura em metros:")
for i in range(10):
    numero_aluno = int(input(f"Digite o número do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura do {i+1}º aluno em metros: "))
    alunos.append((numero_aluno, altura))

aluno_mais_baixo = alunos[0]
aluno_mais_alto = alunos[0]

for aluno in alunos:
    if aluno[1] < aluno_mais_baixo[1]:
        aluno_mais_baixo = aluno
    if aluno[1] > aluno_mais_alto[1]:
        aluno_mais_alto = aluno

print("\nAluno mais baixo:")
print(f"Número do aluno: {aluno_mais_baixo[0]}, Altura: {aluno_mais_baixo[1]} metros")
print("\nAluno mais alto:")
print(f"Número do aluno: {aluno_mais_alto[0]}, Altura: {aluno_mais_alto[1]} metros")
