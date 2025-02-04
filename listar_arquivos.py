import os


def listar_arquivos(pasta):
    try:
        arquivos = os.listdir(pasta)

        if not arquivos:
            print("A pasta está vazia.")
            return

        print("Arquivos encontrados:")
        for arquivo in arquivos:
            print(arquivo)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    listar_arquivos(pasta)
