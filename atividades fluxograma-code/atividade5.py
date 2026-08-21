# Crie um fluxograma que leia duas variáveis A e B, troque os valores entre elas (A recebe B e B recebe A). Mostre os novos valores.
a = int(input("Diga o valor de b:  "))
b = int(input("Diga o valor de a:  "))

temp = a


a = b
b = temp


print(a),print(b)
