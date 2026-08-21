saldo = 0
historico = []

def formatar(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def depositar():
    try:
        valor = float(input("Valor para depositar: R$ "))
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            return
        global saldo
        saldo += valor
        historico.append(("Depósito", valor, saldo))
        print(f"Depósito de {formatar(valor)} realizado! Saldo atual: {formatar(saldo)}")
    except ValueError:
        print("Valor inválido!")

def sacar():
    try:
        valor = float(input("Valor para sacar: R$ "))
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            return
        global saldo
        if valor > saldo:
            print("Saldo insuficiente!")
            return
        saldo -= valor
        historico.append(("Saque", valor, saldo))
        print(f"Saque de {formatar(valor)} realizado! Saldo atual: {formatar(saldo)}")
    except ValueError:
        print("Valor inválido!")

def extrato():
    print("\n===== EXTRATO =====")
    if not historico:
        print("Nenhuma transação realizada.")
    else:
        for tipo, valor, saldo_pos in historico:
            sinal = "+" if tipo == "Depósito" else "-"
            print(f"{tipo}: {sinal}{formatar(valor)} | Saldo: {formatar(saldo_pos)}")
    print(f"\nSaldo atual: {formatar(saldo)}")
    print("===================\n")

opcoes = {
    "1": ("Depositar", depositar),
    "2": ("Sacar", sacar),
    "3": ("Extrato", extrato),
}

print("=== Banco PySimples ===")
while True:
    print("\n1 - Depositar\n2 - Sacar\n3 - Extrato\n0 - Sair")
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "0":
        print("Encerrando. Até logo!")
        break
    elif escolha in opcoes:
        nome, funcao = opcoes[escolha]
        funcao()
    else:
        print("Opção inválida. Tente novamente.")