# Crie um programa que classifique um triângulo quanto aos lados.

base_A = float(input("Informe a base do triângulo em metros:    "))
base_B = float(input("Informe um dos lados do triângulo em metros:     "))
base_C = float(input("Informe o outro lado do triângulo em metros:   "))

if (base_A == base_B and base_B == base_C):
    print("O seu triângulo é equilátero!")
elif (base_A != base_B or base_C):
    print("O seu triângulo é isósceles!")
elif (base_A != base_B and base_B != base_C):
    print("O seu triângulo é escaleno!")