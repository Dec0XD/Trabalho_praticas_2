import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabela import *
from Checar_usuario import*
from Grafico_Total_Violaçoes import *
from Grafico_18_porcento import *
from Grafico_Total_18 import *
from Grafico_Idade import *
from Grafico_Sexo import*
from Grafico_Genero import*
from Grafico_Total_Genero import *
from Graficos_Gerais import *


#Tema do GUI
sg.theme('Dark2')

#Puxando banco de dados pelo pandas
Excel_file = 'Banco_de_dados_praticas.xlsx'
df = pd.read_excel(Excel_file)

#Criando as telas do sistema
#Tela inicial
def janela_principal():
    
    TelaInicio = [
        [sg.Text('Escolha uma das Opções!', font=("Helvetica", 25), pad=(0, 0))],
    ]
    
    ColunaOpçoes = [
        [sg.Text('Responder a pesquisa', font='arial 12')],
        [sg.Text('Dados gerais dos respondentes:', font='arial 12')],
        [sg.Text('Dados filtrados dos respondentes', font='arial 12')],
        [sg.Text('Estatisticas dos respondentes', font='arial 12')],
    ]
        
    ColunaBotoes = [
        [sg.Button('ir para',  key='InicioPesquisa')],
        [sg.Button('ir para', key='InicioDados')],
        [sg.Button('ir para', key='InicioDadosIndividuais')],
        [sg.Button('ir para', key='InicioEstatisticas')],
        
    ]
    
    Botoes = [
        [sg.Button(' SAIR DO SISTEMA ', key='Sair')]
    ]
    
    layout = [
        [sg.Text('Nome do programa(to sem ideia)', font='arial 12 bold', size=(30, 1), pad=((0, 15), 0))],
        [sg.Column(TelaInicio, justification='center')],
        [sg.Column(ColunaOpçoes, pad=((0, 30),0)),
        sg.Column(ColunaBotoes, justification='center')],
        [sg.Column(Botoes, justification='center')]
    ]
    return sg.Window('Inicio', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True) 
    
#tela da pesquisa
def janela_Pesquisa():
    
    principal = [
        [sg.Text('Preencha as cedulas abaixo', font=("Helvetica", 25), pad=(0, 0))],
    ]
    
    ColunaDados = [
        [sg.Text('Qual o seu nome?', size=(20, 0))],
        [sg.Text('Informe sua idade:', size=(20, 0))],
        [sg.Text('Qual o seu gênero')],
        [sg.Text('Informe sua orientação sexual')],
        [sg.Text('Se outros, informe qual:')]
    ]
    
    ColunaInput = [
        [sg.Input(font='arial 12 ', key='Nome', do_not_clear=True, size=(35, 1))],
        [sg.Input(font='arial 12 ', key='Idade', size=(3, 1))],
        [sg.InputCombo(('Masculino', 'Feminino', 'Prefiro não dizer'),key='Sexo', size=(20, 1))],
        [sg.InputCombo(('Transgênero', 'Cisgênero', 'Não-binário', 'Agênero', 'Outros', 'Prefiro não dizer'),key='Gênero', size=(20, 1))],
        [sg.Input('', key='outros')]
    ]
    
    TituloCheckbox = [
        [sg.Text('Já sofreu algum tipo de violação de direitos humanos?', font=("Helvetica", 15), pad=(0, 0))],
        [sg.Text('Se sim - Marque quais já sofreu', font=('Helvetica', 15), pad=(0, 0))],
        [sg.Text('Se não - Desconsidere', font=('Helvetica', 15), pad=(0, 0))]
    ]
    
    Checkbox = [
        [sg.Checkbox('Já teve seu direito a vida comprometido?', key='DireitoVida')],
        [sg.Checkbox('Já sofreu violência?', key='Violência')],
        [sg.Checkbox('Já foi obrigado a fazer trabalho escravo?', key='Escravidão')],
        [sg.Checkbox('Já sofreu tortura ou maus tratos?', key='MausTratos')],
        [sg.Checkbox('Já sofreu um julgamento injusto ou teve sua liberdade retirada?', key='Liberdade')],
        [sg.Checkbox('Já foi reprimido?', key='Repressão')],
        [sg.Checkbox('já tentaram retirar à sua liberdade de expressão?', key='LiberdadeExpressão')], 
    ]
    
    Botoes = [
        [sg.Button('Enviar', font='arial 12', size=(10, 1), pad=((0, 15), 0)),
         sg.Button('Limpar', font='arial 12', size=(8, 1), pad=((0, 15), 0)),
         sg.Button('Voltar', font='arial 12', size=(8, 1), pad=((0, 15), 0)),
         sg.Button('Sair', font='arial 12', size=(8, 1))]
    ]
    
    layout = [
        [sg.Column(principal, justification='center')],
        [sg.Column(ColunaDados, pad=((0, 30),0)),
        sg.Column(ColunaInput, justification='center')],
        [sg.Column(TituloCheckbox, justification='center')],
        [sg.Column(Checkbox, justification='center', pad=((0, 5), 0))],
        [sg.Column(Botoes, justification='center')]
    ]
    
    return sg.Window('Pesquisa', element_padding=(0, 10), layout=layout, size=(600, 800), finalize=True) 

