str_usuario = input("Digite uma frase: ")

tam = len(str_usuario)
cont_espacos = 0
nova_str = ""

for i in range(tam):
    if (str_usuario[i]==" "):
        cont_espacos+=1
        nova_str = nova_str + "_"
    else:
        nova_str = nova_str + str_usuario[i]

print(f"Quantidade de espacos em branco na string: {cont_espacos}")
print(f"A nova string eh: {nova_str}")