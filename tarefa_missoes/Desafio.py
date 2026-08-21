# utilizando listas com o python

import os

arquivos = os.listdir("C:/Users/lucas.falmeida13/OneDrive - SENAC - SP/Documentos/UC9/Atividades fluxograma")
lista_arquivos = []

# Para salvar o nome dos arquivos em nossa lista

for arquivo in arquivos:
    lista_arquivos.append(arquivo)

#Para exibir a nossa lista

for item in lista_arquivos:
    print(item)

qnt_de_arquivos = (len(lista_arquivos))

print(f"Está lista possui", qnt_de_arquivos, "arquivos!")

