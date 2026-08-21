# Neste passo, você deverá exibir apenas arquivos com a extensão .pdf .

import os

arquivos = os.listdir("C:/Users/lucas.falmeida13/OneDrive - SENAC - SP/Documentos/UC9/Atividades fluxograma")
lista_arquivos = []

for arquivo in arquivos:
    lista_arquivos.append(arquivo)

# Filtra e exibe apenas arquivos .pdf

encontrou_pdf = False

for item in lista_arquivos:
    if item.endswith('.pdf'):        # Tipo arduino começa falso e se tal coisa for verdadeira print(Item)
        print(item)
        encontrou_pdf = True

if not encontrou_pdf:               # Função not, não sei bem como usar mas é intuitivo
    print("Não tem nenhum arquivo com este sufixo!")

qnt_de_arquivos = len(lista_arquivos)
print(f"Esta lista possui {qnt_de_arquivos} arquivos!")