def numero_para_vetor(num):
    return [int(digito) for digito in str(num)]

a = int(input("Digite o primeiro número (positivo e menor que 10000): "))
b = int(input("Digite o segundo número (positivo e menor que 10000): "))

vetor_a = numero_para_vetor(a)
vetor_b = numero_para_vetor(b)

vetor_a.reverse()
vetor_b.reverse()

soma = []
carry = 0
max_len = max(len(vetor_a), len(vetor_b))

for i in range(max_len):
    digito_a = vetor_a[i] if i < len(vetor_a) else 0
    digito_b = vetor_b[i] if i < len(vetor_b) else 0

    total = digito_a + digito_b + carry
    soma.insert(0, total % 10)
    carry = total // 10

if carry:
    soma.insert(0, carry)

print(f"Vetor de a: {vetor_a}")
print(f"Vetor de b: {vetor_b}")
print(f"Soma de a e b (vetorizado): {soma}")
