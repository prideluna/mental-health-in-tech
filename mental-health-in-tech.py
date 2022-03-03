TREATMENT = 7
COUNTRY = 3
AGE = 1
GENDER = 2
EMPLOYEES = 9
TECHCOMPANY=11

def menu():
    print()
    print("Menu")
    print("1. Carregar arquivo ") 
    print("2. Listar dados ") 
    print("3. Percentual de pessoas do gênero masculino e feminino em empresas com mais de mil funcionários ")
    print("4. Média de idade dentre as pessoas que procuraram tratamento? ")
    print("5. Em “work_interfere”, informe quantidade de pessoas em cada categoria")
    print("6. Dentre os países, qual o percentual de pessoas com transtornos mentais")
    print("7. Percentual de pessoas com problemas de saúde entre os que trabalham em home-office x na empresa.")
    print("8.Há relação entre o tamanho da empresa e percentual de problemas de saúde? Encontre alguma relação com os dados. ")
    print("9. Gerar nova coluna categorizando as pessoas por idade.")
        # a.  jovem (até 20 anos) ***********************Até 19
        # b. Adulto 1 (entre 20 e 35 anos) 
        # c. Adulto 2 (entre 36 e 50 anos) 
        # d. Adulto 3 (entre 51 e 65 anos) 
        # e. Idoso (mais que 65 anos) 
    print("10.Considerando a nova coluna: percentual de pessoas com problema de saúde em cada faixa de idade. ")
    print("11.Gerar um novo arquivo somente com as pessoas dos Estados Unidos com: idade, genero, se relatou problemas e tamanho da empresa ")
    # print("12.Crie outra pesquisa que julgar fazer sentido para o escopo do projeto. ") 
    print("12. Há relacao entre procura de tratamento e a empresa ser ou nao big tech? ") 
    print()

def carrega_dados_dicio(ds):
    d = {}
    ds = open(r"/home/pri/Desktop/Desktop/_/ADS/AP1/DATASET/survey.csv", "r")
    lines = ds.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", '')
        lines[i]= lines[i].replace("\"", '')
        lines[i]= lines[i].replace("\'", '')
        lines[i]= lines[i].split(',')
    headers = lines[0]
    for header in headers:
        d[header] = []
    for idx in range(1,len(lines)):
        eachLine = lines[idx]
        for i_headers in range(len(headers)):
            header = headers[i_headers]
            field_value = eachLine[i_headers]
            d[header].append(field_value)
    return d

def carregar_dados_matriz(ds):
    mat = []
    ds = open(r"/home/pri/Desktop/Desktop/_/ADS/AP1/DATASET/survey.csv", "r")
    for line in ds:
        line = line.replace("\n", '')
        line= line.replace("\"", '')
        line= line.replace("\'", '')
        data = line.split(',')
        mat.append(data)
    mat = mat[1:]
    ds.close()
    return mat

def listar_dados(ds):
    print(carregar_dados_matriz(ds))

def genero_masc_fem_mil_funcionarios(dict):
    cont_genderF_more_than_1000 = 0
    cont_genderM_more_than_1000 = 0
    contTotal = len(dict['no_employees'])
    genders = dict['Gender']
    genderM = ['M','m','male','Male']
    genderF = ['Female', 'F', 'female', 'f', 'Trans-female', 'Trans woman']

    for i in range(len(genders)):
        gender = genders[i] 
        no_employees = dict['no_employees'][i]

        if gender in genderF and 'More than 1000' ==  no_employees :
            cont_genderF_more_than_1000 += 1
        if gender in genderM  and 'More than 1000' ==  no_employees :
            cont_genderM_more_than_1000 += 1

    percentF = round((cont_genderF_more_than_1000/contTotal)*100, 2)
    percentM = round((cont_genderM_more_than_1000/contTotal)*100,2)
    return percentF, percentM

def procuram_tratamento(dict):
    soma_idade = 0
    contAge = 0
    for i in range(len(dict['Age'])):
        age = int(dict['Age'][i])
        treatment = dict['treatment'][i]

        if treatment == 'Yes' and age <150:
            soma_idade = soma_idade + age
            contAge +=1
    mediaIdade = soma_idade/contAge #!=0
    return round(mediaIdade)

def work_interfere_category(dict):
    frequency = ['Sometimes', 'Often', 'Yes', 'Never', 'NA', 'Rarely']
    for freq in frequency:
        frequencia = dict['work_interfere'].count(freq)
        print(f' {frequencia} pessoas reponderam que a frequencia que a saúde mental reflete no serviço é \"{freq} \" ')
         
