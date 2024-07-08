ano = int(input("Digite o ano: "))

if (ano >= 1000 and ano <=2999):

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("O ano eh bissexto")
    else:
        print("O ano nao eh bissexto")

else:
    print("Ano invalido!")
