'''
Elaborar um programa que efetue a leitura de 20 valores inteiros em uma matriz A com 4 linhas
 e 5 colunas. Construir uma lista B para 4 elementos que seja formada pelo somatório dos elementos
 correspondentes de cada linha da matriz A. Construir também uma lista C para 5 elementos que
 seja formada pelo somatório dos elementos correspondentes de cada coluna da matriz A.
 Ao final o programa deve apresentar os elementos da lista B e da lista C.
'''

matrizA = []
listaB = []
listaC = []

for lin in range(0,4):
    linha = []
    for col in range(0,5):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matrizA.append(linha)

for lin in range(0,4):
    soma_linha = 0
    for col in range(0,5):
        soma_linha+=matrizA[lin][col]
    listaB.append(soma_linha)


for col in range(0,5):
    soma_coluna = 0
    for lin in range(0,4):
        soma_coluna+=matrizA[lin][col]
    listaC.append(soma_coluna)

for lin in range(0,4):
    print(matrizA[lin])

print("\n")
print(listaB)
print(listaC)