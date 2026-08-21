# Desafio Extra

livro = {
    "Título" : "Artes da guerra",
    "Autor" : "Sun Tzu",
    "Ano de publicação" : 1900
}

print("O título do livro é: " , (livro["Título"]))

livro["Ano de publicação"] = 1993

livro ["Quantidade de páginas"] = 97

for item in livro:
    print((item) , ":" , livro[item])
