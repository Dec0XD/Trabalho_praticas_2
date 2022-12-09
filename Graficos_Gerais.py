import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')
print(Excel_file)
Contagem = Excel_file.groupby(['Sexo'])

Contagem1 = Excel_file.groupby(['DireitoVida']).size()
Contagem2 = Excel_file.groupby(['Violência']).size()
Contagem3 = Excel_file.groupby(['Escravidão']).size()
Contagem4 = Excel_file.groupby(['MausTratos']).size()
Contagem5 = Excel_file.groupby(['Liberdade']).size()
Contagem6 = Excel_file.groupby(['Repressão']).size()
Contagem7 = Excel_file.groupby(['LiberdadeExpressão']).size()
print(Contagem1)
print(Contagem2)
print(Contagem3)
print(Contagem4)
print(Contagem5)
print(Contagem6)
print(Contagem7)
Total = Contagem1 + Contagem2 + Contagem3 + Contagem4 + Contagem5 + Contagem6 +Contagem7
print(Total)


x = np.array(Contagem1[1])
y = np.array(Contagem1[0])
x2 = np.array(Contagem2[1])
y2 = np.array(Contagem2[0])
x3 = np.array(Contagem3[1])
y3 = np.array(Contagem3[0])
x4 = np.array(Contagem4[1])
y4 = np.array(Contagem4[0])
x5 = np.array(Contagem5[1])
y5 = np.array(Contagem5[0])
x6 = np.array(Contagem6[1])
y6 = np.array(Contagem6[0])
x7 = np.array(Contagem7[1])
y7 = np.array(Contagem7[0])

plt.plot(x, y, color='green', marker='o')
plt.plot(x2, y2, color='black', marker='o')
plt.plot(x3, y3, color='red', marker='o')
plt.plot(x4, y4, color='blue', marker='o')
plt.plot(x5, y5, color='pink', marker='o')
plt.plot(x6, y6, color='violet', marker='o')
plt.plot(x7, y5, color='orange', marker='o')
plt.xlabel('True')
plt.ylabel('False')



plt.show()
