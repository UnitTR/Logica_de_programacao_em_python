# Neste passo, você deverá criar um sistema de busca. O usuário digita uma palavra e o programa mostra todos os arquivos que contenham essa palavra em seu diretório.

import os

nome = input("Informe o nome do arquivo: ")

lista_arquivos = os.listdir("C:/Users/lucas.falmeida13/OneDrive - SENAC - SP/Documentos/UC9/Atividades fluxograma")

def verifica(nome, lista):
    encontrados = []

    for arquivo in lista:
        if nome.lower() in arquivo.lower():  # lower() para busca sem diferenciar maiúsculas
            encontrados.append(arquivo)

    if encontrados:
        print(f"\nArquivos encontrados com '{nome}':")
        for item in encontrados:
            print(f"  - {item}")
    else:
        print(f"\nNenhum arquivo encontrado com '{nome}'.")

verifica(nome, lista_arquivos)
