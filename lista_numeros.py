lista_numeros = [4, 3, 6, 7, 5, 8, 11, 20]

nova_lista = list(map(lambda num : num + 5 if (num % 2 == 0) else num - 2,lista_numeros))

print(nova_lista)