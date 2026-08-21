# Neste passo, você deverá informar um nome e o programa deve verificar e exibir se existe um arquivo com esse nome na lista de arquivos que você descobriu.

nome = input("Informe o nome do arquivo:  ")

import os

arquivos = os.listdir("C:/Users/lucas.falmeida13/OneDrive - SENAC - SP/Documentos/UC9/Atividades fluxograma")
lista_arquivos = []

# Para salvar o nome dos arquivos em nossa lista

for arquivo in arquivos:
    lista_arquivos.append(arquivo)

for arquivo in lista_arquivos:
    if nome == arquivo:
        print("Este é o arquivo que você estava procurando?", nome, "Ele está na posição:")
    else:
        print("Arquivo não encontrado")

