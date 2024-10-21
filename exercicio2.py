import oracledb
import pandas as pd

try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br","1521","ORCL")
    conn = oracledb.connect(user="PF1633",password="fiap23",dsn = dnStr)

    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()

except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True

while (conexao==True):
    print("1-Inserção")
    print("2-Consulta")
    print("3-Relatorio de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades")
    print("4-Relatorio de todos os produtos com estoque superior a 120 unidades, cujo valor de venda esteja entre R$120,00 e R$350,00")
    print("5-Alteracao")
    print("6-Exclusao")
    print("7-Sair")

    opc = int(input("Digite a opcao (1-7): "))

    if (opc==1):
        try:
            descr = input("Descricao: ")
            categoria = input("Categoria: ")
            qtde = int(input("Quantidade: "))
            valor_compra = float(input("Valor da compra: "))
            valor_venda = float(input("Valor da venda: "))

            cadastro = f"""INSERT INTO produtos (produto_descricao,produto_categoria,produto_quantidade,produto_valorcompra,produto_valorvenda) VALUES ('{descr}','{categoria}',{qtde},{valor_compra},{valor_venda})"""

            inst_cadastro.execute(cadastro)
            conn.commit()
        except ValueError:
            print("Digite valores numÃ©ricos!")
        except:
            print("Erro de transaÃ§Ã£o do BD")
        else:
            print("Dados cadastrados com sucesso!")
    elif (opc==2):
        lista_dados = []

        inst_consulta.execute('SELECT * FROM produtos')

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        lista_dados = sorted(lista_dados)

        dados_df = pd.DataFrame.from_records(lista_dados,columns = ['Id','Descricao','Categoria','Quantidade','Valor Compra','Valor venda'],index='Id')

        if (dados_df.empty):
            print("NÃ£o hÃ¡ registros")
        else:
            print(dados_df)
        print("\n")
    elif (opc==3):
        lista_dados = []
        relat1 = f"""SELECT * FROM produtos WHERE produto_quantidade < 100"""

        inst_consulta.execute(relat1)

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,columns = ['Id','Descricao','Categoria','Quantidade','Valor Compra','Valor venda'],index='Id')

            if (dados_df.empty):
                print("NÃ£o hÃ¡ registros")
            else:
                print(dados_df)
            print("\n")
    elif (opc==4):
        lista_dados = []
        relat2 = f"""SELECT * FROM produtos WHERE produto_quantidade > 120 and produto_valorvenda between 120 and 350"""

        inst_consulta.execute(relat2)

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,columns = ['Id','Descricao','Categoria','Quantidade','Valor Compra','Valor venda'],index='Id')

            if (dados_df.empty):
                print("NÃ£o hÃ¡ registros")
            else:
                print(dados_df)
            print("\n")
    elif (opc == 5):
        lista_dados = []

        id = int(input("Digite o Id do produto a ser alterado: "))

        consulta = f"""SELECT * FROM produtos WHERE produto_id = {id}"""

        inst_consulta.execute(consulta)
        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print("O id digitado nÃ£o existe na tabela")
        else:
            try:
                descr = input("Descricao: ")
                categoria = input("Categoria: ")
                qtde = int(input("Quantidade: "))
                valor_compra = float(input("Valor da compra: "))
                valor_venda = float(input("Valor da venda: "))

                alteracao = f"""UPDATE produtos SET produto_descricao='{descr}',produto_categoria='{categoria}',produto_quantidade={qtde},produto_valorcompra={valor_compra},produto_valorvenda={valor_venda} WHERE produto_id={id}"""

                inst_alteracao.execute(alteracao)
                conn.commit()
            except ValueError:
                print("Digite valores numericos")
            except:
                print("Erro de transaÃ§Ã£o no BD")
            else:
                print("Dados atualizados com sucesso")
    elif (opc==6):
        lista_dados = []

        id = int(input("Digite o Id do produto a ser excluido: "))

        consulta = f"""SELECT * FROM produtos WHERE produto_id = {id}"""

        inst_consulta.execute(consulta)
        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print("O id digitado nÃ£o existe na tabela")
        else:
            try:

                exclusao = f"""DELETE from PRODUTOS WHERE produto_id={id}"""

                inst_alteracao.execute(exclusao)
                conn.commit()
            except:
                print("Erro de transaÃ§Ã£o no BD")
            else:
                print("Dados atualizados com sucesso")
    elif (opc==7):
        conexao = False
