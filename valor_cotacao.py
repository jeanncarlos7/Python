valor_cotacao = float(input("Digite a cotacao do dolar: "))
valor_dolares = float(input("Digite quantos dolares serao convertidos: "))

valor_reais = valor_dolares * valor_cotacao

print(f"U${valor_dolares:.2f} equivale a R${valor_reais:.2f} ")