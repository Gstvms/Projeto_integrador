print("Programa para cálculo do IQA (Índice de qualidade do ar).")
print("_"*90)

inicio = True

while inicio == True:

    try:
        mp25 = float(input("\nDigite o MP2,5 (Partículas inaláveis com diâmetro inferior à 2,5µm) presente no ar: "))
        mp10 = float(input("\nDigite o MP10 (Partículas Inaláveis com diâmetro inferior à 10µm) presente no ar: "))
        o3 = float(input("\nDigite o O3 (Ozônio) presente no ar: "))
        co = float(input("\nDigite o CO (Monóxido de carbono) presente no ar: "))
        no2 = float(input("\nDigite o NO2 (Dióxido de nitrogênio) presente no ar: "))
        so2 = float(input("\nDigite o SO2 (Dióxido de enxofre) presente no ar: "))
        print("\n\n")
    except: 
        print("ERRO - Digite apenas números!\n\n")
        inicio = True
    try:
        if o3 < 0: #mp10 < 0 or mp10 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
            print("ERRO - Nenhum número pode ser negativo!\n\n")
            inicio = True
    except:
        print("ERRO - Digite apenas Números.")
        inicio = True

    #indice = indice inicial + ([indicefinal - indiceinicial] / concfinal- concinicial]) *(concmedida - concinicial)
    else:

        if mp10 <= 50:
            print("Qualidade do ar em relação ao MP10 é BOA.")
        elif mp10 > 50 and mp10 <= 100:
            print("Qualidade do ar em relação ao MP10 é MODERADA.")
        elif mp10 > 100 and mp10 <= 150:
            print("Qualidade do ar em relação ao MP10 é RUIM.")
        elif mp10 > 150 and mp10 <= 250:
            print("Qualidade do ar em relação ao MP10 é MUITO RUIM.")
        elif mp10 > 250:
            print("Qualidade do ar em relação ao MP10 é PESSIMO.")
        else:
            print("ERRO NO CÁLCULO MP10!\n\n")
            inicio = True

        iqamp10 = mp10 / 1.25
        print(f"O iqa do MP10 é {iqamp10} \n")

    #-------------------------------------------------------------------------------------
        
        if mp25 <= 25:
            print("Qualidade do ar em relação ao MP2,5 é BOA.")
        elif mp25 > 25 and mp25 <= 50:
            print("Qualidade do ar em relação ao MP2,5 é MODERADA.")
        elif mp25 > 50 and mp25 <= 75:
            print("Qualidade do ar em relação ao MP2,5 é RUIM.")
        elif mp25 > 75 and mp25 <= 125:
            print("Qualidade do ar em relação ao MP2,5 é MUITO RUIM.")
        elif mp25 > 125:
            print("Qualidade do ar em relação ao MP2,5 é PESSIMO.")
        else:
            print("ERRO NO CÁLCULO MP2,5\n\n")
            inicio = True

        iqamp25 = mp25 * 1.6
        print(f"O IQA do MP2,5 é {iqamp25} \n")

    #------------------------------------------------------------------------------------------------    

        if o3 <= 100:
            print("Qualidade do ar em relação ao O3 é BOA.")

            iqao3 = 0 + (40 / 50) * (o3)

            #indice = indice inicial + ([indicefinal - indiceinicial] / concfinal- concinicial]) *(concmedida - concinicial)


        elif o3 > 100 and o3 <= 130:
            print("Qualidade do ar em relação ao O3 é MODERADA.")

            iqao3 = 41 + (39 / 30) * (o3 - 100) 

        elif o3 > 130 and o3 <= 160:
            print("Qualidade do ar em relação ao O3 é RUIM.") # 81 - 120

            iqao3 = 81 + (39 / 30) * (o3 - 130)

        elif o3 > 160 and o3 <= 200:
            print("Qualidade do ar em relação ao O3 é MUITO RUIM.") #121 - 200

            iqao3 = 121 + (79 / 40) * (o3 - 160)

        elif o3 > 200:
            print("Qualidade do ar em relação ao O3 é PESSIMO.")

            iqao3 = 400

        else:
            print("ERRO NO CÁLCULO O3!\n\n")
            inicio = True      

        print(f"O IQA do O3 é {iqao3} \n")

    #-------------------------------------------------------------------------------------------
    #Até aqui sem ERRO
        try:
            if co <= 9:
                print("Qualidade do ar em relação ao CO é BOA.") #0 - 40

                iqaco = 0 + (40 / 9) * (co - 0)

            elif co > 9 and co <= 11:
                print("Qualidade do ar em relação ao CO é MODERADA.") # 41 - 80

                iqaco = 41 + (39 / 2) * (co - 9)

            elif co > 11 and co <= 13:
                print("Qualidade do ar em relação ao CO é RUIM.") # 81 - 120

                iqaco = 81 + (2 / 39) * (co - 11)

            elif co > 13 and co <= 15:
                print("Qualidade do ar em relação ao CO é MUITO RUIM.") # 121 - 200

                iqaco = 121 + (79 / 2) * (co - 13)

            elif co > 15:
                print("Qualidade do ar em relação ao CO é PESSIMO.") # > 200

                iqaco = 400

            else:
                print("ERRO NO CÁLCULO CO!\n\n")
                inicio = True  

            print(f"O IQA de CO é {iqaco}\n")
        except:
            print("")#ERRO - Digite apenas números!1")
            inicio = True

    #-----------------------------------------------------------------------------------

    #indice = indice inicial + ([indicefinal - indiceinicial] / concfinal- concinicial]) *(concmedida - concinicial)
        try:
            if no2 <= 200:
                print("Qualidade do ar em relação ao NO2 é BOA.") # 0 - 40

                iqano2 = 0 + (40 / 200) * (no2 - 0)

            elif no2 > 200 and no2 <= 240:
                print("Qualidade do ar em relação ao NO2 é MODERADA.") # 41 - 80

                iqano2 = 41 + (39 / 40) * (no2 - 200)

            elif no2 > 240 and no2 <= 320:
                print("Qualidade do ar em relação ao NO2 é RUIM.") # 81 - 120

                iqano2 = 81 + (39 / 80) * (no2 - 240)

            elif no2 > 320 and no2 <= 1130:
                print("Qualidade do ar em relação ao NO2 é MUITO RUIM.") # 121 - 200

                iqano2 = 121 + (79 / 810) * (no2 - 320)

            elif no2 > 1130:
                print("Qualidade do ar em relação ao NO2 é PESSIMO.") #200>

                iqano2 = 400

            else:
                print("ERRO NO CÁLCULO NO2!\n\n")
                inicio = True 
            
            print(f"O IQA do NO2 é {iqano2}\n")
        except:
            print("")#ERRO - Digite apenas números!3")
            inicio = True

    #-------------------------------------------------------------------------------------
        try:
            if so2 <= 20:
                print("Qualidade do ar em relação ao SO2 é BOA.") # 0 - 40

                iqaso2 = 0 + (40 / 20) * (so2 - 0)

            elif so2 > 20 and so2 <= 40:
                print("Qualidade do ar em relação ao SO2 é MODERADA.") # 41 - 80

                iqaso2 = 41 + (39 / 20) * (so2 - 20)

            elif so2 > 40 and so2 <= 365:
                print("Qualidade do ar em relação ao SO2 é RUIM.") # 81 - 120

                iqaso2 = 81 + (39 / 325) * (so2 - 40)

            elif so2 > 365 and so2 <= 800:
                print("Qualidade do ar em relação ao SO2 é MUITO RUIM.") # 121 - 200

                iqaso2 = 121 + (79 / 435) * (so2 - 365)

            elif so2 > 800:
                print("Qualidade do ar em relação ao SO2 é PESSIMO.") #200>

                iqaso2 = 400 

            else:
                print("ERRO NO CÁLCULO SO2!\n\n")
                inicio = True    
        except:
            print("")#ERRO - Digite apenas números!2")
            inicio = True
        
        try:
            print(f"O IQA do SO2 é {iqaso2}")
        

            iqageral = (iqaco + iqamp10 + iqamp25 + iqano2 + iqao3 + iqaso2) / 6

            pior = max(iqaco, iqamp10, iqamp25, iqano2, iqao3, iqaso2)
        
                #-----------------------------------

            print(f"\nO IQA médio geral é {iqageral}.")
            print(f"O pior iqa é {pior}")

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

            continua = input("\n\nDeseja calcular outro IQA? S/N ")
            if continua.lower() == "s":
                inicio = True
            else:
                break

        except:
            print("ERRO - Digite apenas números!")
            inicio = True