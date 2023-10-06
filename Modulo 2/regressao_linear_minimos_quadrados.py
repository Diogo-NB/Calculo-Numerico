#%%
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 10

"""

x = [4.3, 4.5, 5.9, 5.6, 6.1, 5.2, 3.8, 2.1, 7.5]
y = [126, 121, 116, 118, 114, 118, 132, 141, 108]

# y = a1x + a0

plt.plot(x, y, 'o', color='black')
plt.ylabel('Partículas removidas (Mg / m3)')
plt.xlabel('Chuvas diárias (0,01 cm)')
#plt.show()

x = np.array(x, dtype="float64")
y = np.array(y, dtype="float64")

n = x.shape[0]

Sx = 0
Sy = 0
Sxy = 0
Sx2 = 0
Sy2 = 0

# Calculando as somas
for i in range(n):
    Sx += x[i]
    Sy += y[i]
    Sxy += x[i] * y[i]
    Sx2 += x[i] * x[i]
    Sy2 += y[i] * y[i]

# médias
avg_x = Sx / n
avg_y = Sy / n

# Cálculo de a1 e a0
a1 = (n*Sxy - Sx*Sy ) / (n*Sx2 - Sx*Sx)
a0 = avg_y - a1*avg_x

# Soma dos quadrados dos resíduos estimados
Sr = 0
# Soma total dos quadrados em torno da média da variável dependente y é dada por
St = 0

for i in range(n):
    e = y[i] - a0 - a1*(x[i])
    Sr += e*e
    St = (y[i] - avg_y) * (y[i] - avg_y)

# Coeficiente de Determinação
r2 = (St - Sr) / St

print("a1 =", a1, "\na0 =", a0, "\nr² =", round(r2, 9))

novo_y = np.zeros(n)

for i in range(n):
    novo_y[i] = a1*x[i] + a0

plt.plot(x, novo_y, color='red')
plt.show()