#tela de dados de quem responde
def Janela_Usuario():
 
    usuario = [
        [sg.Text('Informe o id do Usuario', font='arial 12', pad=(0, 0))],
        [sg.Input(size=(20, 0), font='arial 12', pad=(0, 0), key='Id')]
    ]
    
    coluna1 = [
        [sg.Text('NOME:', font='arial 12')],
        [sg.Text('IDADE:', font='arial 12')],
        [sg.Text('GÊNERO:', font='arial 12')],
        [sg.Text('ORIENTAÇÃO SEXUAL:', font='arial 12')],
        [sg.Text('OUTROS:', font='arial 12')],
    ]
    
    coluna2 = [
        [sg.Input(font='arial 12 bold', key='Nome_Consulta', size=(35, 1))],
        [sg.Input(font='arial 12 bold', key='Idade', size=(35, 1))],
        [sg.Input(font='arial 12 bold', key='genero', size=(35, 1))],
        [sg.Input(font='arial 12 bold', key='orientação_sexual', size=(35, 1))],
        [sg.Input(font='arial 12 bold', key='outros', size=(35, 1))],
    ]
    
    botoes = [
        [sg.Button('Consultar',key='Consulta', font='arial 12', size=(10, 1), pad=((0, 15), 0)),
         sg.Button('Voltar', font='arial 12', size=(8, 1), pad=((0, 15), 0)),
        sg.Button('Sair', font='arial 12', size=(8, 1), pad=((0, 15), 0))],
    ]
    
    layout = [
        [sg.Text('Consultar Usuario', font=("Helvetica", 25), justification='center')],
        [sg.Column(usuario, justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0)),
        sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]
    ]
    
    
    return sg.Window('ConsultaUsuario', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True)
    
#Tela de dados individuais


