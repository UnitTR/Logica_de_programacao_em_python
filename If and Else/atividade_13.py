#  Desenvolva um programa que calcule multa com base na velocidade excedida.

velocidade = float(input("Informe a velocidade do veículo em kilometros por hora:        ")) # rua de 30 Km/h

if (velocidade > 0 and velocidade <= 30):
    print("Não há multa!")
elif (velocidade > 30 and velocidade <= 60):
    print("Multa de R$100,00")
elif (velocidade > 60 and velocidade <= 90):
    print("Multa de R$300,00")
elif (velocidade > 90 and velocidade <= 120):
    print("Multa de R$500,00")
else: 
    print(f'{velocidade} Km/h + 4 rodas = 7 palmos debaixo da terra. A conta pode não bater, mas você pode') 
