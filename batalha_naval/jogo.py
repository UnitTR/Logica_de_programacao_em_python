
# Criando um tabuleiro

tabuleiro = [
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

navio_linha = 3
navio_coluna = 3

tentativas = 0

while True:

    linha = int(input("Informe a linha onde está o navio!: "))
    coluna = int(input("Informe a coluna onde está o navio!: "))
    
    tentativas += 1

    if tentativas == 3:
        tabuleiro [linha][coluna] = "O"
        print("Suas tentativas acabaram!")
        for linha in tabuleiro:
            print(linha)
        break

    if linha == navio_linha and coluna == navio_coluna:
        tabuleiro [navio_linha][navio_coluna] = "X"        
        print("Você venceu em" ,tentativas,"tentativas.")
        for linha in tabuleiro:
            print(linha)
        break
    else:
        tabuleiro [linha][coluna] = "O"
        print("Você errou!")

    for linha in tabuleiro:
        print(linha)
