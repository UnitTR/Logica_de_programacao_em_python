# Desafio - Desenvolva um programa que peça um número ao usuário e exiba a tabuada desse número de 1 até 10 utilizando while.

num = int(input('Informe um número:    '))

contador = 1

while contador < 11:
    calculo = contador * num
    print(f'{contador} X {num} = {calculo}')
    contador = contador + 1



    