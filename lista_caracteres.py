lista_caracteres = ["A", "c", "B", "f", "X", "d", "t"]

nova_lista = list(map(lambda carac : carac.lower() if (carac == carac.upper()) else carac.upper(),lista_caracteres))

print(nova_lista)