def saude_mental_pais(mat):
    dict = {}
    for i in range (len(mat)):
        if mat[i][TREATMENT] == 'Yes':
            if mat[i][COUNTRY] not in dict.keys():
                dict[mat[i][COUNTRY]] = 0
            for chave in dict:
                if chave == mat[i][COUNTRY]:
                    dict[mat[i][COUNTRY]] =  dict[mat[i][COUNTRY]] + 1
    return dict

def percentual_home_office_presencial_e_saude_mental(dict):
    contMentalConditionHomeoffice = 0
    contMentalConditionNoHomeoffice = 0
    totalRemote = 0
    totalNoRemote = 0
    for i in range(len(dict['remote_work'])):
        if dict['remote_work'][i] == "Yes":
            totalRemote +=1
            if dict['treatment'][i] == "Yes":
                contMentalConditionHomeoffice +=1
        if dict['remote_work'][i] == "No":
            totalNoRemote +=1
            if dict['treatment'][i] == "Yes":
                contMentalConditionNoHomeoffice +=1       
    percHomeOffice = contMentalConditionHomeoffice/totalRemote
    percNoHomeOffice = contMentalConditionNoHomeoffice/totalNoRemote
    return percHomeOffice, percNoHomeOffice

def relacao_tamanho_empresa_saude_mental(mat,dict):
    L = []
    tot = len(dict['Age'])  ##### -----> colocar total em relacao à quantidade que disse sim e nao dentro das empresas
    qtde =0
    for i in range(len(dict)):
        if mat[i][EMPLOYEES] not in L:
            L.append(mat[i][EMPLOYEES])
    
    for size in L:
        print(len(dict['treatment']))
            
      #  print(f'Porcentagem de pessoas que buscam tratamento em empresas do tamanho de {size} funcionarios é {percent}%')

def ageCategory(mat):
    addCategoriaIdade = []
    categorizadoPorIdade = []
    for i in range(1, len(mat)):
        addCategoriaIdade = mat[i]
        categoria = ['Jovem', 'Adulto 1', 'Adulto 2', 'Adulto 3', 'Idoso' ]
        if mat[i][AGE] == ']9':
            mat[i][AGE] = 30
        if int(mat[i][AGE]) < 120: 
            age = int(mat[i][AGE])
        if int(mat[i][AGE]) >= 120: 
            age = 29
        if age <= 19:
            addCategoriaIdade.append(categoria[0])
        elif age > 19 and age <= 35:
            addCategoriaIdade.append(categoria[1])
        elif age >= 36 and age <= 50:
            addCategoriaIdade.append(categoria[2])
        elif age >= 51 and age <= 65:
            addCategoriaIdade.append(categoria[3])
        else:
            addCategoriaIdade.append(categoria[4])
        categorizadoPorIdade.append(addCategoriaIdade)
    return categorizadoPorIdade
    
    #return matriz[i][]
        # if age >= 20 and age <= 35:
        #     dados.append(mat[i])
        #     matriz.append(dados)
        # if age >= 36 and age <= 50:
        #     print("Adulto 2")
        # if age >= 51 and age <= 65:
        #     print("Adulto 3")
        # if age > 65:
        #     print("Idoso")

def saude_mental_faixa_idade(mat):
    ageCategory(mat)
    somaJovem = 0
    somaAdulto1 = 0
    somaAdulto2 =0
    somaAdulto3 =0
    somaIdoso =0
    somaTotal = 0
    for i in range(1, len(mat)):
        somaTotal= somaTotal +1 
        if mat[i][27] == 'Jovem':
            somaJovem = somaJovem +1
        if mat[i][27] == 'Adulto 1':
            somaAdulto1 = somaAdulto1 +1
        if mat[i][27] == 'Adulto 2':
            somaAdulto2 = somaAdulto2 +1
        if mat[i][27] == 'Adulto 3':
            somaAdulto3 = somaAdulto3 +1
        if mat[i][27] == 'Idoso':
            somaIdoso = somaIdoso +1
    percJovem = round((somaJovem/somaTotal)*100, 2)
    percAdulto1 = round((somaAdulto1/somaTotal)*100, 2)
    percAdulto2 = round((somaAdulto2/somaTotal)*100, 2)
    percAdulto3 = round((somaAdulto3/somaTotal)*100, 2)
    percIdoso = round((somaIdoso/somaTotal)*100, 2)

    return percJovem, percAdulto1,  percAdulto2, percAdulto3, percIdoso

def novoArquivoEUA(mat):
    arquivoNovo = open(r'/home/pri/Desktop/Desktop/_/ADS/AP1/DATASET/novoArquivoEUA', "w") 
    matEUA = []
    for i in range(len(mat)):
        listaEUA = []
        if mat[i][COUNTRY] == 'United States':
            listaEUA.append(mat[i][AGE])
            listaEUA.append(mat[i][GENDER])
            listaEUA.append(mat[i][TREATMENT])
            listaEUA.append(mat[i][EMPLOYEES])
            matEUA.append(listaEUA)
    for i in range(len(matEUA)):
       linha = matEUA[i]
       arquivoNovo.write(str(linha) + "\n")   
    arquivoNovo.close()

