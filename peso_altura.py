peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / altura**2

if (imc <= 18.5):
    print(f"Abaixo do peso com imc {imc:.2f}")
elif (imc <= 24.9):
    print(f"Peso ideal com imc {imc:.2f} (Parabens!)")
elif (imc <= 29.9):
    print(f"Levemente acima do peso com imc {imc:.2f}")
elif (imc <= 34.9):
    print(f"Obesidade grau I com imc {imc:.2f}")
elif (imc <= 39.9):
    print(f"Obesidade grau II (severa) com imc {imc:.2f}")
else:
    print(f"Obesidade grau III (morbida) com imc {imc:.2f}")