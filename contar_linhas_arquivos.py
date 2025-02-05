import os


def contar_linhas_arquivos(pasta):
    try:
        arquivos = os.listdir(pasta)

        if not arquivos:
            print("A pasta está vazia.")
            return

        print("Contagem de linhas por arquivo:")
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_arquivo):
                with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                    num_linhas = sum(1 for line in f)
                print(f"{arquivo}: {num_linhas} linhas")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    contar_linhas_arquivos(pasta)
