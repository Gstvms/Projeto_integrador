import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host='us-cdbr-east-06.cleardb.net',
        user='b0e0b46a8c1c10',
        password='b49eace8',
        database='heroku_b89f3369fa5ed88',
    )

    consulta_sql = """
                        select * from ProjetoIntegrador;
                        """

    cursor = conexao.cursor()
    cursor.execute(consulta_sql)

    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os IQAs registrados: ")
    for linha in linhas:
        print("ID: ", linha[0])
        print("MP2,5: : ", linha[1])
        mp25 = linha[1]
        print("MP10: ", linha[2])
        mp10 = linha[2]
        print("O3: ", linha[3])
        o3 = linha[3]
        print("CO: ", linha[4])
        co = linha[4]
        print("NO2: ", linha[5])
        no2 = linha[5]
        print("SO2: ", linha[6])
        so2 = linha[6]


        #--------------------------------------------------------------------------------------------------------

        iqamp25 = mp25 * 1.6

        iqamp10 = mp10 /1.25

        #-------------------------------------------------------------------------------------------------------
        if o3 <= 100:
            iqao3 = 0 + (40 / 50) * (o3)

        elif o3 > 100 and o3 <= 130:

            iqao3 = 41 + (39 / 30) * (o3 - 100) 

        elif o3 > 130 and o3 <= 160:

            iqao3 = 81 + (39 / 30) * (o3 - 130)

        elif o3 > 160 and o3 <= 200:

            iqao3 = 121 + (79 / 40) * (o3 - 160)

        elif o3 > 200:

            iqao3 = 400   

        #---------------------------------------------------------------------------------------------------------
        if co <= 9:
            iqaco = 0 + (40 / 9) * (co - 0)

        elif co > 9 and co <= 11:
            iqaco = 41 + (39 / 2) * (co - 9)

        elif co > 11 and co <= 13:
            iqaco = 81 + (2 / 39) * (co - 11)

        elif co > 13 and co <= 15:

            iqaco = 121 + (79 / 2) * (co - 13)

        elif co > 15:

            iqaco = 400
        #---------------------------------------------------------------------------
        if no2 <= 200:

            iqano2 = 0 + (40 / 200) * (no2 - 0)

        elif no2 > 200 and no2 <= 240:

            iqano2 = 41 + (39 / 40) * (no2 - 200)

        elif no2 > 240 and no2 <= 320:

            iqano2 = 81 + (39 / 80) * (no2 - 240)

        elif no2 > 320 and no2 <= 1130:

            iqano2 = 121 + (79 / 810) * (no2 - 320)

        elif no2 > 1130:

            iqano2 = 400
        #-----------------------------------------
        if so2 <= 20:

            iqaso2 = 0 + (40 / 20) * (so2 - 0)

        elif so2 > 20 and so2 <= 40:

            iqaso2 = 41 + (39 / 20) * (so2 - 20)

        elif so2 > 40 and so2 <= 365:

            iqaso2 = 81 + (39 / 325) * (so2 - 40)

        elif so2 > 365 and so2 <= 800:

            iqaso2 = 121 + (79 / 435) * (so2 - 365)

        elif so2 > 800:

            iqaso2 = 400
        #----------------------------------------

        iqafinal = (iqaco + iqamp10 + iqamp25 + iqano2 + iqao3 + iqaso2) / 6
        pior = max(iqaco, iqamp10, iqamp25, iqano2, iqao3, iqaso2)
        print(f"IQA FINAL = %.2f"%(iqafinal))
        print(f"O PIOR IQA É = %.2f\n"%(pior))

        if pior <= 40:
            print("A qualidade do ar está BOM.")

        elif pior >40 and pior <= 80:
            print("A qualidade do ar está MODERADO.")
            print("Pessoas de grupos sensíveis (cranças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não será afetada.")

        elif pior > 80 and pior <=120:
            print("A qualidade do ar está RUIM.")
            print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com problemas respiratórios e cardíacas) podem apresentar efeitos mais sério na saúde.")

        elif pior > 120 and pior <= 200:
            print("A qualidade do ar está MUITO RUIM.")
            print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardos nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sentíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")

        elif pior > 200:
            print("A qualidade do ar está PÉSSIMO.")
            print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

        
        print("\n\n\n")


except Error as erro:
    print("ERRO ao acessar tabela MYSQL: {}".format(erro))
finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("Conexão ao MYSQL finalizada")
