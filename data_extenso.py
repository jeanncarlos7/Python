data_nasc = input("Digite a data de nascimento no formato dd/mm/aaaa: ")

lista_data = data_nasc.split("/")

if (lista_data[1] == "01"):
    mes_extenso = "janeiro"
elif (lista_data[1] == "02"):
    mes_extenso = "fevereiro"
elif (lista_data[1] == "03"):
    mes_extenso = "março"
elif (lista_data[1] == "04"):
    mes_extenso = "abril"
elif (lista_data[1] == "05"):
    mes_extenso = "maio"
elif (lista_data[1] == "06"):
    mes_extenso = "junho"
elif (lista_data[1] == "07"):
    mes_extenso = "julho"
elif (lista_data[1] == "08"):
    mes_extenso = "agosto"
elif (lista_data[1] == "09"):
    mes_extenso = "setembro"
elif (lista_data[1] == "10"):
    mes_extenso = "outubro"
elif (lista_data[1] == "11"):
    mes_extenso = "novembro"
elif (lista_data[1] == "12"):
    mes_extenso = "dezembro"

data_extenso = lista_data[0]+" de "+mes_extenso+" de "+lista_data[2]

print(f"Data por extenso: {data_extenso}")