matriz_A = [
[1 , 2],
[1 , 2]
]

matriz_B = [
    [1 , 7],
    [7 , 1]
]

matriz_C = [
    [7 , 9],
    [2 , 4]
]

num1 = matriz_A [0][0] + matriz_B [0][0]
num2 = matriz_A [0][1] + matriz_B [0][1]
num3 = matriz_A [1][0] + matriz_B [1][0]
num4 = matriz_A [1][1] + matriz_B [1][1]

matriz_d = [
    [num1, num2],
    [num3, num4]
]

for linha in matriz_d:
    print(linha)

