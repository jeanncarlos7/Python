str = input("Digite a string: ")

tam = len(str)
qtde_vogais = 0

for i in range(tam):
    if (str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        qtde_vogais+=1

print(f"Quantidade de vogais: {qtde_vogais}")
