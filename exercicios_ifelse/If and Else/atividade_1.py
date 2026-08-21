#  Desenvolva um programa que receba um número e informe se ele é positivo, negativo ou zero.

num =  float(input("Informe um número qualquer:   "))

if (num < 0):
    print("Este número é negativo!")
elif (num > 0):
    print("Este número é positivo!")
elif (num == 0):
    print("O seu número é zero?")
