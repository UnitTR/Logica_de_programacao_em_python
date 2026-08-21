# Pedindo os números da matriz

num1 = input("Informe um número para a posição [0][0] da matriz: ")
num2 = input("Informe um número para a posição [0][1] da matriz: ")
num3 = input("Informe um número para a posição [0][2] da matriz: ")
num4 = input("Informe um número para a posição [1][0] da matriz: ")
num5 = input("Informe um número para a posição [1][1] da matriz: ")
num6 = input("Informe um número para a posição [1][2] da matriz: ")
num7 = input("Informe um número para a posição [2][0] da matriz: ")
num8 = input("Informe um número para a posição [2][1] da matriz: ")
num9 = input("Informe um número para a posição [2][2] da matriz: ")

matriz_3x3 = [
    [num1, num2, num3],
    [num4, num5, num6],
    [num7, num8, num9]
]

# Mostrando a coluna 2 (índice 2) na tela

print("Coluna 2 da matriz:")
for linha in matriz_3x3:
    print(linha[2])