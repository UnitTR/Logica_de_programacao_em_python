# Neste passo, você deverá contar arquivos por tipo. Você precisará utilizar listas, condicionais e contadores.

# Tipos de Arquivos: .pdf , .word, .xls, .txt, etc...
# Exemplo de resultado:
# .pdf = 5
# .word = 2
# .xls = 0

import os

lista_arquivos = os.listdir("C:/Users/lucas.falmeida13/OneDrive - SENAC - SP/Documentos/UC9/Atividades fluxograma")

# Contadores por tipo
pdf   = 0
word  = 0
xls   = 0
txt   = 0
outro = 0

for arquivo in lista_arquivos:
    if arquivo.endswith(".pdf"):
        pdf += 1
    elif arquivo.endswith(".docx") or arquivo.endswith(".doc"):
        word += 1
    elif arquivo.endswith(".xlsx") or arquivo.endswith(".xls"):
        xls += 1
    elif arquivo.endswith(".txt"):
        txt += 1
    else:
        outro += 1

print(f".pdf  = {pdf}")
print(f".word = {word}")
print(f".xls  = {xls}")
print(f".txt  = {txt}")
print(f"outro = {outro}")

