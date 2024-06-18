vetor = []
num = 1

while len(vetor) < 100:
    if num % 7 != 0 and num % 10 != 7:
        vetor.append(num)
    num += 1

print("Vetor com os 100 primeiros naturais que não são múltiplos de 7 ou terminam com 7:")
print(vetor)
