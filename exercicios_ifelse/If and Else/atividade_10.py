# Desenvolva um sistema que calcule imposto de renda com base em faixas salariais.

salario = float(input("Informe seu salário mensal:   R$"))

# | Rendimento mensal (R$) | Base de cálculo (R$)     | Alíquota do IR (%) | Parcela a deduzir (R$) |
# | ---------------------- | ------------------------ | ------------------ | ---------------------- |
 #| Até 3.036              | Até 2.428,80             | 0                  | 0                      |
 #| De 3.036 a 3.533,31    | De 2.428,81 até 2.826,65 | 7,5                | 182,16                 |
 #| De 3.533,31 a 4.688,85 | De 2.826,66 até 3.751,05 | 15                 | 394,16                 |
 #| De 4.688,85 a 5.830,85 | De 3.751,06 até 4.664,68 | 22,5               | 675,49                 |
 #| Acima de 5.830,85      | Acima de 4.664,68        | 27,5               | 908,73                 |

 # IR = (Base de Cálculo X Alíquota) − Parcela a Deduzir

if (salario < 3036.00):
    imposto1 = (2428.80 * 0) - 0
    print(f'Seu montante de imposto de renda será de R${imposto1}')
elif (salario > 3036.00 and salario <= 3533.31):
    imposto2 = (2826.65 * 0.075) - 182.16
    print(f'Seu montante de imposto de renda será de R${imposto2}')
elif (salario > 3533.31 and salario <= 4688.85):
    imposto3 = (3751.05 * 0.15) - 394.16
    print(f'Seu montante de imposto de renda será de R${imposto3}')
elif (salario > 4688.85 and salario <= 5830.85):
    imposto4 = (4664.68 * 0.225) - 675.49
    print(f'Seu montante de imposto de renda será de R${imposto4}')
else: 
    (salario > 5830.85 )
    imposto5 = (5000.00 * 0.275) - 908.73
    print(f'Seu montante GENEROSO de imposto de renda será de R${imposto5}')