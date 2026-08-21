# Elabore um programa que mostre a tabuada de um número informado.

num = int(input('Informe um número:    '))

contador = 1

while contador < 11:
    calculo = contador * num
    print(f'{contador} X {num} = {calculo}')
    contador = contador + 1


