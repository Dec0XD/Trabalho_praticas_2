import PySimpleGUI as sg
import pandas as pd


def tabela_geral():
    Excel_file = 'Banco_de_dados_praticas.xlsx'
    df = pd.read_excel(Excel_file)
    print(df)
    