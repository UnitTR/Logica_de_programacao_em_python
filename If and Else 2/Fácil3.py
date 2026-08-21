# Elabore um programa que receba um turno (“manhã”, “tarde” ou “noite”) e exiba uma mensagem correspondente. Ex: “Bom dia! Bem-vindo” para o turno da manhã e “Boa tarde! Bem-vindo” para o turno da tarde

turno = str(input("Informe o seu turno:     "))

if (turno == str("manha") ):
    print("Bom dia, já tomou seu café?")
elif (turno == str("tarde")):
    print("Boa tarde, já almoçou hj?")
elif (turno == str("noite")):
    print("Boa noite, já jantou hj?")
else: 
    print("Isto é um horário?")