# Crie um programa que verifique se um número é múltiplo de 3 e de 5 simultaneamente.

num = float(input("Informe um número qualquer:    "))

if ((num % 3 ) == 0 and (num % 5) == 0):
    print("Este número é divisivel tanto por 3 quanto por 5!")
else:
    print("Este número não é divisivel por 3 e por 5 simultaneamente!")