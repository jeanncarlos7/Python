matriz_ascii = []

senha = input("Digite uma senha com 9 caracteres: ")
indice_str = 0

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(ord(senha[indice_str]))
        indice_str+=1
    matriz_ascii.append(linha)

for lin in range(3):
    print(matriz_ascii[lin])