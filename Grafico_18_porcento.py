import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def grafico_porcentagem_18():
    #banco de dados
    Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')

    #Transformando idades em Maior e Menor
    valores = []
    for indice, linha in Excel_file.iterrows():
        valores.append('Maior' if linha['Idade']  >= 18 else 'Menor')
    Excel_file['Maior/Menor'] = valores
    #print(Excel_file)

    #vendo quando Maior e menores existem
    ContagemMaior = Excel_file.groupby(['Maior/Menor']).size()
    #print(ContagemMaior)

    #Seperando as tabelas em pessoas maiores e menores
    dadoMaior = Excel_file.loc[Excel_file['Maior/Menor'] == 'Maior']
    dadoMenor = Excel_file.loc[Excel_file['Maior/Menor'] == 'Menor']
    print(dadoMaior)
    print('--'*80)
    print(dadoMenor)

    #Contagem Para cada Direto ferido
    #Direito a vida (Maior)retido
    ContagemDireitoVida_Maior = dadoMaior.groupby(['DireitoVida']).size()
    print(ContagemDireitoVida_Maior)
    #Direito a vida (Menor) retido
    ContagemDireitoVida_Menor = dadoMenor.groupby(['DireitoVida']).size()
    #print(ContagemDireitoVida_Menor)

    #Contagem Violencia Maior
    ContagemViolencia_Maior = dadoMaior.groupby(['Violência']).size()
    #print(ContagemViolência_Maior)
    #Contagem Violencia Menor
    ContagemViolencia_Menor = dadoMenor.groupby(['Violência']).size()
    #print(ContagemDireitoVida_Menor)

    #Contagem Escravidão Maior
    ContagemEscravidao_Maior = dadoMaior.groupby(['Escravidão']).size()
    #print(ContagemEscravidao_Maior)
    #contagem Escravidão Menor
    ContagemEscravidao_Menor = dadoMenor.groupby(['Escravidão']).size()
    #print(ContagemEscravidao_Menor)

    #Contagem Maus Tratos Maior
    ContagemMausTratos_Maior = dadoMaior.groupby(['MausTratos']).size()
    #print(ContagemMausTratos_Maior)
    #Contagem Maus Tratos Menor
    ContagemMausTratos_Menor = dadoMenor.groupby(['MausTratos']).size()
    #print(ContagemMausTratos_Menor)

    #Contagem Liberdade Maior
    ContagemLiberdade_Maior = dadoMaior.groupby(['Liberdade']).size()
    #print(ContagemLiberdade_Maior)
    #Contagem Liberdade Menor
    ContagemLiberdade_Menor = dadoMenor.groupby(['Liberdade']).size()
    #print(ContagemLiberdade_Menor)

    #Contagem Repressão Maior
    ContagemRepressão_Maior = dadoMaior.groupby(['Repressão']).size()
    #print(ContagemRepressão_Maior)
    #Contagem Repressão Menor
    ContagemRepressão_Menor = dadoMenor.groupby(['Repressão']).size()
    #print(ContagemRepressão_Menor)

    #Contagem Liberdade de Expressão Maior
    ConatgemLiberdadeExpressão_Maior = dadoMaior.groupby(['LiberdadeExpressão']).size()
    #print(ConatgemLiberdadeExpressão_Maior)
    #Contagem Liberdade de Expressão Menor
    ContagemLiberdadeExpressão_Menor = dadoMenor.groupby(['LiberdadeExpressão']).size()
    #print(ContagemLiberdade_Menor)

    #Plotando o grafico

    plt.subplot(3,3,1)
    plt.pie(ContagemDireitoVida_Maior, labels=ContagemDireitoVida_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,2)
    plt.pie(ContagemViolencia_Maior, labels=ContagemViolencia_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,3)
    plt.pie(ContagemEscravidao_Maior, labels=ContagemEscravidao_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,4)
    plt.pie(ContagemMausTratos_Maior, labels=ContagemMausTratos_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,5)
    plt.pie(ContagemLiberdade_Maior, labels=ContagemLiberdade_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,6)
    plt.pie(ContagemLiberdade_Maior, labels=ContagemLiberdade_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,7)
    plt.pie(ContagemRepressão_Maior, labels=ContagemRepressão_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.subplot(3,3,8)
    plt.pie(ConatgemLiberdadeExpressão_Maior, labels=ConatgemLiberdadeExpressão_Maior, autopct='%1.0f%%')
    plt.legend()

    plt.show()
