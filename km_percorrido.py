km_percorrida = float(input("Digite a quilometragem percorrida: "))
litros = float(input("Digite quantos litros gastou para essa quilometragem: "))

km_l = km_percorrida / litros

print(f"Autonomia do carro: {km_l:.2f}")