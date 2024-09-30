valor_mercadoria = float(input("Digite o valor da mercadoria: "))
valor_usuario = float(input("Digite o valor que tens em maos: "))

if (valor_mercadoria <= valor_usuario):
    print("O valor que tens em maos eh suficiente!")
else:
    print("O valor que tens em maos nao eh suficiente!")