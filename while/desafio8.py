# Elabore um programa que calcule a média de valores inseridos até que o usuário finalize.

total = 1
temp = 0
media = 0

while True:
    try:
        num = float(input('Informe um número qualquer ( 0 finaliza o programa ):   '))
    except ValueError:
        print('Isso não é um número!')
        continue      
        
    temp += num

    if num == 0:
        break
    elif num > 0:
        media = temp / total
        total += 1

print(f'A média dos valores será de {media}') 