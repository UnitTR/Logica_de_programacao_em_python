# Imposto de renda de SIMPLICADO

salario = float(input("Informe o seu salário mensal: R$ "))

# A cada R$2500,00 a porcentagem sobe
# Até R$5000,00 não paga imposto de renda

imposto1 = salario * 0.075 # 7.5%
imposto2 = salario * 0.150 # 15.0%
imposto3 = salario * 0.225 # 22.5%
imposto4 = salario * 0.275 # 27.5%

# Cálculo do imposto de renda simplificado 
# Imposto = Salário * Porcentagem do imposto com base no salário mensal

if (salario <= 5000):
    print("Isento do imposto!")
elif (salario > 5000 and salario <= 7500):
    print("Você pagará no total de imposto de renda: R$",imposto1)
elif (salario > 7500 and salario <= 10000):
    print("Você pagará no total de imposto de renda: R$",imposto2)
elif (salario > 10000 and salario <= 12500):
    print("Você pagará no total de imposto de renda: R$",imposto3)
else:
    (salario > 12500)
    print("Você pagará no total de imposto de renda: R$", imposto4)

