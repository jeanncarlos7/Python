'''
3. [2,0 pontos] Desenvolva um programa que recebe o peso e a altura do usuário. Calcule o
IMC sabendo que a fórmula do IMC é o peso dividido pela altura ao quadrado. Apresente na
tela o valor do IMC e a classificação de acordo com a tabela abaixo:
'''
peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

imc = peso / altura**2

if (imc <= 18.5):
    print(f"Abaixo do peso com IMC igual a {imc:.2f}")
elif (imc <= 24.9):
    print(f"Peso ideal com IMC igual a {imc:.2f}")
elif (imc <= 29.9):
    print(f"Levemente acima do peso com IMC igual a {imc:.2f}")
elif (imc <= 34.9):
    print(f"Obesidade grau I com IMC igual a {imc:.2f}")
elif (imc <= 39.9):
    print(f"Obesidade grau II (severa) com IMC igual a {imc:.2f}")
else:
    print(f"Obesidade grau III (mórbida) com IMC igual a {imc:.2f}")