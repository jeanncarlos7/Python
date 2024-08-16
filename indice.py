lista_nomes = []
lista_profissoes = []

resp = 1

while(resp!=0):
    lista_nomes.append(input("Digite o nome da pessoa: "))
    lista_profissoes.append(input("Digite a profissao da pessoa: "))
    resp = int(input("Deseja continuar (1-SIM / 0-NAO)? "))

nome = input("Digite o nome ao qual deseja saber a profissao: ")

if (nome in lista_nomes):
    indice = lista_nomes.index(nome)
    print(f"A profissao de {nome} eh {lista_profissoes[indice]}")