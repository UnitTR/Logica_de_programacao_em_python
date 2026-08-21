# Desenvolva um programa que receba a idade de uma pessoa e informe se ela é criança, adolescente, adulta ou idosa. Considere adolescente a partir dos 12 até os 17 e idoso acima de 60.

idade = int(input("Informe sua idade:   "))

if (idade < 12 ):
    print("Você é uma criança?")
elif (idade >= 12 and idade <= 17 ):
    print("Você é um adolescente?")
elif (idade >= 18 and idade < 60 ):
    print("Você é um adulto?")
elif (idade >= 60 and idade <= 130 ):
    print("Você é um idoso?")
else:
    print("Viajou no tempo fdp?")