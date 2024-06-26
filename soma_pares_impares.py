lista_numeros = [4, 7, 6, 2, 5, 13, 12, 9, 20]

soma_pares = sum(list(map(lambda num : num if (num % 2 == 0) else 0,lista_numeros)))
soma_impares = sum(list(map(lambda num : num if (num % 2 != 0) else 0,lista_numeros)))

print(f"A soma dos pares é {soma_pares}")
print(f"A soma dos ímpares é {soma_impares}")
