import PySimpleGUI as sg
import pandas as pd

def Checar_usuario():
    Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')

    nome = str(input('Qual o Usuario que quer ver?')).capitalize()

    if nome not in Excel_file['Nome']:
        dado = Excel_file.loc[Excel_file['Nome'] == f'{nome}']
        print(dado)
    else:
        print('usuario não existe')
