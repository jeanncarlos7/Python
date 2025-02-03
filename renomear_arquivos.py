import os


def renomear_arquivos(pasta, prefixo="arquivo"):
    try:
        arquivos = os.listdir(pasta)
        arquivos.sort()

        for i, arquivo in enumerate(arquivos, start=1):
            caminho_antigo = os.path.join(pasta, arquivo)

            if os.path.isfile(caminho_antigo):
                extensao = os.path.splitext(arquivo)[1]
                novo_nome = f"{prefixo}_{i}{extensao}"
                caminho_novo = os.path.join(pasta, novo_nome)

                os.rename(caminho_antigo, caminho_novo)
                print(f"{arquivo} -> {novo_nome}")

        print("Renomeação concluída!")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    prefixo = input("Digite o prefixo dos arquivos (ou pressione Enter para usar 'arquivo'): ")
    if not prefixo:
        prefixo = "arquivo"
    renomear_arquivos(pasta, prefixo)

