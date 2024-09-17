votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_validos = int(input("Digite a quantidade de votos validos: "))

total_eleitores = votos_brancos + votos_nulos + votos_validos

perc_brancos = (votos_brancos * 100) / total_eleitores
perc_nulos = (votos_nulos * 100) / total_eleitores
perc_validos = (votos_validos * 100) / total_eleitores

print(f"Percentual de votos brancos: {perc_brancos:.2f}%")
print(f"Percentual de votos nulos: {perc_nulos:.2f}%")
print(f"Percentual de votos validos: {perc_validos:.2f}%")