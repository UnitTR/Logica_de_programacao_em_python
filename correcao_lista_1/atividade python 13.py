#Faça um programa que peça um valor e mostre o valor com 15% de aumento.
reais = float(input(f'Qual o valor do produto? R$:  '))
aumento = reais * 0.15

total = reais + aumento

print(f'Este produto de R${reais} terá um aumento de R${aumento}, logo seu produto custará R${total}!')