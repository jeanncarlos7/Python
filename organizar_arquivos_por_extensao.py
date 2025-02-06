import os
import shutil


def organizar_arquivos_por_extensao(pasta):
    try:
        arquivos = os.listdir(pasta)

        if not arquivos:
            print("A pasta está vazia.")
            return

        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_arquivo):
                extensao = os.path.splitext(arquivo)[1][1:]
                if not extensao:
                    extensao = "sem_extensao"
                pasta_destino = os.path.join(pasta, extensao)
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                print(f"Movido: {arquivo} -> {pasta_destino}")

        print("Organização concluída!")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    organizar_arquivos_por_extensao(pasta)
