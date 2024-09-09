check1 = float(input("Digite a nota do checkpoint 1: "))
check2 = float(input("Digite a nota do checkpoint 2: "))
check3 = float(input("Digite a nota do checkpoint 3: "))

media = (check1 + check2 + check3) / 3

if (media >= 6.0):
    print(f"Aprovado com media {media:.2f}")
elif (media >= 3.0):
    print(f"Exame com media {media:.2f}")
else:
    print(f"Reprovado com media {media:.2f}")