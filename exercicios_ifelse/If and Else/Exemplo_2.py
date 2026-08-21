# Verificação da classe social

temp = float(input("Informe sua temperatura em graus:    "))
if (temp <= 35.0): # Hiportemia
    print("Olá picolé!")
elif (temp >= 35.1 and temp <= 35.9):
    print("Hiportemia leve")
elif (temp > 35.0 and temp <= 37.5): # Normal
    print("Você está bem!")
elif (temp > 37.5 and temp <= 39.5): # Febre   
    print("É só uma gripezinha!") 
elif (temp > 39.5 and temp <= 41.0): # Febre alta
    print("Você está com frebre alta!")  
else: # Hipertemia
    print("Em chamas! kkkkk")                                                                                                                                                                                                                                                                                                                                                                                                                        