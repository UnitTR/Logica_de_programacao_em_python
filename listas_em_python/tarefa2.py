# Crie uma lista com 10 frutas. Adicione uma nova fruta à lista. Após isso, remova uma fruta e imprima a lista no final

frutas = [f"Maça","Pera","Laranja","Manga","Limão","Tangerina","Banana","Caju","Uva","Abacate"]

frutas.append("Amora")

frutas.remove("Caju")

for fruta in frutas:
    print(fruta)