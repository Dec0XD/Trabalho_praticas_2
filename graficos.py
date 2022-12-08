import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')

def separa_velho_e_jovem(value):
    color = 'red' if value <= 25 else 'black'
    return 'color: %s' % color

    fifa19[['Age']].style.applymap(separa_velho_e_jovem)

Banco = Excel_file.to_numpy()
emOrdem = Banco.transpose()
sorted_Banco = emOrdem[:, np.argsort(emOrdem[1])]
Violencia = emOrdem[:, np.argsort(emOrdem[1])]
print(sorted_Banco)

x = np.array(Violencia[0])
y = np.array(Violencia[2])




plt.plot(x, y, color='green')
plt.xlabel('Nome')
plt.ylabel('Sofreu')
plt.show()