#Telas de estatistica
def janela_graficos():
    
    TelaInicio = [
        [sg.Text('Escolha qual grafico quer ver!', font=("Helvetica", 25), pad=(0, 0))],
    ]
    
    ColunaOpçoes = [
        [sg.Text('Respostas das pesquisas', font='arial 12',pad=(0, 8))],
        [sg.Text('Geral por violação', font='arial 12',pad=(0, 8))],
        [sg.Text('Idade dos respondentes', font='arial 12',pad=(0, 8))],
        [sg.Text('Sexo dos respondentes', font='arial 12',pad=(0, 8))],
        [sg.Text('Gênero dos respondentes', font='arial 12',pad=(0, 8))],
        [sg.Text('Direitos Violados por idade', font='arial 12',pad=(0, 8))],
        [sg.Text('Direitos Violados por sexo', font='arial 12',pad=(0, 8))],
    ]
        
    ColunaBotoes = [
        [sg.Button('ir para', font='arial 12',  key='TabelaPesquisas',pad=(0, 5))],
        [sg.Button('ir para', font='arial 12', key='GraficoGeral',pad=(0, 5))],
        [sg.Button('ir para', font='arial 12', key='Graficoidade',pad=(0, 5))],
        [sg.Button('ir para', font='arial 12', key='GraficioSexo',pad=(0, 5))],
        [sg.Button('ir para', font='arial 12', key='GraficoGenero',pad=(0, 5))],
        [sg.Button('ir para', font='arial 12', key='GraficoDireitosIdade',pad=(0, 5))],
        [sg.Button('ir para', font='arial 12', key='GraficoDireitosgenero',pad=(0, 5))],
        
    ]
    
    Botoes = [
        [sg.Button('Voltar', font='arial 12', size=(8, 1), pad=((0, 15), 0)),
        sg.Button('Sair', font='arial 12', size=(8, 1), pad=((0, 15), 0))],
    ]
    
    layout = [
        [sg.Column(TelaInicio, justification='center')],
        [sg.Column(ColunaOpçoes, pad=((0, 30),0)),
        sg.Column(ColunaBotoes, justification='center')],
        [sg.Column(Botoes, justification='center')]
    ]
    return sg.Window('Inicio', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True) 

#Grafico para idade/Nome
#Grafico dos direitos
#tela de fim



#Quando quiser limpar dados
def Limpar_janela():
    for key in Dados:
        Janela[key]("")
    return None
 
#Criando as janelas iniciais 
PaginaPrincipal, SegundaPagina = janela_principal(), None
#Criando o loop de leitura e enviando dados para o excel
while True:
    Janela, evento, Dados = sg.read_all_windows()
   
    #Quando a janela for fechada ou clicar para sair
    if evento in (sg.WIN_CLOSED, 'Sair'):
        break
    
        #Quando quiser limpar o formulario
    if evento == 'Limpar':
        Limpar_janela()
        
    #envio de formulario para o banco de dados
    if evento == 'Enviar':
        df = df.append(Dados, ignore_index=True)
        df.to_excel(Excel_file, index=False)
        sg.popup('Usuário salvo do Banco de dados!')
        Limpar_janela()
    
    #Quando quiser voltar para a anterior
    if Janela == SegundaPagina and evento == 'Voltar':
        SegundaPagina.hide()
        PaginaPrincipal.un_hide()
        
    #Quando for para a pagina de pesquisa
    if Janela == PaginaPrincipal and evento == 'InicioPesquisa':
        PaginaPrincipal.hide()
        SegundaPagina = janela_Pesquisa()
    
    #Quando for para a pagina de Dados gerais
    if Janela == PaginaPrincipal and evento == 'InicioDados':
        SegundaPagina = tabela_geral()
        
    #Quando for para a pagina de usuarios
    if Janela == PaginaPrincipal and evento == 'InicioDadosIndividuais':
        SegundaPagina = Checar_usuario()
       
    #Quando abrir as estatisticas
    if Janela == PaginaPrincipal and evento == 'InicioEstatisticas':
        PaginaPrincipal.hide()
        SegundaPagina = janela_graficos()     
    
    #Graficos
    #Ver Total das pesquisas
    if evento == 'TabelaPesquisas':
        SegundaPagina == total_pesquisa()
    elif evento == 'GraficoGeral':
        SegundaPagina = grafico_geral()
    #Ver Idades
    elif evento == 'Graficoidade':
        SegundaPagina = idade()
    #Ver Sexos
    elif evento == 'GraficioSexo':
        SegundaPagina = sexo_usuarios()
    #Ver Generos
    elif evento == 'GraficoGenero':
        SegundaPagina = genero_usuarios()
    #direitos violados por idade
    elif evento == 'GraficoDireitosIdade':
        SegundaPagina = total_idade()
        SegundaPagina = grafico_porcentagem_18()
    #direitos violados por genero
    elif evento == 'GraficoDireitosgenero':
        SegundaPagina = total_genero()
