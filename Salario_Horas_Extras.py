'''
2. [1,5 ponto] A jornada de trabalho semanal de um funcionário é de 40 horas.
O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o
valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o
número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do
funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas
(considere que o mês possua 4 semanas exatas).
'''
nro_horas_mes = int(input("Digite o número de horas trabalhadas em um mês:  "))
valor_hora = float(input("Digite o valor do salário/hora: "))

if (nro_horas_mes > 160):
    valor_hora_extra = valor_hora * 1.50
    salario_final = (160 * valor_hora) + (nro_horas_mes - 160) * valor_hora_extra
else:
    salario_final = nro_horas_mes * valor_hora

print(f"O salário final é R${salario_final:.2f}")
