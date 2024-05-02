#Dicionário para armazenar os parâmetros de um inversor de frequência.

linha1 = {
    "Descrição": "Acesso aos Parâmetros",
    "Faixa de valores": "0 a 9999",
    "Ajuste de Fábrica": 0,
    "Ajuste do usuário": None,
    "Propr.": None,
    "Grupos": None,
    "Pág.": "5-2",
}

linha2 = {
    "Descrição": "Referência velocidade",
    "Faixa de valores": "0 a 65535",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-1",
}

linha3 = {
    "Descrição": "Velocidade de saída (Motor)",
    "Faixa de valores": "0 a 65535",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-1",
}

dicionario = {
    "P0000": linha1,
    "P0001": linha2,
    "P0002": linha3,
}

for parametro, info_parametro in dicionario.items():
    print(parametro, "->")
    for topicos, info_topicos in info_parametro.items():
        print(topicos, ":", info_topicos)
        print('')
    print('')

#for key, value in a_dict.items():
#print(key, '->', value)


