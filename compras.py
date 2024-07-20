qtde_macas = int(input("Digite a quantidade de macas: "))

if (qtde_macas < 12):
    valor_pagar = qtde_macas * 1.30
else:
    valor_pagar = qtde_macas * 1.00

print(f"Voce comprou {qtde_macas} por {valor_pagar:.2f}")