# Crie um programa em Python utilizando dicionários aninhados (dicionário dentro de dicionário) para gerenciar uma biblioteca digital.

# Cada livro deverá possuir:
# Título
# Autor
# Quantidade de exemplares disponíveis
# Quantidade de empréstimos realizados
# Avaliação média dos leitores

# Sistema de bem vindo

while True:

    biblioteca = []
   
    print("\n")
    print(f'======= Bem vindo a biblioteca digital! =========')
    print("\n")
   
    print(f'1 = Cadastrar um novo livro')
    print(f'2 = Realizar empréstimo')
    print(f'3 = Devolver livro')
    print(f'4 = Consultar livro')
    print(f'5 = Listar todos os livros')
    print(f'6 = Atualizar avaliação')
    print(f'7 = Exibir ranking dos livros')
    print(f'8 = Livro mais emprestado')
    print(f'9 = Livros indisponíveis')
    print(f'10 = Relatório geral')
    print(f'11 = Remover livro')
    print(f'12 = Encerrar programa')

    print("\n")

    analise = int(input(("Informe o que deseja fazer com base na tabela: ")))
    livro = []

    if analise == 1:
        titulo = input("Informe o título do livro: ")
        autor = input("Informe o autor: ")
        exemplares = input("Informe a quantidade de exemplares disponíveis: ")
        emprestimos = input("Informe a quantidade de empréstimos realizados: ")
        leitores = input("Informe a avaliação média dos leitores: ")

        livro = {
        "titulo": titulo,
        "autor": autor,
        "exemplares": exemplares,
        "emprestimos": emprestimos,
        "leitores": leitores
        }
    
        biblioteca.append(livro)  
        print("Cadastro realizado!")

    for livro in biblioteca:
        print((livro))
    
    if analise == 2:
        titulo2 = input("Informe o título do livro: ")
        if titulo2 == biblioteca:
            biblioteca[exemplares] =- 1
            biblioteca[emprestimos] =+ 1
            print('Emprestimo realizado com sucesso')
        else:
            print("Este livro não existe!")

    if analise == 3:
        biblioteca[exemplares] =+ 1
        print("Livro devolvido com sucesso!")

    if analise == 4: # Erro
        busca = input("Informe o título do livro que vc deseja pesquisar: ")
        for livro in biblioteca:
                if livro == "busca":
                    print(livro)
                else:
                    print("Livro não encontrado!")
        
    if analise == 5:
        for livro in biblioteca:
            print(livro)

    if analise == 6:
         
        for livro in biblioteca:
                if livro == "busca":
                    nova_avaliação = input("Qual a nova nota que vc deseja aplicar?")
                else:
                     print("Livro não encontrado!")

    

         
                 




  
#     if analise == 1:
#         titulo1 = input("Informe o título do livro: ")
#         autor1 = input("Informe o autor: ")
#         exemplares1 = input("Informe a quantidade de exemplares disponíveis: ")
#         emprestimos1 = input("Informe a quantidade de empréstimos realizados: ")
#         leitores1 = input("Informe a avaliação média dos leitores: ")
#         print("Cadastro realizado!")
    
#     cadastro.update({
#     "titulo": "titulo1",
#     "ativo": True
#     print(cadastro)
# })

# print(dados)
#     cadastro["titulo"] = titulo1
#     cadastro["autor"] = autor1
#     cadastro["exemplares"] = exemplares1
#     cadastro["emprestimos"] = emprestimos1
#     cadastro["leitores"] = leitores1

#     print(cadastro)




