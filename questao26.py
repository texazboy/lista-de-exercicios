import math

v = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

media = sum(v) / len(v)

soma_quadrados_diff = sum((x - media)**2 for x in v)

desvio_padrao = math.sqrt(soma_quadrados_diff / len(v))

print(f"Vetor v: {v}")
print(f"Média: {media}")
print(f"Desvio padrão: {desvio_padrao}")
