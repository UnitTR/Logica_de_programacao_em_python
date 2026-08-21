# Elabore um programa que aplique desconto com base em faixas de valor de compra.

valor = float(input("Informe o valor da sua compra:   R$"))

temp = valor

if (valor >= 100.00 and valor < 200.00):   # A cada R$100,00 em compras o desconto sobe 5%
    valor_com_10 = temp - (valor * 0.10) 
    print(f'Você tem um desconto de 10%, sua compra com desconto será R${valor_com_10} !') 
elif (valor >= 200.00 and valor < 300.00):   # A cada R$100,00 em compras o desconto sobe 5%
    valor_com_15 = temp - (valor * 0.15) 
    print(f'Você tem um desconto de 15%, sua compra com desconto será R${valor_com_15} !') 
elif (valor >= 300.00 and valor < 400.00):   # A cada R$100,00 em compras o desconto sobe 5%
    valor_com_20 = temp - (valor * 0.20) 
    print(f'Você tem um desconto de 20%, sua compra com desconto será R${valor_com_20} !') 
elif (valor >= 400.00):   # A cada R$100,00 em compras o desconto sobe 5%
    valor_com_25 = temp - (valor * 0.25) 
    print(f'Você tem um desconto de 25%, sua compra com desconto será R${valor_com_25} !') 
else:
     print("Valor cheio chefe!")
