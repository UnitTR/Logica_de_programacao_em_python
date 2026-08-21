# Crie um programa que classifique um triângulo quanto aos lados.

# Leitura dos lados
a = float(input("Informe a base do triângulo em metros: "))
b = float(input("Informe um dos lados do triângulo em metros: "))
c = float(input("Informe o outro lado do triângulo em metros: "))

# Função para checar se os lados formam um triângulo
def eh_triangulo(x, y, z):
    return (x + y > z) and (x + z > y) and (y + z > x)

# Função de comparação com tolerância para floats
def iguais(x, y, eps=1e-9):
    return abs(x - y) <= eps

if not eh_triangulo(a, b, c):
    print("Não é possível formar um triângulo com esses lados.")
else:
    if iguais(a, b) and iguais(b, c):
        print("O seu triângulo é equilátero!")
    elif iguais(a, b) or iguais(a, c) or iguais(b, c):
        print("O seu triângulo é isósceles!")
    else:
        print("O seu triângulo é escaleno!")