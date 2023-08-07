#inserção, alteração ou exclusão de dados - sistema de menu

import mysql.connector
from mysql.connector import Error

def insercao(mp25, mp10, o3, co, no2, so2): #funcionando 100%
    try:
        conexao = mysql.connector.connect(
            host='us-cdbr-east-06.cleardb.net',
            user='b0e0b46a8c1c10',
            password='b49eace8',
            database='heroku_b89f3369fa5ed88',
        )

        insere_dados_sql = "insert into projetointegrador (mp25, mp10, o3, co, no2, so2) values (%s, %s, %s, %s, %s, %s)"

        valores = [mp25, mp10, o3, co, no2, so2]

        cursor = conexao.cursor()
        cursor.execute(insere_dados_sql, valores)

        conexao.commit()
        print(cursor.rowcount, "registros inseridos na tabela!")
        cursor.close()
        
        print("Dados inseridos com Sucesso!")
    except Error as erro:
        print("Falha ao inserir dados no MYSQL: {}".format(erro))
    finally:
        # if conexao.is_connected():
        #     cursor.close()
        #     conexao.close()
        #     print("Conexão ao MYSQL finalizada")

        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MYSQL finalizada")



def alteracao(mp25, mp10, o3, co, no2, so2, id):
    try:
        conexao = mysql.connector.connect(
            host='us-cdbr-east-06.cleardb.net',
            user='b0e0b46a8c1c10',
            password='b49eace8',
            database='heroku_b89f3369fa5ed88',
        )

        altera_dados_sql = "update projetointegrador set mp25 = %s, mp10 = %s, o3 = %s, co = %s, no2 = %s, so2 = %s where id = %s"

        

        valores = [mp25, mp10, o3, co, no2, so2, id]

        cursor = conexao.cursor()
        cursor.execute(altera_dados_sql, valores)

        conexao.commit()
        print(cursor.rowcount, "registros alterados da tabela!")
        cursor.close()
        
        print("Dados alterados com Sucesso!")
    except Error as erro:
        print("Falha ao alterar dados no MYSQL: {}".format(erro))
    finally:

        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MYSQL finalizada")



def exclusao(id):
    try:
        conexao = mysql.connector.connect(
            host='us-cdbr-east-06.cleardb.net',
            user='b0e0b46a8c1c10',
            password='b49eace8',
            database='heroku_b89f3369fa5ed88',
        )

        exclui_dados_sql = "delete from projetointegrador where id = %s"

        valores = [id]

        cursor = conexao.cursor()
        cursor.execute(exclui_dados_sql, valores)

        conexao.commit()
        print(cursor.rowcount, "registros deletados da tabela!")
        cursor.close()
        
        print("Dados deletados com Sucesso!")
    except Error as erro:
        print("Falha ao deletar dados no MYSQL: {}".format(erro))
    finally:

        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MYSQL finalizada")
    



while True:

    menu = input("""Digite a função que deseja fazer:\n
1) Insersão de dados;
2) Alteração de dados;
3) Exclusão de dados.
""")

    if menu == "1": #insercao funcionando 100%
        mp25 = float(input("\nDigite o MP2,5 (Partículas inaláveis com diâmetro inferior à 2,5µm) presente no ar: "))
        mp10 = float(input("\nDigite o MP10 (Partículas Inaláveis com diâmetro inferior à 10µm) presente no ar: "))
        o3 = float(input("\nDigite o O3 (Ozônio) presente no ar: "))
        co = float(input("\nDigite o CO (Monóxido de carbono) presente no ar: "))
        no2 = float(input("\nDigite o NO2 (Dióxido de nitrogênio) presente no ar: "))
        so2 = float(input("\nDigite o SO2 (Dióxido de enxofre) presente no ar: "))
        insercao(mp25, mp10, o3, co, no2, so2)
        

    elif menu == "2": #alteração de dados #funcionando 100%
        id = int(input("\nDigite o ID do registro que deseja alterar: "))
        mp25 = float(input("\nDigite o MP2,5 (Partículas inaláveis com diâmetro inferior à 2,5µm) presente no ar: "))
        mp10 = float(input("\nDigite o MP10 (Partículas Inaláveis com diâmetro inferior à 10µm) presente no ar: "))
        o3 = float(input("\nDigite o O3 (Ozônio) presente no ar: "))
        co = float(input("\nDigite o CO (Monóxido de carbono) presente no ar: "))
        no2 = float(input("\nDigite o NO2 (Dióxido de nitrogênio) presente no ar: "))
        so2 = float(input("\nDigite o SO2 (Dióxido de enxofre) presente no ar: "))
        alteracao(mp25, mp10, o3, co, no2, so2, id)
        

    elif menu == "3": #exclusão de dados funcionando 100%
        id = int(input("\nDigite o ID do registro que deseja excluir: "))
        exclusao(id)

    continua = input("Deseja fazer outra operação? S/N: ")
    continua = continua.lower()
    if continua == "n" or continua == "nao" or continua == "não": break