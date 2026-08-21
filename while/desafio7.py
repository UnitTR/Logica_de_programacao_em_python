# Crie um sistema que conte quantos números positivos foram digitados.

total = 0

while True:
    try:
        num = float(input('Informe um número qualquer ( 0 encerra o programa ):   '))
    except ValueError:
        print('Isso não é um número!')
        continue
        
    if num == 0:
        break
    elif num > 0:
        total += 1  # era "soma + 1" (sem atribuição) e usava variável errada

print(f'Você digitou {total} números positivos!')  # estava dentro do loop, imprimia cedo demais