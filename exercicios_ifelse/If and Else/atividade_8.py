# Desenvolva um sistema que calcule e classifique o IMC

peso = float(input("Informe o seu peso atual, em Kg:     "))
altura = float(input("Informe sua altura atual, em Metros:    "))

altura_m2 = altura * altura

temp = altura_m2

IMC = peso / altura_m2

if (IMC < 18.5):
    print("Você está abaixo do peso!")
elif (IMC >= 18.6 and IMC <= 24.9):
    print("Peso ideal, parabéns!")
elif (IMC >= 25.0 and IMC <= 29.9):
    print("Levemente acima do peso!")
elif (IMC >= 30.0 and IMC <= 34.9):
    print("Obesidade grau I")
elif (IMC >= 35.0 and IMC <= 39.9):
    print("Obesidade grau II (Severa)")
else:
    print("Obesidade grau III (Mórbida)")

