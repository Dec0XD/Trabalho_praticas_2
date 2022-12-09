import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')

Contagem = Excel_file.groupby(['Idade']).size()
print(Contagem)

Banco = Excel_file.to_numpy()
emOrdem = Banco.transpose()
sorted_Banco = emOrdem[:, np.argsort(emOrdem[1])]

x = np.array(sorted_Banco[1])
y = np.array(sorted_Banco[0])

plt.plot(x, y, color='green', marker='o')
plt.xlabel('idade')
plt.ylabel('Nome')
plt.show()
