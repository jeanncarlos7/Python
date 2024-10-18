import oracledb
import pandas as pd
import brazilcep

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
    print("1-Insercao")
    print("2-Consulta")
    print("3-Relatorio de todos os clientes com idade superior a 35 anos que residam na cidade de Sao Paulo")
    print("4-Relatorio de todos os clientes que residam no Rio de Janeiro com limite de credito superior a R$5000,00")
    print("5-Alteracao")
    print("6-Exclusao")
    print("7-Sair")

    opc = int(input("Digite a opcao (1-6): "))

    if (opc==1):
        try:
            nome = input("Nome: ")
            try:
                cep = input("Digite o CEP da sua residência - 99999-999: ")
                address = brazilcep.get_address_from_cep(cep)
            except:
                print("Erro de consulta ao CEP")
            else:
                logr = address['street']
                bairro = address['district']
                cidade = address['city']

            idade = int(input("Idade: "))
            limite = float(input("Limite de Credito: "))

            cadastro = f"""INSERT INTO clientes (cliente_nome,cliente_logradouro,cliente_bairro,cliente_cidade,cliente_idade,cliente_limitecredito) VALUES ('{nome}','{logr}','{bairro}','{cidade}',{idade},{limite})"""

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

        inst_consulta.execute('SELECT * FROM clientes')

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        lista_dados = sorted(lista_dados)

        dados_df = pd.DataFrame.from_records(lista_dados,columns = ['Id','Nome','Logradouro','Bairro','Cidade','Idade','Limite Credito'],index='Id')

        if (dados_df.empty):
            print("NÃ£o hÃ¡ registros")
        else:
            print(dados_df)
        print("\n")
    elif (opc==3):
        lista_dados = []
        relat1 = f"""SELECT * FROM clientes WHERE cliente_idade > 35 and cliente_cidade = 'São Paulo'"""

        inst_consulta.execute(relat1)

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade','Limite Credito'], index='Id')

            if (dados_df.empty):
                print("NÃ£o hÃ¡ registros")
            else:
                print(dados_df)
            print("\n")
    elif (opc==4):
        lista_dados = []
        relat2 = f"""SELECT * FROM clientes WHERE cliente_limitecredito > 5000 and cliente_cidade = 'Rio de Janeiro'"""

        inst_consulta.execute(relat2)

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade','Limite Credito'], index='Id')

            if (dados_df.empty):
                print("NÃ£o hÃ¡ registros")
            else:
                print(dados_df)
            print("\n")
    elif (opc == 5):
        lista_dados = []

        id = int(input("Digite o Id do cliente a ser alterado: "))

        consulta = f"""SELECT * FROM clientes WHERE cliente_id = {id}"""

        inst_consulta.execute(consulta)
        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print("O id digitado nÃ£o existe na tabela")
        else:
            try:
                nome = input("Nome: ")
                try:
                    cep = input("Digite o CEP da sua residência - 99999-999: ")
                    address = brazilcep.get_address_from_cep(cep)
                except:
                    print("Erro de consulta ao CEP")
                else:
                    logr = address['street']
                    bairro = address['district']
                    cidade = address['city']

                idade = int(input("Idade: "))
                limite = float(input("Limite de Credito: "))

                alteracao = f"""UPDATE clientes SET cliente_nome='{nome}',cliente_logradouro='{logr}',cliente_bairro='{bairro}',cliente_cidade='{cidade}',cliente_idade={idade},cliente_limitecredito={limite} WHERE cliente_id={id}"""

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

        id = int(input("Digite o Id do cliente a ser excluido: "))

        consulta = f"""SELECT * FROM clientes WHERE cliente_id = {id}"""

        inst_consulta.execute(consulta)
        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print("O id digitado nÃ£o existe na tabela")
        else:
            try:

                exclusao = f"""DELETE from CLIENTES WHERE cliente_id={id}"""

                inst_alteracao.execute(exclusao)
                conn.commit()
            except:
                print("Erro de transaÃ§Ã£o no BD")
            else:
                print("Dados atualizados com sucesso")
    elif (opc==7):
        conexao = False
