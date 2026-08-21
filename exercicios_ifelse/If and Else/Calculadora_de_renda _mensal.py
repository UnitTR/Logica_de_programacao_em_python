# Está análizará sua renda mensal e irá lhe informar sua classe social!

renda = float(input("Informe sua renda mensal:    R$ "))

if (renda >= 25200.0):
    print("Sua classe social é A!")
elif (renda > 25200.0 and renda >= 8100.0):
    print("Sua classe social é B!")
elif (renda > 8100.0 and renda >= 3400.0):
    print("Sua classe social é C!")
else:
    print("Sua classe social é D/E!")
