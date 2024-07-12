def main():
    listaOriginal = [234, 64, 13467, 45.89, 23]
    listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

    lista_preco_desc = list(map(calcula_desconto,listaOriginal,listaDescontos))

    print(lista_preco_desc)


def calcula_desconto (preco,desc):
    preco_desc = preco - (preco * desc)
    return (preco_desc)

if (__name__ == "__main__"):
    main()
