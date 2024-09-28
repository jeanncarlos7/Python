'''
1. [1,5 ponto] Uma revendedora de carros usados paga a seus funcionários
vendedores um salário fixo por mês, mais uma comissão também fixa para
cada carro vendido e mais 5% do valor das vendas por ele efetuadas.
Escrever um algoritmo que leia o número de carros por ele vendidos, o
valor total de suas vendas, o salário fixo e o valor que ele recebe
por carro vendido. Calcule e escreva o salário final do vendedor.
'''
nro_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = float(input("Digite o salário fixo: "))
valor_comissao_por_carro = float(input("Digite o valor da comissão por carro: "))

salario_final = salario_fixo + (nro_carros_vendidos * valor_comissao_por_carro) + (valor_vendas * 0.05)

print(f"O salário final é R${salario_final:.2f}")