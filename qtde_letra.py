'''
3. [1,5 pontos] Faça um programa que peça para o usuário inserir uma frase e
uma letra e que mostre na tela a quantidade de vezes que a letra inserida
apareceu na frase.
'''
frase = input("Digite uma frase: ")
letra = input("Digite uma letra a ser contada na frase: ")
qtde_letra = 0
tamanho = len(frase)

for i in range(tamanho):
    if (frase[i] == letra[0]):
        qtde_letra+=1

print(f"Quantidade de vezes da letra {letra[0]}: {qtde_letra}")