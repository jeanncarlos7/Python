
# ITEM A
converte_oposto = lambda num : -num
print(converte_oposto(7))

# ITEM B
converte_inverso = lambda num : 1/num
print(converte_inverso(4))

#ITEM C
calcula_metade = lambda num : num/2
print(calcula_metade(6))

#ITEM D
calcula_soma_quadrados = lambda a,b : a**2 + b**2
print(calcula_soma_quadrados(7,5))

#ITEM E
imprime_dados = lambda nome,idade : print(f"{nome} tem {idade} anos")
imprime_dados("João",20)

#ITEM F
verifica_parimpar = lambda x : 1 if (x % 2 == 0) else 0
print(verifica_parimpar(8))

#ITEM G
calcula_triplo = lambda p : 3 * p
print(calcula_triplo(8))

#ITEM H
verifica_maioridade = lambda idade : print("A pessoa é maior de idade") if (idade >= 18) else print("A pessoa não é maior de idade")
verifica_maioridade(17)
