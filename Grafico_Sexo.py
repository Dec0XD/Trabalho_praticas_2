import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def sexo_usuarios():
    Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')
    print(Excel_file)

    Contagem = Excel_file.groupby(['Sexo']).size()
    print(Contagem)

    plt.hist(Excel_file['Sexo'])
    plt.title('Quantidade de Homens e Mulheres que responderam a pesquisa')
    plt.xlabel('Masculino X Feminino')
    plt.ylabel('Quantidade')
    plt.show()
    