# 

import pandas as pd

df = pd.read_excel("C:/Users/lucas.falmeida13/OneDrive - SENAC - SP/Book.xlsx")
print(df.head())

lst_objetos_py = []

for i in df:
    lst_objetos_py.append(i)

for i in df:
    if i == "cabo".lower():
        print(f'Pallavra chave pra finalizaão da aplicação utilizada - CABO')
        break
    else:
        print(i) 