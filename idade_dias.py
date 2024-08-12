idade = int(input("Digite sua idade: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

idade_dias = (idade * 365) + (meses * 30) + dias

print("Sua idade em dias eh: ", idade_dias)