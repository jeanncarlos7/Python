import oracledb
import pandas as pd

def main():

    conexao, inst_SQL, conn = conecta_BD()

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

                str_insert = f"""INSERT INTO produtos (produto_descricao,produto_categoria,produto_quantidade,produto_valorcompra,produto_valorvenda) VALUES ('{descr}','{categoria}',{qtde},{valor_compra},{valor_venda})"""

                insert_tabela(inst_SQL, conn, str_insert)
            except ValueError:
                print("Digite valores numÃ©ricos!")

        elif (opc==2):
            str_consulta = 'SELECT * FROM produtos'
            str_colunas = f"""SELECT column_name FROM all_tab_cols WHERE table_name = 'PRODUTOS' AND OWNER = 'PF1633'"""

            inst_SQL.execute(str_colunas)
            dados = inst_SQL.fetchall()
            colunas = []
            for i in range(len(dados)):
                colunas.append(dados[i][0].split("_")[1])

            consulta_tabela(inst_SQL, str_consulta, colunas)
            print("\n")
        elif (opc==3):

            str_consulta = f"""SELECT * FROM produtos WHERE produto_quantidade < 100"""

            str_colunas = f"""SELECT column_name FROM all_tab_cols WHERE table_name = 'PRODUTOS' AND OWNER = 'PF1633'"""

            inst_SQL.execute(str_colunas)
            dados = inst_SQL.fetchall()
            colunas = []
            for i in range(len(dados)):
                colunas.append(dados[i][0].split("_")[1])

            consulta_tabela(inst_SQL, str_consulta, colunas)
            print("\n")
        elif (opc==4):

            str_consulta = f"""SELECT * FROM produtos WHERE produto_quantidade > 120 and produto_valorvenda between 120 and 350"""

            str_colunas = f"""SELECT column_name FROM all_tab_cols WHERE table_name = 'PRODUTOS' AND OWNER = 'PF1633'"""

            inst_SQL.execute(str_colunas)
            dados = inst_SQL.fetchall()
            colunas = []
            for i in range(len(dados)):
                colunas.append(dados[i][0].split("_")[1])

            consulta_tabela(inst_SQL, str_consulta, colunas)
            print("\n")
        elif (opc == 5):
            lista_dados = []

            id = int(input("Digite o Id do produto a ser alterado: "))

            consulta = f"""SELECT * FROM produtos WHERE produto_id = {id}"""

            inst_SQL.execute(consulta)
            dados = inst_SQL.fetchall()

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

                    str_update = f"""UPDATE produtos SET produto_descricao='{descr}',produto_categoria='{categoria}',produto_quantidade={qtde},produto_valorcompra={valor_compra},produto_valorvenda={valor_venda} WHERE produto_id={id}"""

                    update_tabela(inst_SQL, conn, str_update)

                except ValueError:
                    print("Digite valores numericos")

        elif (opc==6):
            lista_dados = []

            id = int(input("Digite o Id do produto a ser excluido: "))

            consulta = f"""SELECT * FROM produtos WHERE produto_id = {id}"""

            inst_SQL.execute(consulta)
            dados = inst_SQL.fetchall()

            for dado in dados:
                lista_dados.append(dado)

            if (len(lista_dados) == 0):
                print("O id digitado nÃ£o existe na tabela")
            else:
                str_delete = f"""DELETE from PRODUTOS WHERE produto_id={id}"""

                delete_tabela(inst_SQL, conn, str_delete)
        elif (opc==7):
            conexao = False

def conecta_BD():

    try:
        #conectar com o Servidor
        dnStr = oracledb.makedsn("oracle.fiap.com.br","1521","ORCL")
        #efetuar a conexao com o usuario
        conn = oracledb.connect(user='PF1633',password='fiap23',dsn=dnStr)

        #Criar as instrucoes para cada modulo
        inst_SQL = conn.cursor()

    except Exception as e:
        print("Erro: ", e)
        conexao = False
        inst_SQL = ""
        conn = ""
    else:
        conexao = True

    return(conexao,inst_SQL,conn)


def insert_tabela(inst_SQL,conn,str_insert):
    try:
        inst_SQL.execute(str_insert)
        conn.commit()

    except:
        print("Erro de transacao com o BD")
    else:
        print("Dados gravados com sucesso")

def consulta_tabela(inst_SQL,str_consulta,colunas):
    lista = []

    # Executa a consulta (Select) no BD
    inst_SQL.execute(str_consulta)

    # Captura todos os registros vindos pela consulta
    dados = inst_SQL.fetchall()

    # Insere os registros em uma lista
    for registro in dados:
        lista.append(registro)

    # Ordena a lista
    lista = sorted(lista)

    # Gera um Dataframe com os dados da lista (Pandas)
    base_df = pd.DataFrame.from_records(lista, columns=colunas, index=colunas[0])

    if (base_df.empty):
        print("Nao ha registros cadastrados")
    else:
        print(base_df)


def update_tabela(inst_SQL,conn,str_update):
        try:
            inst_SQL.execute(str_update)
            conn.commit()
        except:
            print("Erro de transacao com o BD")
        else:
            print("Dados alterados com sucesso")


def delete_tabela(inst_SQL, conn, str_delete):
    try:
        inst_SQL.execute(str_delete)
        conn.commit()
    except:
        print("Erro de transacao com o BD")
    else:
        print("Dados excluidos com sucesso")


if (__name__ == "__main__"):
    main()