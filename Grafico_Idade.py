import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def idade():
    Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')

    Banco = Excel_file.to_numpy()
    emOrdem = Banco.transpose()
    sorted_Banco = emOrdem[:, np.argsort(emOrdem[1])]

    x = np.array(sorted_Banco[1])
    y = np.array(sorted_Banco[0])


    def grafico_idade(x, y):
        Contagem = Excel_file.groupby(['Idade']).size()
        print(Contagem)


        plt.plot(x, y, color='green', marker='o')
        plt.xlabel('idade')
        plt.ylabel('Nome')
        return plt.gcf()

    layout = [
            [sg.Text('Grafico Idades')],
            [sg.Canvas(size=(1000, 1000), key='CANVAS')],
            [sg.Exit()]]

    def plotando_GraficoIdade(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    idades = sg.Window('Grafico das idades', layout, finalize=True, element_justification='center')

    plotando_GraficoIdade(idades['CANVAS'].TKCanvas, grafico_idade(x, y))

    while True:
        event, values = idades.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    idades.close()
