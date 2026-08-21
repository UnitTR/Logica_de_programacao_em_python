# 1 - Ana
# 2 - Bruno
# 3 - Carlos

# numeros = range(1,11)

# for numero in numeros:

#0,1,2,3,4,5,6,7,8,9,10
eleitores = range (11)

for eleitor in eleitores:
    print(f'\nCANDIDATOS:')
    print(f'O - Voto em branco')
    print(f'1 - Ana')
    print(f'2 - Bruno')
    print(f'3 - Carlos')

    voto = input("Informe o número do seu eleitor!: ")
    
    contador_Nulo = []
    contador_Ana = []
    contador_Bruno = []
    contador_Carlos = []
    
    if voto == 1:
        contador_Ana += 1
    elif voto == 2:
        contador_Bruno += 1
    elif voto == 3:
        contador_Carlos += 1
    elif voto == 0:
        if contador_Ana > contador_Bruno and contador_Carlos:
            contador_Ana += 1
        elif contador_Bruno > contador_Ana and contador_Carlos:
            contador_Bruno += 1
        elif contador_Carlos > contador_Ana and contador_Bruno:
            contador_Carlos += 1

    # if voto in lst_de_votos == 1:
    #     contador_Ana += 1
    # elif voto in lst_de_votos == 2:
    #     contador_Bruno += 1
    # elif voto in lst_de_votos == 3:
    #     contador_Carlos += 1
    # elif voto in lst_de_votos == 0:
    #     if contador_Ana > contador_Bruno and contador_Carlos:
    #         contador_Ana += 1
    #     elif contador_Bruno > contador_Ana and contador_Carlos:
    #         contador_Bruno += 1
    #     elif contador_Carlos > contador_Ana and contador_Bruno:
    #         contador_Carlos += 1
    #     else:
    #         print(f'Todos os candidatos estão empatados!, tem certeza que quer manter sua escolha?')
    print(f'\n==== RESULTADO FINAL ====')
    print(f'Ana: {contador_Ana} voto(s)')
    print(f'Bruno: {contador_Bruno} voto(s)')
    print(f'Carlos: {contador_Carlos} voto(s)')
    print(f'Branco: {contador_Nulo} voto(s)')
for voto in eleitores:
    if contador_Ana > contador_Bruno and contador_Carlos:
        print(f'Ana ganhou a eleição com {contador_Ana}')
    elif contador_Bruno > contador_Ana and contador_Carlos:
        print(f'Ana ganhou a eleição com {contador_Bruno}')
    elif contador_Carlos > contador_Ana and contador_Bruno:
        print(f'Ana ganhou a eleição com {contador_Carlos}')
    else:
        print(f'Tivemos um empate!')
