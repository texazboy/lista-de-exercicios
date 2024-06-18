notas = []

print("Digite as notas dos 15 alunos:")
for i in range(15):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

soma_notas = sum(notas)
media_geral = soma_notas / len(notas)

print(f"\nMédia geral das notas: {media_geral:.2f}")
