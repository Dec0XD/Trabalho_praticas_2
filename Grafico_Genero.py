import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')
print(Excel_file)

Contagem = Excel_file.groupby(['Gênero']).size()
print(Contagem)

plt.hist(Excel_file['Gênero'])
plt.title('Grafico de Gêneros dos usuários')
plt.xlabel('Gêneros')
plt.ylabel('Quantidade')

plt.show()