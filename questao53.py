import random

def gerar_cartela():
    numeros_disponiveis = list(range(100))  
    random.shuffle(numeros_disponiveis)    

    cartela = []
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(numeros_disponiveis[i * 5 + j])
        cartela.append(linha)
    
    return cartela

def imprimir_cartela(cartela):
    print("Cartela de Bingo:")
    for linha in cartela:
        print(linha)

def main():
    cartela = gerar_cartela()
    imprimir_cartela(cartela)

if __name__ == "__main__":
    main()
