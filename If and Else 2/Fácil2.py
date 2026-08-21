# Crie um programa que receba uma senha numérica e informe se ela está correta. Considere que a senha correta é “adminadmin”.

senha = str(input("Informe a senha corretamente:     "))

senha_correta =  str("adminadmin")

if(senha == senha_correta):
    print("Senha correta! Pode entrar!")
else:
    print("Boa tentativa, tente novamente!")