import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def total_genero():
    Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')

    genero = []
    for indice, linha in Excel_file.iterrows():
        genero.append('Masculino' if linha['Sexo']  == 'Masculino' else 'Feminino')
    Excel_file['genero'] = genero

    ContagemMaior = Excel_file.groupby(['genero']).size()

    dadoMasc = Excel_file.loc[Excel_file['Sexo'] == 'Masculino']
    dadofem = Excel_file.loc[Excel_file['Sexo'] == 'Feminino']
    print(dadoMasc)
    print('--'*80)
    print(dadofem)

    #Contagem Para cada Direto ferido
    #Direito a vida (Masc)retido
    ContagemDireitoVida_Masc = dadoMasc.groupby(['DireitoVida']).size()
    print(ContagemDireitoVida_Masc)
    #Direito a vida (Fem) retido
    ContagemDireitoVida_fem = dadofem.groupby(['DireitoVida']).size()
    print(ContagemDireitoVida_fem)

    print('--'*80)

    #Contagem Violencia Masc
    ContagemViolencia_Masc = dadoMasc.groupby(['Violência']).size()
    print(ContagemViolencia_Masc)
    #Contagem Violencia Fem
    ContagemViolencia_Fem = dadofem.groupby(['Violência']).size()
    print(ContagemViolencia_Fem)

    print('--'*80)

    #Contagem Escravidão Masc
    ContagemEscravidao_Masc = dadoMasc.groupby(['Escravidão']).size()
    print(ContagemEscravidao_Masc)
    #contagem Escravidão Fem
    ContagemEscravidao_Fem = dadofem.groupby(['Escravidão']).size()
    print(ContagemEscravidao_Fem)

    print('--'*80)

    #Contagem Maus Tratos Masc
    ContagemMausTratos_Masc = dadoMasc.groupby(['MausTratos']).size()
    print(ContagemMausTratos_Masc)
    #Contagem Maus Tratos Fem
    ContagemMausTratos_Fem = dadofem.groupby(['MausTratos']).size()
    print(ContagemMausTratos_Fem)

    print('--'*80)

    #Contagem Liberdade Masc
    ContagemLiberdade_Masc = dadoMasc.groupby(['Liberdade']).size()
    print(ContagemLiberdade_Masc)
    #Contagem Liberdade Fem
    ContagemLiberdade_Fem = dadofem.groupby(['Liberdade']).size()
    print(ContagemLiberdade_Fem)

    print('--'*80)

    #Contagem Repressão Masc
    ContagemRepressão_Masc = dadoMasc.groupby(['Repressão']).size()
    print(ContagemRepressão_Masc)
    #Contagem Repressão Fem
    ContagemRepressão_Fem = dadofem.groupby(['Repressão']).size()
    print(ContagemRepressão_Fem)

    print('--'*80)

    #Contagem Liberdade de Expressão Masc
    ConatgemLiberdadeExpressão_Masc = dadoMasc.groupby(['LiberdadeExpressão']).size()
    print(ConatgemLiberdadeExpressão_Masc)
    #Contagem Liberdade de Expressão Fem
    ContagemLiberdadeExpressão_Fem = dadofem.groupby(['LiberdadeExpressão']).size()
    print(ContagemLiberdade_Fem)

    print('--'*80)

    #Tamanho das barras
    TamanhoBarra = 0.1

    #Separando grafico em colunas
    r1 = np.arange(len(ContagemMaior))
    r2 = [x + TamanhoBarra for x in r1]
    r3 = [x + TamanhoBarra for x in r2]
    r4 = [x + TamanhoBarra for x in r3]
    r5 = [x + TamanhoBarra for x in r4]
    r6 = [x + TamanhoBarra for x in r5]
    r7 = [x + TamanhoBarra for x in r6]


    #Plotando o grafico

    plt.subplot(2,1,1)
    plt.bar(r1, ContagemDireitoVida_Masc, width=TamanhoBarra, label='Direito a vida')
    plt.bar(r2, ContagemViolencia_Masc,width=TamanhoBarra, color='red', label='Violência')
    plt.bar(r3, ContagemEscravidao_Masc,width=TamanhoBarra, color='orange', label='Escravidão')
    plt.bar(r4, ContagemMausTratos_Masc, width=TamanhoBarra, color='pink', label='Maus Tratos')
    plt.bar(r5, ContagemLiberdade_Masc, width=TamanhoBarra, color='violet', label='Libedade')
    plt.bar(r6, ContagemRepressão_Masc, width=TamanhoBarra, color='black', label='Repressão')
    plt.bar(r7, ConatgemLiberdadeExpressão_Masc, width=TamanhoBarra, color='green', label='Liberdade de expressão')
    plt.xticks([r + TamanhoBarra for r in range(len(ContagemMaior))], ['Não Sofreram','Sofreram',])
    plt.legend()

    plt.title('Sexo Masculino x feminino ')

    plt.subplot(2,1,2)
    plt.bar(r1, ContagemDireitoVida_fem, width=TamanhoBarra, label='Direito a vida')
    plt.bar(r2, ContagemViolencia_Fem,width=TamanhoBarra, color='red', label='Violência')
    plt.bar(r3, ContagemEscravidao_Fem,width=TamanhoBarra, color='orange', label='Escravidão')
    plt.bar(r4, ContagemMausTratos_Fem, width=TamanhoBarra, color='pink', label='Maus Tratos')
    plt.bar(r5, ContagemLiberdade_Fem, width=TamanhoBarra, color='violet', label='Libedade')
    plt.bar(r6, ContagemRepressão_Fem, width=TamanhoBarra, color='black', label='Repressão')
    plt.bar(r7, ContagemLiberdadeExpressão_Fem, width=TamanhoBarra, color='green', label='Liberdade de expressão')
    plt.xticks([r + TamanhoBarra for r in range(len(ContagemMaior))], ['Não Sofreram','Sofreram',])
    plt.legend()


    plt.show()
    