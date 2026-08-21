#Crie um programa que peça um valor em reais e mostre o valor com 10% de desconto.
reais = float(input(f'Qual o valor do produto? R$:  '))
desconto = reais / 10

print(f'Este produto de R${reais} terá um desconto de R${desconto}!')