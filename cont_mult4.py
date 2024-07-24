lista_numeros = []

cont_mult4 = 0

for i in range(10):
    lista_numeros.append(int(input("Digite um numero: ")))

for i in range(10):
    if (lista_numeros[i] % 4 == 0):
        cont_mult4+=1

print(f"Quantidade de divisiveis por 4: {cont_mult4}")