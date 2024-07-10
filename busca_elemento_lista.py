def main():
    lista_numeros = []
    tam = int(input("Digite o tamanho desejado para a lista: "))
    carrega_lista(lista_numeros, tam)
    maior,menor = retorna_maior_menor (lista_numeros, tam)
    print(f"O maior elemento da lista é {maior}")
    print(f"O menor elemento da lista é {menor}")
    elem = int(input("Digite o elemento a ser procurado na lista: "))
    pos = busca_elemento_lista (lista_numeros, tam, elem)

    if (pos != -1):
        print(f"O elemento foi encontrado na posição {pos}")
    else:
        print("O elemento não se encontra na lista")



def carrega_lista(lista_numeros, tam):
    for i in range(tam):
        lista_numeros.append(int(input("Digite um elemento da lista: ")))

def retorna_maior_menor (lista_numeros, tam):
    maior = lista_numeros[0]
    menor = lista_numeros[0]

    for i in range (1,tam):
        if (lista_numeros[i] > maior):
            maior = lista_numeros[i]
        if (lista_numeros[i] < menor):
            menor = lista_numeros[i]

    return (maior,menor)

def busca_elemento_lista (lista_numeros, tam, elem):
    pos = -1
    for i in range (tam):
        if (lista_numeros[i] == elem):
           pos = i
    return (pos)

if (__name__ == "__main__"):
    main()
