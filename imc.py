peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura * altura)  #peso / altura**

print(f"Seu IMC eh: {imc:.2f}")

