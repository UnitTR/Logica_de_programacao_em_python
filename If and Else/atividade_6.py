# Crie um sistema de login simples que valide usuário e senha.

email = str(input("Digite seu e-mail:             ")) #admin1234@gmail.com
senha = int(input("Digite sua senha:              ")) #1234

email_correto = str("admin1234@gmail.com")
senha_correta = int(1234)

if (email == email_correto and senha == senha_correta):
    print("Bem vindo! Acesso concedido!")
else:
    print("Acesso negado! Verifique seu e-mail e senha e tente novamente.")
