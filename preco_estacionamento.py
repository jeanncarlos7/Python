qtde_horas = float(input("Digite a quantidade de horas no estacionamento: "))

valor_pagar = qtde_horas * 5.00

if (qtde_horas >= 7):
    print("Valor a pagar: R$35.00")
else:
    print(f"Valor a pagar: {valor_pagar:.2f}")