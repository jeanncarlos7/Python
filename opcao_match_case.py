x = float(input("Digite o valor de x: "))

opc = int(input("Digite a opcao (1-3): "))

match opc:
    case 1:
        x = x + 5 # x+=5
    case 2:
        x = x - 4
    case 3:
        x = 2 * x
    case _:
        print("Opcao invalida!")

print(f"Novo valor de x: {x:.2f}")
