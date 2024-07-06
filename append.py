matrizA = []
listaB = []

for lin in range(0,3):
    linha = []
    for col in range(0,6):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matrizA.append(linha)

for col in range(0,6):
    soma = 0
    for lin in range(0,3):
        if (col % 2 != 0):
            soma+=matrizA[lin][col]
    if (soma!=0):
        listaB.append(soma)

for lin in range(0,3):
    print(matrizA[lin])

print("\n Soma dos elementos das colunas cujos indices sao impares")
print(listaB)


