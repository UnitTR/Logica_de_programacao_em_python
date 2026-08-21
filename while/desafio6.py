# Desenvolva um programa que continue solicitando números até que o usuário digite 0 e mostre a soma total.

total = 0

while True:
    try:
        num = int(input("Informe um número (0 encerra): "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if num == 0:
        print(f"Soma total: {total}")
        print("Encerrando o programa. Parabéns!")
        break

    total += num

