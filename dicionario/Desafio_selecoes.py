# Crie um dicionário para para cada grupo das
# seleções. Você deve contemplar TODAS as seleções
# que estão participando desta copa.

selecoes = {
    # CONMEBOL — América do Sul
    "CONMEBOL": {
        "Brasil":    {"jogos": 3, "vitorias": 3, "empates": 0, "derrotas": 0},  
        "Argentina": {"jogos": 3, "vitorias": 2, "empates": 1, "derrotas": 0},  
        "Colômbia":  {"jogos": 3, "vitorias": 2, "empates": 0, "derrotas": 1}, 
        "Uruguai":   {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Equador":   {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2},  
        "Venezuela": {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2}, 
    },

    # CONCACAF — América do Norte, Central e Caribe
    "CONCACAF": {
        "EUA":           {"jogos": 3, "vitorias": 2, "empates": 1, "derrotas": 0}, 
        "México":        {"jogos": 3, "vitorias": 1, "empates": 2, "derrotas": 0},  
        "Canadá":        {"jogos": 3, "vitorias": 2, "empates": 0, "derrotas": 1},  
        "Panamá":        {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Costa Rica":    {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2},  
        "Jamaica":       {"jogos": 3, "vitorias": 0, "empates": 2, "derrotas": 1},  
        "Honduras":      {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
        "El Salvador":   {"jogos": 3, "vitorias": 0, "empates": 0, "derrotas": 3},  
        "Guatemala":     {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
    },

    # UEFA — Europa
    "UEFA": {
        "Espanha":       {"jogos": 3, "vitorias": 3, "empates": 0, "derrotas": 0},  
        "França":        {"jogos": 3, "vitorias": 2, "empates": 1, "derrotas": 0},  
        "Inglaterra":    {"jogos": 3, "vitorias": 2, "empates": 0, "derrotas": 1},  
        "Portugal":      {"jogos": 3, "vitorias": 2, "empates": 1, "derrotas": 0},  
        "Alemanha":      {"jogos": 3, "vitorias": 2, "empates": 0, "derrotas": 1}, 
        "Países Baixos": {"jogos": 3, "vitorias": 1, "empates": 2, "derrotas": 0},  
        "Bélgica":       {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Croácia":       {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1}, 
        "Suíça":         {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1}, 
        "Áustria":       {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2},  
        "Turquia":       {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2}, 
        "Dinamarca":     {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Hungria":       {"jogos": 3, "vitorias": 0, "empates": 2, "derrotas": 1},  
        "Escócia":       {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
        "Sérvia":        {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
        "Ucrânia":       {"jogos": 3, "vitorias": 0, "empates": 0, "derrotas": 3},  
    },

    # CAF — África
    "CAF": {
        "Marrocos":        {"jogos": 3, "vitorias": 2, "empates": 1, "derrotas": 0}, 
        "Senegal":         {"jogos": 3, "vitorias": 2, "empates": 0, "derrotas": 1},  
        "Egito":           {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Nigéria":         {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Costa do Marfim": {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2},  
        "África do Sul":   {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2},  
        "Camarões":        {"jogos": 3, "vitorias": 0, "empates": 2, "derrotas": 1},  
        "Mali":            {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
        "Tanzânia":        {"jogos": 3, "vitorias": 0, "empates": 0, "derrotas": 3},  
    },

    # AFC — Ásia
    "AFC": {
        "Japão":          {"jogos": 3, "vitorias": 2, "empates": 1, "derrotas": 0},  
        "Coreia do Sul":  {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Austrália":      {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Irã":            {"jogos": 3, "vitorias": 1, "empates": 1, "derrotas": 1},  
        "Arábia Saudita": {"jogos": 3, "vitorias": 1, "empates": 0, "derrotas": 2},  
        "Uzbequistão":    {"jogos": 3, "vitorias": 0, "empates": 2, "derrotas": 1},
        "Qatar":          {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
        "Iraque":         {"jogos": 3, "vitorias": 0, "empates": 0, "derrotas": 3},  
    },

    # OFC — Oceania
    "OFC": {
        "Nova Zelândia": {"jogos": 3, "vitorias": 0, "empates": 1, "derrotas": 2},  
    }
}

for item in selecoes["CONMEBOL"]:
    print((item))
for item in selecoes["CONCACAF"]:
    print((item), ":" ) 
for item in selecoes["UEFA"]:
    print((item))
for item in selecoes["CAF"]:
    print((item))
for item in selecoes["AFC"]:
    print((item))
for item in selecoes["OFC"]:
    print((item))







