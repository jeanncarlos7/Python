lista_precos = [230.33, 340.20, 125.60, 560.45, 854.30]

lista_precos_desc = list(map(lambda preco : preco - (preco * 0.20),lista_precos))

print(lista_precos_desc)