# Crie um sistema de autenticação com limite de três tentativas de senha.

senha_correta = "admin123"
tentativas = 3

while tentativas > 0:
    senha = input("Informe sua senha: ")

    if senha == senha_correta:
        print("Senha correta, pode entrar!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta, tentativas restantes: {tentativas}")
        else:
            print("Senha incorreta. Você excedeu o número de tentativas.")