'''
4. [2,5 pontos] O gerente de uma loja de produtos para Pets está levantando o valor total
de todas as mercadorias em estoque. Para tanto, ele solicitou a uma empresa de
desenvolvimento de softwares, a qual você é funcionário, que desenvolva um programa
que permita a entrada do número total de cada mercadoria no estoque e o valor de
cada mercadoria. Ao final o programa deverá imprimir a quantidade total de produtos
em estoque, o valor total em estoque (em reais) e a média de valor das mercadorias.
Vale ressaltar que, para a entrada dos dados, deverá haver a mensagem
“Deseja continuar (1-SIM e 0-NÃO)?”. Nesse caso, utilize a estrutura de repetição “while”.
'''
resp = 1
qtde_total_estoque = 0
valor_total_estoque = 0

while (resp != 0):
    valor_mercadoria = float(input("Digite o valor da mercadoria: "))
    qtde_mercadoria = int(input("Digite a quantidade da mercadoria: "))
    qtde_total_estoque+=qtde_mercadoria
    valor_total_estoque+=(qtde_mercadoria * valor_mercadoria)
    resp = int(input("Deseja continuar (1-SIM/0-NÃO)? "))

media_valor_mercadorias = valor_total_estoque / qtde_total_estoque

print(f"Quantidade total de produtos em estoque: {qtde_total_estoque}")
print(f"Valor total em estoque (em reais): {valor_total_estoque:.2f}")
print(f"Média de valor das mercadorias: {media_valor_mercadorias:.2f}")
