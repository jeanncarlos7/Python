def main():
    lista_precos = [150.20, 50.38, 100.45, 230.13, 500.70]
    # chamada da função SEM map
    print(f"Preços com descontos: {calcula_desconto_sem_map (lista_precos)}")
    
    # chamada da função COM map
    lista_precos_desc = list(map(calcula_desconto_map,lista_precos))
    print(f"Preços com descontos: {lista_precos_desc}")


# Função SEM map

def calcula_desconto_sem_map (lista_precos):
    lista_precos_desc = []
    for i in range(len(lista_precos)):
        lista_precos_desc.append(lista_precos[i] - (lista_precos[i] * 0.20))

    return (lista_precos_desc)

# Função para utilizar no map

def calcula_desconto_map (preco):
    preco_desc = preco - (preco * 0.20)
    return(preco_desc)

if (__name__ == "__main__"):
    main()
