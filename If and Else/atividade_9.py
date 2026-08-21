#  Crie um programa que verifique se um número é múltiplo de 3 e de 5 simultaneamente.

num = float(input("Informe um número qualquer:    "))

if (num % 15 == 0):
    print("Este número é divisível simultaneamente por 3 e 5! ")
else:
    print("Este número não é divisível por 3 e 5 simultaneamente!")