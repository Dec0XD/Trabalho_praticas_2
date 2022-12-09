import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


Excel_file = pd.read_excel('Banco_de_dados_praticas.xlsx')
print(Excel_file)

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

plt.subplot(3,3,1)
plt.hist(Total[0], label='False', color='red')
plt.xlabel('Total de falsos')
plt.legend()

plt.subplot(3,3,2)
plt.hist(Total[1], label='True')
plt.xlabel('Total de verdadeiros')
plt.legend()

plt.subplot(3,3,3)
plt.hist(Contagem1[1], label='True')
plt.hist(Contagem1[0], label='False')
plt.xlabel('Direito a vida')
plt.legend()

plt.subplot(3,3,4)
plt.hist(Contagem2[1], label='True')
plt.hist(Contagem2[0], label='False')
plt.xlabel('violência')
plt.legend()

plt.subplot(3,3,5)
plt.hist(Contagem3[1], label='True')
plt.hist(Contagem3[0], label='False')
plt.xlabel('Escravidão')
plt.legend()

plt.subplot(3,3,6)
plt.hist(Contagem4[1], label='True')
plt.hist(Contagem4[0], label='False')
plt.xlabel('MausTratos')
plt.legend()

plt.subplot(3,3,7)
plt.hist(Contagem5[1], label='True')
plt.hist(Contagem5[0], label='False')
plt.xlabel('Liberdade')
plt.legend()

plt.subplot(3,3,8)
plt.hist(Contagem6[1], label='True')
plt.hist(Contagem6[0], label='False')
plt.xlabel('Repressão')
plt.legend()

plt.subplot(3,3,9)
plt.hist(Contagem7[1], label='True')
plt.hist(Contagem7[0], label='False')
plt.xlabel('Liberdade de Expressão')
plt.legend()



plt.show() 