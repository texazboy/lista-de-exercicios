A = [1, 2, 3, 4, 5, 6, 20, 18, 16, 14, 12]

parte1 = A[:6]
parte2 = A[6:]

parte1.sort()
parte2.sort(reverse=True)

A_ordenado = parte1 + parte2

print("Vetor ordenado:")
print(A_ordenado)
