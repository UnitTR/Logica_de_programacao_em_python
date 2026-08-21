# Elabore um sistema que avalie concessão de empréstimo com base em idade e renda.

idade = int(input("Informe sua idade:  "))
renda = float(input("Informe sua renda:   ")) # a partir de um salário minímo
emprestimo = float(input("Informe quanto você quer de empréstimo:    "))

salario_minimo = 1620.0       # salário mínimo utilizado como referência (exemplo)
parcela_maxima = 0.30     # 30% da renda

prestacao_mensal = emprestimo / 12.0
parcela_permitida = renda * parcela_maxima

if idade < 18:
    print("Não é elegível: idade inferior a 18 anos.")
elif renda < salario_minimo:
    print("Não é elegível: renda abaixo do salário mínimo.")
elif prestacao_mensal <= parcela_permitida:
    print("Parabéns! Você consegue pegar este empréstimo.")
else:
    print("Perdão! Você não consegue pegar este empréstimo.")