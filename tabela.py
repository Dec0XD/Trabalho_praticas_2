import PySimpleGUI as sg
import pandas as pd


def tabela_geral():
    Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')
    Contagem = Excel_file.groupby(['Idade']).size()


    contact_information_array = [
        [Excel_file["Nome"],Excel_file["Idade"],[Excel_file['Sexo']],[Excel_file['Gênero']],[Excel_file['outros']]],
    ]

    headings = ['Nome', 'Idade', 'Sexo','Gênero','outros'
    ]

    layout = [
            [sg.Table(values=contact_information_array, 
            headings=headings, 
            max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=10,
                        key='-TABLE-',
                        row_height=35)],
            [sg.Button('Voltar', font='arial 12', size=(8, 1), pad=((0, 15), 0)),
            sg.Button('Sair', font='arial 12', size=(8, 1), pad=((0, 15), 0))],
        ]

    window = sg.Window("Informações dos usuários", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
            
    window.close()
    