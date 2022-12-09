import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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
#print(ContagemDireitoVida_Maior)
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
print(ContagemRepressão_Maior)
#Contagem Repressão Menor
ContagemRepressão_Menor = dadoMenor.groupby(['Repressão']).size()
print(ContagemRepressão_Menor)

#Contagem Liberdade de Expressão Maior
ConatgemLiberdadeExpressão_Maior = dadoMaior.groupby(['LiberdadeExpressão']).size()
print(ConatgemLiberdadeExpressão_Maior)
#Contagem Liberdade de Expressão Menor
ContagemLiberdadeExpressão_Menor = dadoMenor.groupby(['LiberdadeExpressão']).size()
print(ContagemLiberdade_Menor)


#Tamanho das barras
TamanhoBarra = 0.1

#Tamanho do Grafico


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
plt.bar(r1, ContagemDireitoVida_Maior, width=TamanhoBarra, label='Direito a vida')
plt.bar(r2, ContagemViolencia_Maior,width=TamanhoBarra, color='red', label='Violência')
plt.bar(r3, ContagemEscravidao_Maior,width=TamanhoBarra, color='orange', label='Escravidão')
plt.bar(r4, ContagemMausTratos_Maior, width=TamanhoBarra, color='pink', label='Maus Tratos')
plt.bar(r5, ContagemLiberdade_Maior, width=TamanhoBarra, color='violet', label='Libedade')
plt.bar(r6, ContagemRepressão_Maior, width=TamanhoBarra, color='black', label='Repressão')
plt.bar(r7, ConatgemLiberdadeExpressão_Maior, width=TamanhoBarra, color='green', label='Liberdade de expressão')
plt.xticks([r + TamanhoBarra for r in range(len(ContagemMaior))], ['Não Sofreram','Sofreram',])
plt.legend()

plt.title('Pessoas Maiores de 18 x Menores de 18')

plt.subplot(2,1,2)
plt.bar(r1, ContagemDireitoVida_Menor, width=TamanhoBarra, label='Direito a vida')
plt.bar(r2, ContagemViolencia_Menor,width=TamanhoBarra, color='red', label='Violência')
plt.bar(r3, ContagemEscravidao_Menor,width=TamanhoBarra, color='orange', label='Escravidão')
plt.bar(r4, ContagemMausTratos_Menor, width=TamanhoBarra, color='pink', label='Maus Tratos')
plt.bar(r5, ContagemLiberdade_Menor, width=TamanhoBarra, color='violet', label='Libedade')
plt.bar(r6, ContagemRepressão_Menor, width=TamanhoBarra, color='black', label='Repressão')
plt.bar(r7, ContagemLiberdadeExpressão_Menor, width=TamanhoBarra, color='green', label='Liberdade de expressão')
plt.xticks([r + TamanhoBarra for r in range(len(ContagemMaior))], ['Não Sofreram','Sofreram',])
plt.legend()


plt.show()