def procura_tratamento_empresaTech(mat):
    count1 = 0
    count2 = 0
    countTotalBigTech =0
    countTotalNoBigTech =0
    for i in range(len(mat)):
        if mat[i][TECHCOMPANY] == 'Yes':
            countTotalBigTech +=1
            if mat[i][TREATMENT] == 'Yes':
                count1+=1
        if mat[i][TECHCOMPANY] == 'No':
            countTotalNoBigTech +=1
            if mat[i][TREATMENT] == 'Yes':
                count2+=1
    percBigTechTreatment = round(count1/countTotalBigTech*100)
    percNoBigTechTreatment = round(count2/countTotalNoBigTech*100)
    return percBigTechTreatment, percNoBigTechTreatment

dataset = r'/home/pri/Desktop/Desktop/_/ADS/AP1/DATASET/survey.csv'
matriz = carregar_dados_matriz(dataset)
dicionarioDataset = carrega_dados_dicio(dataset)
opcao= -1
while opcao !=0:
    menu()
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        carrega_dados_dicio(dataset)
        print('Dados carregados com sucesso')
        
    elif opcao==2:
        matrizListar = carregar_dados_matriz(dataset)
        for i in range(len(matriz)):
            print(matrizListar[i])

    elif opcao ==3:
        genF, genM = genero_masc_fem_mil_funcionarios(dicionarioDataset)
        
        print(f'A porcentagem de mulheres que procuraram tratamento e trabalham em empresa com mais de 1000 funcionarios é:{genF}% ')
        print(f'A porcentagem de homens que procuraram tratamento e trabalham em empresa com mais de 1000 funcionarios é:{genM}% ')

    elif opcao ==4:
        mediaIdadeProcuramTratamento = procuram_tratamento(dicionarioDataset)
        print(f'A média de idade em que os funcionarios procuram tratamento é: {mediaIdadeProcuramTratamento} anos')

    elif opcao ==5:
        work_interfere_category(dicionarioDataset)

    elif opcao ==6:
        dicionarioSaudePais = saude_mental_pais(matriz)
        for key in dicionarioSaudePais:
            porcentagem = 100*(dicionarioSaudePais[key]/len(matriz))
            print(f'Pessoas no país {key} que procuram tratamento: {dicionarioSaudePais[key]}, do total é: {round(porcentagem, 2)}% ')
    
    elif opcao ==7:
        homeOffice, noHomeOffice =  percentual_home_office_presencial_e_saude_mental(dicionarioDataset)
        print('Porcentagem de pessoas que procuram tratamento e trabalham home-office: ' + str(round(homeOffice,3)*100) + '%')
        print('Porcentagem de pessoas que procuram tratamento e não trabalham home-office: ' + str(round(noHomeOffice,3)*100) + '%')

    elif opcao ==8:
        relacao_tamanho_empresa_saude_mental(matriz,dicionarioDataset)
        print(f"Os valores são muito próximos e nao há como se tirar relacao entre eles, precisa-se de uma base de dados maior.")

    elif opcao ==9:
        ageCategory(matriz) 
        (print('Nova coluna categorizada por idade gerada!'))
    
    elif opcao ==10:
        jovem, adulto1, adulto2,adulto3,idoso = saude_mental_faixa_idade(matriz)
        print(f"porcentagem de pessoas na faixa de idade jovens que relatam problema de saúde mental é: {jovem}%")
        print(f"porcentagem de pessoas na faixa de idade adulto1 que relatam problema de saúde mental é: {adulto1}%")
        print(f"porcentagem de pessoas na faixa de idade adulto2 que relatam problema de saúde mental é: {adulto2}%")
        print(f"porcentagem de pessoas na faixa de idade adulto3 que relatam problema de saúde mental é: {adulto3}%")
        print(f"porcentagem de pessoas na faixa de idade idoso que relatam problema de saúde mental é: {idoso}%")
        
    elif opcao ==11:
        novoArquivoEUA(matriz)
        print('Arquivo criado')

    elif opcao ==12:
        percentualEmpresaTech, percentualEmpresaNaoTech = procura_tratamento_empresaTech(matriz)
        print(f'O percentual  procura por tratamento em empresa tech é de {percentualEmpresaTech}%')
        print(f'O percentual  procura por tratamento em empresa nao tech é de {percentualEmpresaNaoTech}%')

    else:
        print("Opcao inválida")
